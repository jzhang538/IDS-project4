from fastapi import FastAPI
from libs.querydatabricks import query
import uvicorn

@app.get("/")
async def root():
    return {"Hi! Please use 'query/k' to fetch the first k records from the trip database."}

@app.get("/query/{k}")
async def query(k):
    result = querydb(k)
    return {"result": result}

if __name__ == "__main__":
    app = FastAPI()
    uvicorn.run(app, port=8080, host="0.0.0.0")