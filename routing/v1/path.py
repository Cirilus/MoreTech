from fastapi import APIRouter, HTTPException
from starlette import status

router = APIRouter(prefix="/api/v1/path", tags=["path"])


@router.post(
    "",
    description="рассчитывает расстояние между двумя точками"
)
def get_dist(pos1: float, pos2: float):

    if pos1 == None or pos2 == None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
