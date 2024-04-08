from src.application.classificator.services.trained_model_service import TrainedModelService
from src.application.classificator.services.translator_service import TranslatorService


class ClassificatorService:
    def __init__(self, translator_service: TranslatorService, trained_model_service: TrainedModelService):
        self._translator_service = translator_service
        self._trained_model_service = trained_model_service

    async def classify_text(self, text: str) -> str | None:
        translated_text = await self._translator_service.translate_to_english(text)
        if not translated_text:
            return None

        prediction = self._trained_model_service.predict(translated_text)

        portuguese_prediction = await self._translator_service.translate_to_portuguese(prediction)
        if not portuguese_prediction:
            return None
        return portuguese_prediction

