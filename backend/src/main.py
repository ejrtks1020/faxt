from fastapi import FastAPI
from starlette.responses import JSONResponse
from contextlib import asynccontextmanager
from icecream import ic
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    ic("start")

    yield

    ic("end")

app = FastAPI(lifespan=lifespan)

@app.get('/')
def hello_world():
    return JSONResponse('hello world')

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
