import requests
import mysql.connector
from mysql.connector import errorcode


trivia_url_base = 'https://opentdb.com/api.php?'


def retrieve_trivia(num, difficulty):
    request_url =  "{0}amount={1}&difficulty={2}".format(trivia_url_base, num, difficulty)
    try:
        trivia_response = requests.get(request_url).json()
    except requests.exceptions.RequestException as e:
        print("Bad Request")
     
    if trivia_response["response_code"] == 0:
        return trivia_response
    else:
        return trivia_response["response_code"]


class Trivia():
    def __init__(self, trivia_json) -> None:
        self.trivia_json = trivia_json
        self.trivia

    def get_questions(self):
        """retrieve questions """
        qs_list = {i['question']:[i['incorrect_answers'], i['correct_answer']] for i in self.trivia_json['results']}
        return qs_list

    def get_difficulty(self):
        difficulty = {i['question']:i['difficulty'] for i in self.trivia_json['results']}
        conversion = {'easy': 1, 'medium': 2, 'hard': 3}
        
        for k, v in difficulty.items():
            difficulty[k] = conversion[v]
        return difficulty

    def input_questions():

        pass

    def get_scores():
        pass 

    def update_score(userid: str, score:int):
        pass

    def give_question(difficulty:int):
        pass
