from typing import Any

import httpx
from fastapi import (
    APIRouter,
    FastAPI,
    Response,
    status,
)
from pydantic import BaseModel

ROUTER = APIRouter()


class EchoRequestBody(BaseModel):
    message: str


@ROUTER.get("/hello")
async def read_hello(response: Response) -> dict[str, str]:
    response.status_code = status.HTTP_200_OK
    return {"message": "Hello, World!"}


@ROUTER.get("/httpbin")
async def httpbin(response: Response) -> dict[str, Any]:
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://httpbin.org/get")
        response.status_code = resp.status_code
        return resp.json()


@ROUTER.post("/echo")
async def echo(body: EchoRequestBody, response: Response) -> dict[str, str]:
    response.status_code = status.HTTP_200_OK
    return {"message": body.message}


def create_app() -> FastAPI:
    app = FastAPI(docs_url="/")
    app.include_router(ROUTER)
    return app


if __name__ == "__main__":
    import uvicorn

    app = create_app()
    uvicorn.run(app, host="localhost", port=8000)
