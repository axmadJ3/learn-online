from fastapi import FastAPI
from fastapi.routing import APIRouter

import uvicorn

from api.handlers import user_router


app = FastAPI(title="online-learning")

# create the instance for the routes
main_api_router = APIRouter()

# set routes to the app instance
main_api_router.include_router(user_router, prefix='/user', tags=['user'])
app.include_router(main_api_router)

if __name__ == "__main__":
    # run app on the host and port
    uvicorn.run(app, host="0.0.0.0", port=8000)
    