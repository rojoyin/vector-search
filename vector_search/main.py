from fastapi import FastAPI
from vector_search.api.routes import router

application = FastAPI()
application.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:application", host="0.0.0.0", port=8000, reload=True)
