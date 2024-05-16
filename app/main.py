import json
import os
from openai import OpenAI
from fastapi import FastAPI

chatGPT_key = os.environ["chatGPT_key"]


def init_client(api_key):
    return OpenAI(api_key=api_key)


client = init_client(chatGPT_key)
promp = "haz una nota deportiva de 5 párrafos de un partido de la tercera jornada del torneo de fútbol sala FutSal NIES. Los equipos fueron Eco Pasto contra Cachorros. El marcador quedó 5 a 4 a favor de Eco Pasto. Los anotadores por Eco Pasto fueron Jared (3 goles), Saul (1 gol) y Jonathan (1 gol). Los goles de los Cachorros fueron de Jesús Trujillo (3 goles) y Adán Gómez"
response = client.chat.completions.create(
    model="gpt-3.5-turbo", messages=[{"role": "user", "content": promp}]
)
f = open("./data/fixtures.json")
fixtures = json.load(f)
app = FastAPI(
    title="API of FutSal NIES",
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


@app.get("/v1/fixtures/")
def get_fixture():
    return fixtures


@app.get("/v1/match_note/")
def get_match_note():
    return print(response)
