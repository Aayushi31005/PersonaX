from fastapi import APIRouter

from app.api.routes.simulations import router as simulation_router

api_router = APIRouter()

api_router.include_router(
    simulation_router,
    prefix="/simulations",
    tags=["Simulations"],
)
