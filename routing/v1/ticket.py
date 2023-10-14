import uuid
import random

from fastapi import APIRouter, HTTPException
from utils.data import russian_alphabet

router = APIRouter(prefix="/api/v1/ticket", tags=["ticket"])


@router.post(
    "",
    description="получение электронного талона"
)
def get_ticket():
    random_index = random.randint(0, len(russian_alphabet) - 1)

    random_letter = russian_alphabet[random_index]
    return f"{random_letter}-{random.randint(1, 200)}"
