import requests
import mysql.connector
from mysql.connector import errorcode
import html
import db

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
                k = html.unescape(k)
            unescaped.append(dict)        
        return unescaped
    else:
        return trivia_response["response_code"]


class Question():
    def __init__(self, question, answers) -> None:
        self.question = question
        self.answers = answers
        self.correct_a = answers[1]
        self.incorrect_a = answers[0]

    def combine_q_a(self):
        pass


class Trivia():
    def __init__(self, trivia_json) -> None:
        self.trivia_json = trivia_json
        self.difficulty = self.make_difficulty()
        self.questions = self.get_questions()
        self.scores = self.make_scores()

    def get_questions(self):
        """retrieve questions """
        qs_dict = {i['question']:[i['incorrect_answers'], i['correct_answer']] for i in self.trivia_json}
        return qs_dict

    def make_difficulty(self):
        difficulty = {i['question']:i['difficulty'] for i in self.trivia_json}
        conversion = {'easy': 1, 'medium': 2, 'hard': 3}
        
        for k, v in difficulty.items():
            difficulty[k] = conversion[v]
        return difficulty
    
    def get_difficulty(self):
        return self.difficulty
    
    def get_scores(self):
        return self.scores

    def make_scores(self):
        scores = {k:v*2 for (k, v) in self.difficulty.items()}
        return scores

    def input_questions():
        stmt = "INSERT INTO questions ()"
        pass

    def get_scores():
        pass 

    def update_score(userid: str, score:int):
        pass

    def give_question(difficulty:int):
        pass
