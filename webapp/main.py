from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from transformers import pipeline
from pydantic import BaseModel

generator = pipeline('text-generation', model='gpt2')

app = FastAPI()

class Body(BaseModel):
    text:str

@app.get('/')
def root():
    HTMLResponse("<h1> First hugging face implementaion via fast api </h1>")

@app.post('/generate')
def predict(body:Body):
    results = generator(body.text, max_length=35, num_return_sequences=1)
    return results[0]