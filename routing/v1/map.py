import random

from fastapi import APIRouter
from utils.data import offices, atms

router = APIRouter(prefix="/api/v1/map", tags=["map"])



@router.get(
    "/offices",
    description="получение всех офисов для отображение в картах"
)
def get_offices():
    return {
        "offices": offices[:random.randint(5, 7)]
    }

@router.get(
    "/atms",
    description="получение всех банкоматов для отображение в картах"
)
def get_atms():
    return {
        "atms": atms[:random.randint(5, 7)],
    }

