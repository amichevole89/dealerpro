from fastapi import APIRouter

router = APIRouter(

)

@router.get("automobiles/")
def get_automobiles():
    return {"automobiles": []}

@router.get("automobiles/{automobile_id}")
def get_automobile(automobile_id: int):
    return {"automobile": automobile_id}

@router.post("automobiles/")
def create_automobile():
    return {"automobile": {}}

@router.put("automobiles/{automobile_id}")
def update_automobile(automobile_id: int):
    return {"automobile": automobile_id}

@router.patch("automobiles/{automobile_id}")
def patch_automobile(automobile_id: int):
    return {"automobile": automobile_id}

@router.delete("automobiles/{automobile_id}")
def delete_automobile(automobile_id: int):
    return {"automobile": automobile_id}
