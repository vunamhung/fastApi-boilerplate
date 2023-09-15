from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    response = JSONResponse({"message": "Hello World"})
    response.set_cookie(key="abc", value="abc")
    return response
