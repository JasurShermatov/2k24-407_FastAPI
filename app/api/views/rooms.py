from fastapi import APIRouter, Depends

from app.api.controller.rooms import RoomsController

router = APIRouter()


@router.get("/")
async def get_rooms(
        controller: RoomsController = Depends()
):
    return await controller.get_rooms()

@router.get("/{room_id}")
async def get_room(
        controller: RoomsController = Depends(),
        room_id: int | None = None
):
    return await controller.get_room(room_id)