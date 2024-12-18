from fastapi import APIRouter, Depends

from app.api import controller
from app.api.controller.rooms import RoomsController

router = APIRouter()


@router.get("/")
async def rooms(
        conntroller:RoomsController=Depends()
):
    return await controller.get_rooms()

