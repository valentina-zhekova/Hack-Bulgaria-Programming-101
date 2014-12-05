from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from connection import Base
from question import Question

DATABASE_NAME = "game_database.db"

engine = create_engine("sqlite:///{}".format(DATABASE_NAME))
Base.metadata.create_all(engine)


def start_questions_collection(engine):

    session = Session(bind=engine)

    q1 = "What is the answer to 6 x 6?"
    q2 = "What is the answer to 2 ^ 8?"
    q3 = "What is the answer to 5 + 1?"
    q4 = "What is the answer to 1 + 1?"

    session.add_all([Question(question=q1, answer=answer_is(q1)),
                     Question(question=q2, answer=answer_is(q2)),
                     Question(question=q3, answer=answer_is(q3)),
                     Question(question=q4, answer=answer_is(q4))])

    session.commit()


# function should calculate the answer on it's own
def answer_is(question):
    math_expression = question[len("What is the answer to "):-1]
    pass
