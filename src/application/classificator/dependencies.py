from fastapi import Depends

from src.application.classificator.service import ClassificatorService
from src.application.classificator.services.trained_model_service import TrainedModelService
from src.application.classificator.services.translator_service import TranslatorService


async def resolve_trained_model_service() -> TrainedModelService:
    yield TrainedModelService()


async def resolve_translator_service() -> TranslatorService:
    yield TranslatorService()


async def resolve_classificator_service(translator_service=Depends(resolve_translator_service),
                                        trained_model_service=Depends(
                                            resolve_trained_model_service)) -> ClassificatorService:
    yield ClassificatorService(translator_service=translator_service, trained_model_service=trained_model_service)
