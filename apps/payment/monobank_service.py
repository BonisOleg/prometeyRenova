import os
import json
import logging
from decimal import Decimal
from typing import Optional, Tuple

import requests
from django.conf import settings

logger = logging.getLogger('payment')


class MonobankAcquiringService:
    BASE_URL = 'https://api.monobank.ua'

    def __init__(self, token: Optional[str] = None, site_url: Optional[str] = None):
        self.token = token or os.getenv('MONOBANK_TOKEN') or getattr(settings, 'MONOBANK_TOKEN', None)
        self.site_url = (site_url or os.getenv('SITE_URL') or getattr(settings, 'SITE_URL', '')).rstrip('/')
        if not self.token:
            logger.error('Monobank token is not configured')

    def _headers(self) -> dict:
        return {
            'X-Token': self.token,
            'Content-Type': 'application/json',
        }

    def create_invoice(self, reference: str, amount_uah: Decimal, destination: str, comment: str,
                       validity_seconds: int = 3600) -> Tuple[Optional[str], Optional[str]]:
        try:
            amount_kop = int(Decimal(amount_uah) * 100)
            payload = {
                'amount': amount_kop,
                'ccy': 980,
                'merchantPaymInfo': {
                    'reference': str(reference),
                    'destination': destination[:255],
                    'comment': comment[:255],
                },
                'redirectUrl': f'{self.site_url}/payment/pay/{reference}/success/',
                'webHookUrl': f'{self.site_url}/payment/webhook/monobank/',
                'validity': validity_seconds,
                'paymentType': 'debit',
            }

            url = f'{self.BASE_URL}/api/merchant/invoice/create'
            resp = requests.post(url, headers=self._headers(), data=json.dumps(payload), timeout=20)
            resp.raise_for_status()
            data = resp.json()
            page_url = data.get('pageUrl')
            invoice_id = data.get('invoiceId')
            return invoice_id, page_url
        except Exception as e:
            logger.exception('Failed to create monobank invoice: %s', e)
            return None, None

    def get_invoice_status(self, invoice_id: str) -> Optional[dict]:
        try:
            url = f'{self.BASE_URL}/api/merchant/invoice/status?invoiceId={invoice_id}'
            resp = requests.get(url, headers=self._headers(), timeout=15)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            logger.exception('Failed to fetch monobank invoice status: %s', e)
            return None

