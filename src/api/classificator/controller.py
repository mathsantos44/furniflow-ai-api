from fastapi import status, HTTPException, Depends, Query

from src.api.classificator.models.output import OutputModel
from src.api.common.custom_router import CustomAPIRouter
from src.application.classificator.dependencies import resolve_classificator_service
from src.application.classificator.service import ClassificatorService

router = CustomAPIRouter(prefix='/classify', tags=['Classify Product Type'])


@router.get('/', status_code=status.HTTP_200_OK)
async def classify(product: str = Query(...), quantity: str = Query(...),
                   service: ClassificatorService = Depends(resolve_classificator_service)):
    try:
        product_type = await service.classify_text(product)
        return OutputModel(product=product, quantity=quantity, type=product_type)

    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
