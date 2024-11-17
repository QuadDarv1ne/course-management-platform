from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class PaymentWebhook(BaseModel):
    payment_id: str
    status: str

@router.post("/webhook/payment/")
async def payment_webhook(webhook: PaymentWebhook):
    # Обработка данных платежа
    if webhook.status == "success":
        # Здесь должна быть логика для успешного платежа
        return {"message": "Payment processed successfully"}
    else:
        raise HTTPException(status_code=400, detail="Payment failed")
