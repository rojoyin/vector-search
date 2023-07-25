from fastapi import FastAPI

application = FastAPI()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:application", host="0.0.0.0", port=8000, reload=True)
