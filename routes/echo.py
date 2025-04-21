from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, Dict, Any


router = APIRouter()

class EchoData(BaseModel):
    message: Optional[str] = None
    data: Optional[Dict[str, Any]] = None


@router.get("/echo", response_model=EchoData)
async def echo_get(message: Optional[str] = None):
    """Эхо через GET запрос"""
    return {"message": message}


@router.post("/echo", response_model=EchoData)
async def echo_post(data: EchoData):
    """Эхо через POST запрос"""
    print(data)
    return data


@router.api_route("/echo/all", methods=["GET", "POST", "PUT", "DELETE"])
async def echo_all(request: Request):
    """Эхо для любого метода, возвращает все данные запроса"""
    request_data = {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "query_params": dict(request.query_params),
        "path_params": request.path_params,
    }
    
    try:
        body = await request.json()
        request_data["body"] = body
    except:
        pass
    
    return JSONResponse(content=request_data)