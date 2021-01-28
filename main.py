from typing import Optional
from fastapi import Depends, FastAPI
from pydantic import BaseModel
import pickle
import preprocessing
from enum import Enum

app = FastAPI()

class Ticket(BaseModel):
    text: str
    demand: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "text": "Hallo, ich bin eine Beispielnachricht für ein ml-model."
            }
        }


def load_model():
    try:
      print ('Calling Depends Function')
      global prediction_model, vectorizer
      prediction_model = pickle.load(open('models/classifier.pickle','rb'))
      vectorizer = pickle.load(open('models/vectorizer.pickle','rb'))
      print ('Models have been loaded')
    except Exception as e:
      raise ValueError('No model here')

@app.get("/api/v1/predict", response_model=Ticket)
def predict(text: str, model = Depends(load_model())):
    text_clean = preprocessing.clean(text)
    text_tfidf = vectorizer.transform([text_clean])
    demand = prediction_model.predict(text_tfidf)
    predicted = demand.item()
    return {"predicted": predicted, "text": text}

@app.post("/api/v1/predict", response_model=Ticket)
def predict(ticket: Ticket, model = Depends(load_model())):
    text_clean = preprocessing.clean(ticket.text)
    text_tfidf = vectorizer.transform([text_clean])
    demand = prediction_model.predict(text_tfidf)
    ticket.demand = demand.item()
    return ticket
