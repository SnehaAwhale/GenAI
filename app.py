
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test():
    return {"message":"This is my finance portal"}

@app.get("/home")
def home():
    return {"message":"I ma gin to create a dashboard for myself"}

data = {1:"American Express",2:"city",3:"freedom"}

@app.get("/accounts")
def accounts():
    return data

@app.get("/accounts/{accountinfo}")
def get_account(accountinfo:int):
    return {"id":accountinfo,"account":data[accountinfo]}

@app.get("/accounts/{account_id}/{accountname}")
def add_account(account_id: int, accountname: str):
    data[account_id] = accountname
    return {"status": "added", "data": data}

from pydantic import BaseModel 
class newdata(BaseModel):
    acc_id : int
    accountname : str

@app.post("/accounts/different_addition")
def add_accnt_newvalue(newdata:newdata):
    data[newdata.acc_id] = newdata.accountname
    return {"status": "added", "data": data}


