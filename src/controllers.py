from fastapi import APIRouter

from src.models import Transaction
from src.services import CheckFraudService

router = APIRouter()

service = CheckFraudService()


@router.post("/check-fraud")
async def check_fraud(transaction: Transaction):
    result = await service.execute(transaction)
    return {"result": result[0], "proba": result[1]}

@router.get("/")
async def home():
    return {"message": "Acesse /docs para ver a documentação da API."}