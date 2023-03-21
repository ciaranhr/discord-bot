import requests
import mysql.connector
from mysql.connector import errorcode
import html
from ..db import db

trivia_url_base = 'https://opentdb.com/api.php?'


def retrieve_trivia(num, difficulty):
    request_url =  "{0}amount={1}&difficulty={2}".format(trivia_url_base, num, difficulty)
    try:
        trivia_response = requests.get(request_url).json()
    except requests.exceptions.RequestException as e:
        print("Bad Request")
     
    if trivia_response["response_code"] == 0:
        unescaped = []
        for dict in trivia_response['results']:
            for k in dict:
                dict[k] = html.unescape(dict[k])
            unescaped.append(dict)        
        return unescaped
    else:
        return trivia_response["response_code"]


class Question():
    """
    Questions that can be stored in a Trivia Game and asked of users of the game
    Answers able to be retreived for a given question, """
    def __init__(self, question: str, answers: list, difficulty: int, type: str) -> None:
        self.question = question
        self.answers = answers
        self.correct = answers[1]
        self.incorrect = answers[0]
        self.difficulty = difficulty
        self.type = type

    def get_q(self):
        """returns: string of question"""
        return self.question
    
    def get_correct(self):
        """returns: string of correct answer"""
        return self.correct
    
    def get_incorrect(self):
        """returns: array of strings of incorrect answers"""
        return self.incorrect
    
    def get_all(self):
        """returns: string containig correct and incorrect answers"""
        combined = {self.question:self.answers}
        return combined
    
    def get_difficulty(self):
        """returns: difficulty of the question"""
        return self.difficulty
    
    def __str__(self):
        return "% s" % (self.question)

    def __repr__(self):
        return "%s" % (self.question)
    
class Trivia():
    def __init__(self, trivia_json) -> None:
        self.trivia_json = trivia_json
        self.questions = self.get_questions()

    def get_questions(self) -> list:
        """retrieve questions from json of api
         return: list of questions"""
        difficulties = {i['question']:i['difficulty'] for i in self.trivia_json}
        conversion = {'easy': 1, 'medium': 2, 'hard': 3}
        
        for k, v in difficulties.items():
            difficulties[k] = conversion[v]

        questions = []
        for i in self.trivia_json:
                answers = [i['correct_answer'], i['incorrect_answers']]
                question = i['question']
                difficulty = difficulties[question]
                type = i['type']
                questions.append(Question(question, answers, difficulty, type))

        return questions
    

    def input_questions():
        stmt = "INSERT INTO questions ()"
        pass

    def get_scores():
        pass 

    def update_score(userid: str, score:int):
        pass

    def give_question(difficulty:int):
        pass
