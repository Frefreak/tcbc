import time
import os
import random
import requests

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, constr

import jd_rev.sign as sign

app = FastAPI()
origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def jd_search(keyword: str):
    body_dict = {"keyword": keyword}
    uuid = os.urandom(8).hex()
    client = "android"
    client_version = "9.3.8"
    st = str(int(1000 * time.time()))
    sv = "1" + str(random.randrange(3)) + str(random.randrange(3))
    function_id = "search"
    headers = {"User-Agent": "okhttp/3.12.1"}
    sig, body = sign.mk_sign(function_id, body_dict, uuid, client, client_version, st, sv)
    r = requests.post(
        "https://some_upstream_url/client.action",
        params={
            "functionId": function_id,
            "clientVersion": client_version,
            "client": client,
            "uuid": uuid,
            "st": st,
            "sv": sv,
            "sign": sig,
        },
        headers=headers,
        data={"body": body},
    )
    return r.json()

class SearchReq(BaseModel):
    keyword: constr(strict=True, min_length=1)

    class Config:
        extra = 'forbid'


@app.post("/search")
def search(r: SearchReq):
    rj = jd_search(r.keyword)
    info = rj.get('wareInfo', [])
    count = rj.get('wareCount', 0)
    return {
        'info': info,
        'count': count
    }
