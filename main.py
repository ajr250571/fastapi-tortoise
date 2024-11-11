# main.py
from fastapi import FastAPI
from routes import router

app = FastAPI(title="FastAPI Pony Demo")
app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
