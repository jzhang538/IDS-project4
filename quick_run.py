from fastapi import FastAPI
from libs.querydatabricks import querymydb
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"Hi! Please use 'query/k' to fetch the first k records from the trip database."}

@app.get("/query/{k}")
async def query(k):
    result = querymydb(k=k)
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
