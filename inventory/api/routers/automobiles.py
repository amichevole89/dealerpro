from fastapi import APIRouter, Depends, HTTPException, Request, status

from inventory.api.models import Automobile, VehicleModel, Manufacturer
from inventory.api.queries.automobiles import AutomobileQueries

router = APIRouter(prefix="/automobiles", tags=["automobiles"])

@router.post("/", response_model=Automobile, status_code=status.HTTP_201_CREATED, summary="Create Automobile")
def create_automobile(automobile: Automobile, request: Request, queries: AutomobileQueries = Depends(),):
    automobile = queries.create_automobile(automobile)
    return automobile

@router.get("/", response_model=list[Automobile], summary="List Automobiles")
def list_automobiles(queries: AutomobileQueries = Depends(),):
    automobiles = queries.list_automobiles()
    return automobiles

@router.get("/{id}", response_model=Automobile, summary="Get Automobile")
def single_automobile(id: str, queries: AutomobileQueries = Depends(),):
    automobile = queries.single_automobile(id)
    return automobile

@router.put("/{id}", response_model=Automobile, summary="Update Automobile")
def update_automobile(id: str, queries: AutomobileQueries = Depends(),):
    automobile = queries.update_automobile(id)
    return automobile

@router.delete("/{id}", response_model=Automobile, summary="Delete Automobile")
def delete_automobile(id: str, queries: AutomobileQueries = Depends(),):
    automobile = queries.delete_automobile(id)
    return automobile

@router.patch("/{id}", response_model=Automobile, summary="Patch Automobile")
def patch_automobile(id: str, queries: AutomobileQueries = Depends(),):
    automobile = queries.patch_automobile(id)
    return automobile