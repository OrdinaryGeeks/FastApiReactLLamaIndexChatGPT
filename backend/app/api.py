from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os


from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext, Document
from llama_index.llms import OpenAI
import openai

app = FastAPI()


origins = [
    "http://localhost:3000",
    "localhost:3000",
    "*"
]
todos = [
    {
        "id": "1",
        "item": "Read a book."
    },
    {
        "id": "2",
        "item": "Cycle around town."
    }
]

class Question(BaseModel):
    question: str
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

openai.api_key = "[redacted]"

documents = SimpleDirectoryReader("C:/Users/alect/Desktop/FastApipythonreact/backend/documents").load_data()
service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are helping to make a decision about whether or not to hire Nathan based upon your companies entered answers of what they are looking for and what they are like.  Also list reasons why you gave your answer"))
index = VectorStoreIndex.from_documents(documents, service_context=service_context)


from fastapi import HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException



@app.post("/shouldwehireNathan", tags=["Nathan"])
async def post_hire_nathan_question(question :Question):

    query_engine = index.as_query_engine()
    
    return query_engine.query(question.question).response

@app.get("/todo", tags=["todos"])
async def get_todos():
    return  todos




@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}


class SPAStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope):
        try:
            return await super().get_response(path, scope)
        except (HTTPException, StarletteHTTPException) as ex:
            if ex.status_code == 404:
                return await super().get_response("index.html", scope)
            else:
                raise ex

print(os.getcwd())
app.mount("/home", SPAStaticFiles(directory="./build/", html=True), name="spa-static-files")