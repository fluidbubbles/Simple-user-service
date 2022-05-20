from pathlib import Path

from fastapi import FastAPI
from app.routers import users


ROOT = Path(__file__).resolve().parent.parent
app = FastAPI()

app.include_router(
    users.router,
    prefix="/users"
)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
