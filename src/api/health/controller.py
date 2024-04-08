from fastapi import status
from src.api.common.custom_router import CustomAPIRouter

router = CustomAPIRouter(prefix='/healthcheck', tags=['Healthcheck'])


@router.get('/', status_code=status.HTTP_200_OK)
async def healthcheck():
    return {'status': 'alive'}