from fastapi import FastAPI,HTTPException
from pydantic import BaseModel 
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

client = AsyncIOMotorClient(mongo_uri)

db = client["euronDatabase"]
euron_coll = db["euron_coll"]

app = FastAPI()

class euron_pydantic(BaseModel):
    name: str
    phone: int 
    city: str
    course: str

# @app.post("/euron/insert")
# def euron_data_insert_helper(data:euron_pydantic):
#     result = euron_coll.insert_one(data)
#     return str(result.inserted_id)


@app.post("/euron/insert")
async def euron_data_insert_helper(data: euron_pydantic):
    result = await euron_coll.insert_one(data)
    return {"inserted_id": str(result.inserted_id)}

def get_helper(doc):
    doc["id"]= str(doc["_id"])
    del doc["_id"]
    return doc

@app.get("/euron/getdata")
async def get_data():  
    iterem=[]
    cursor=euron_coll.find({})
    async for document in cursor:
        print('document in loop ',document)
        iterem.append(get_helper(document))
    return iterem


