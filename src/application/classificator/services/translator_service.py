import asyncio
import logging
import traceback

from httpx import AsyncClient, Timeout

from src.settings import get_settings

_setting = get_settings()
logger = logging.getLogger(__name__)


class TranslatorService:
    def __init__(self, translator_url: str = _setting.translator_url):
        self._translator_url = translator_url

    async def request_translate(self, payload):
        async with AsyncClient(timeout=Timeout(timeout=30.0)) as client:
            try:
                response = await client.post(
                    self._translator_url,
                    json=payload
                )

                return response.json()['translatedText']

            except Exception as e:
                logger.error(f'Error translation: {e}')
                traceback.print_stack()
                return None

    async def translate_to_portuguese(self, text: str) -> str | None:
        payload = {
            'q': text,
            'source': 'en',
            'target': 'pt',
        }

        return await self.request_translate(payload)

    async def translate_to_english(self, text: str) -> str | None:
        payload = {
            'q': text,
            'source': 'pt',
            'target': 'en',
        }

        return await self.request_translate(payload)
