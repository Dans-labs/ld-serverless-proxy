from fastapi import FastAPI, Request
from mangum import Mangum
import requests
import re
import os
import json
import urllib3, io

app = FastAPI(
    # if not custom domain
    # openapi_prefix="/prod"
)


#app.include_router(api_router, prefix=API_V1_STR)
http = urllib3.PoolManager()


@app.get("/ping")
def pong():
    """
    Sanity check.

    This will let the user know that the service is operational.

    And this path operation will:
    * show a lifesign

    """
    return {"ping": "pong!"}

@app.get("/test")
def pong():
    return {"test": "pong!"}

@app.get("/concepts/{vocab}/{term}/", tags=["namespace"])
def namespace(vocab: str, term: str, request: Request):
    artnamespace = {}
    artnamespace['ns'] = vocab
    artnamespace['term'] = term
    return artnamespace

handler = Mangum(app) #, enable_lifespan=False)

print('test')
a = 1
if a:
    artnamespace = {}
    # https://www.wikidata.org/wiki/Special:EntityData/Q82069695.json”
    cache_url = "https://www.wikidata.org/wiki/Special:EntityData/Q82069695.json"
    term = 'str'
    artnamespace['term'] = term
    if term:
        r = requests.get(cache_url)
        artnamespace['json'] = r.json()
    print(artnamespace)
