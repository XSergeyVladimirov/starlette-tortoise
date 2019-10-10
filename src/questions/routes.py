from starlette.routing import Route, Router
from questions.views import (
    questions_all, question, question_create, answer_create, tags, search
)

questions_routes = Router([
    Route("/", endpoint=questions_all,
          methods=["GET", "POST"], name="questions_all"),
    Route("/{id:int}/{slug:str}", endpoint=question,
          methods=["GET", "POST"], name="question"),
    Route("/create", endpoint=question_create,
          methods=["GET", "POST"], name="question_create"),
    Route("/answer-create", endpoint=answer_create,
          methods=["GET", "POST"], name="answer_create"),
    Route("/tags/{tag:str}", endpoint=tags, methods=["GET"], name="tags"),
    Route("/search", endpoint=search, methods=["GET"], name="search"),
])
