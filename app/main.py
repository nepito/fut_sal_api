import json
from fastapi import FastAPI


f = open("./data/fixtures.json")
fixtures = json.load(f)
app = FastAPI(
    title="API of NIES",
    description="API made by NIES",
    summary="API about data of using by NIES",
    version="0.1.0",
    contact={
        "name": "NIES",
        "url": "https://github.com/niesfutbol",
        "email": "nepo@nies.futbol",
    },
    license_info={
        "name": "AGPL-3.0 license",
        "url": "https://github.com/niesfutbol/fut_sal_api/blob/develop/LICENSE",
    },
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/v1/fixtures/")
def get_fixture():
    return fixtures
