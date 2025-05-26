from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
import keyword_mapper

class Query(BaseModel):
    question: str

class Answer(BaseModel):
    message: str


app = FastAPI()

#Post endpoint that gets user question and returns it back
@app.post("/", response_model=Answer)
def post_query(request: Query):
    print(request.question)
    return {"message":keyword_mapper.find_best_response("keywords.txt", request.question)}


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
