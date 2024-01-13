from fastapi import APIRouter, Depends, HTTPException, Request, status

from inventory.api.models import Manufacturer

router = APIRouter(prefix="/manufacturers", tags=["manufacturers"])
