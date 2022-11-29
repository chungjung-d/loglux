from fastapi import FastAPI
from api.route.router_index import router as api_router

app = FastAPI()


def get_application() -> FastAPI:
    application = FastAPI()

    application.include_router(api_router)

    return application

app = get_application()