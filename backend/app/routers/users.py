from fastapi import APIRouter
from app.schemas.user import UserRegister


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register")
def register(user: UserRegister):
    return{
        "message": "User registered successfully"
    }
