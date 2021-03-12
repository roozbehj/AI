from fastapi import FastAPI
from typing import List
from pydantic import BaseModel,Field

app = FastAPI()


class InputPayload(BaseModel):
    msg: str


# SoftMatch endpoint
@app.post('/acrtest')
async def process_request(item: InputPayload):
    return item


