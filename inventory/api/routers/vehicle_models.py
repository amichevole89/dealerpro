from fastapi import APIRouter, Depends, HTTPException, Request, status

from inventory.api.models import VehicleModel

router = APIRouter(prefix="/models", tags=["models"])
