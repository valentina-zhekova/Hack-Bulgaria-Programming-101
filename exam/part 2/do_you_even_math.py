# a class to interact with the database
from sqlalchemy.orm import Session
from player import Player
from question import Question


class Math_Game:

    def __init__(self, engine):
        self.session = Session(bind=self.engine)
        self.questions = self.__get_questions()

    def add_player(self, nickname, scores):
        pass

    # load questions from the database shuffled
    def __get_questions():
        pass

    def ask_question():
        pass

    # and some other functions
