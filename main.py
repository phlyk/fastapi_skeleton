from fastapi import FastAPI
from app.reference_endpoints import router as reference_router
from app.event_ticketing import router as event_router

app = FastAPI()

app.include_router(reference_router)
app.include_router(event_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
