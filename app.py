import sys

from fastapi import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware
from routing.v1.map import router as map_router
from routing.v1.path import router as path_router
from routing.v1.ticket import router as ticker_router

from configs.Environment import get_environment_variables


app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


env = get_environment_variables()


app.include_router(map_router)
app.include_router(path_router)
app.include_router(ticker_router)

if not env.DEBUG:
    logger.remove()
    logger.add(sys.stdout, level="INFO")