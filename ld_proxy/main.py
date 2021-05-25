from fastapi import FastAPI, Request
from mangum import Mangum
import requests
import re
import os
import json
import urllib3, io

from ld_proxy.api.api_v1.api import router as api_router
from ld_proxy.core.config import API_V1_STR, PROJECT_NAME

app = FastAPI(
    title=PROJECT_NAME,
    # if not custom domain
    openapi_prefix="/prod"
)


http = urllib3.PoolManager()
app.include_router(api_router, prefix=API_V1_STR)


@app.get("/ping")
def pong():
    """
    Sanity check.

    This will let the user know that the service is operational.

    And this path operation will:
    * show a lifesign

    """
    return {"ping": "pong!"}

@app.get("/wikidata/{term}/", tags=["namespace"])
def wikidata(term: str, request: Request):
    """
    Endpoint to archive concepts from Wikidata
    """
    artnamespace = {}

    cache_url = "https://www.wikidata.org/wiki/Special:EntityData/%s.json" % term
    artnamespace['term'] = term
    try:
        r = requests.get(cache_url)
        artnamespace['json'] = r.json()
    except:
        artnamespace['json'] = 'no data' 
    return artnamespace

@app.get("/skosmos/{term}/", tags=["namespace"])
def skosmos(term: str, request: Request):
    """
    Endpoint to archive concepts from Skosmos
    """
    artnamespace = {}

    cache_url = "http://finto.fi/rest/v1/mesh/data?uri=http%3A%2F%2Fwww.yso.fi%2Fonto%2Fmesh%2F%s&format=application/json" % term
    artnamespace['term'] = term
    try:
        r = requests.get(cache_url)
        artnamespace['json'] = r.json()
    except:
        artnamespace['json'] = 'no data'
    return artnamespace

@app.get("/mesh/{term}/", tags=["namespace"])
def mesh(term: str, request: Request):
    """
    Endpoint to archive concepts from MeSH
    """
    artnamespace = {}

    cache_url = "https://id.nlm.nih.gov/mesh/%s.json-ld" % term
    artnamespace['term'] = term
    try:
        r = requests.get(cache_url)
        artnamespace['json'] = r.json()
    except:
        artnamespace['json'] = 'no data'
    return artnamespace

@app.get("/lcsh/{term}/", tags=["namespace"])
def lcsh(term: str, request: Request):
    """
    Endpoint to archive concepts from MeSH 
    """
    artnamespace = {}

    cache_url = "http://id.loc.gov/authorities/subjects/%s.skos.json" % term
    artnamespace['term'] = term
    try:
        r = requests.get(cache_url)
        artnamespace['json'] = r.json()
    except:
        artnamespace['json'] = 'no data'
    return artnamespace

@app.get("/cache/{term}/", tags=["namespace"])
def namespace(term: str, request: Request):
    artnamespace = {}

    cache_url = "https://www.wikidata.org/wiki/Special:EntityData/%s.json" % term
    artnamespace['term'] = term
    try:
        r = requests.get(cache_url)
        artnamespace['json'] = r.json()
    except:
        artnamespace['json'] = 'no data'
    return artnamespace

@app.get("/concepts/{vocab}/{term}/", tags=["namespace"])
def conceptsnamespace(vocab: str, term: str, request: Request):
    artnamespace = {}
    artnamespace['ns'] = vocab
    artnamespace['term'] = term
    return artnamespace

handler = Mangum(app) #, enable_lifespan=False)
