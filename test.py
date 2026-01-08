from fastapi import FastAPI
from pydantic import BaseModel 
import psycopg2
from psycopg2.extras import RealDictCursor



app = FastAPI()


db_neon_conn_url= "postgresql://neondb_owner:npg_KRjx2nkq8zoc@ep-fragrant-bush-adq3weqf-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

class account(BaseModel):
    acc_id : int
    acc_name : str
    acc_amount : int

def neon_connect_url():
    conn = psycopg2.connect(db_neon_conn_url)
    return conn

@app.post("/account/db/insert")
def store_accounts_in_DB(acc : account):
    conn= neon_connect_url()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    insert_query = "insert into account (id, name, amount) values (%s,%s,%s)"
    cursor.execute(insert_query, (acc.acc_id,acc.acc_name,acc.acc_amount))

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Inserted successfully"}


def save_to_file(acc: account):
    with open("account.txt", "a") as f:
        f.write(f"{acc.acc_id},{acc.acc_name},{acc.acc_amount}\n")

@app.post("/account_info")
def create_account(acc : account):
    save_to_file(acc)
    return {"message":"student data saved successfully"}

