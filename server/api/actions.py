from fastapi import APIRouter

router = APIRouter(prefix="/actions")


@router.get("/")
def index():
    return "Hello"
