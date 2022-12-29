from fastapi import FastAPI

app = FastAPI()


@app.get("/")       # path operation decorator
async def root():   # path operation function
    return {"message": "Hello World, Hung"}
