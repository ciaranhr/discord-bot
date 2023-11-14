import requests
import mysql.connector
from mysql.connector import errorcode
import html
from ..db import db

trivia_url_base = 'https://opentdb.com/api.php?'


def retrieve_trivia(num, difficulty):
    """collect json from trivia api and convert html encoding to plaintext
    returns: a list of dictionaries containing trivia questions and answers"""
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
    """A Question that is to be stored in a TriviaProcessing and asked of users of the game
    Answers are able to be retreived for the question
    Answers are able to be checked against correct answer"""

    def __init__(self, question: str, answers: list, difficulty: int, type: str) -> None:
        self._question = question
        self._answers = answers
        self._correct = answers[0]
        self._incorrect = answers[1]
        self._difficulty = difficulty
        self._type = type  

    def get_q(self):
        """returns: string of question"""
        return self._question
    
    def get_correct(self):
        """returns: string of correct answer"""
        return self._correct
    
    def get_incorrect(self):
        """returns: array of strings of incorrect answers"""
        return self._incorrect

    def get_type(self):
        """return: string of the type of the question"""    
        return self._type
    
    def get_all(self):
        """returns: string containig correct and incorrect answers"""
        combined = {self._question:self._answers}
        return combined
    
    def get_difficulty(self):
        """returns: integer difficulty of the question"""
        return self._difficulty
    
    def __str__(self):
        return "%s" % (self._question)

    def __repr__(self):
        return "%s" % (self._question)

def parse_questions(trivia_json:str) -> list:
    """retrieve questions from json of api
        return: list of questions"""
    difficulties = {i['question']:i['difficulty'] for i in trivia_json}
    conversion = {'easy': 1, 'medium': 2, 'hard': 3}
    
    for k, v in difficulties.items():
        difficulties[k] = conversion[v]

    questions = []
    for i in trivia_json:
            answers = [i['correct_answer'], i['incorrect_answers']]
            question = i['question']
            difficulty = difficulties[question]
            type = i['type']
            questions.append(Question(question, answers, difficulty, type))
    return questions

class TriviaProcessing():
    """Processing and populating a trivia game based on some input json"""
    def __init__(self, trivia_json) -> None: 
        self._trivia_json = trivia_json
        self._questions = parse_questions(trivia_json)

    def get_questions(self):
        """return Questions stored from json"""
        return self._questions

    def input_questions(self, num:int):
        """input a specific number of questions that have been processing"""
        if num > len(self._questions):

            raise Exception
        
        insert_question = ("INSERT INTO discordinfo.questions "
                "(question_id, type, level, trivia_score, content) " 
                "VALUES (%s, %s, %s, %s, %s)" )            

        insert_answers = ("INSERT INTO discordinfo.answers"
                          "(question_id, correct, content)"
                          "VALUES (%s, %s, %s)") 
        
        q_id = 1
        question_data = []
        answer_data = []
        for i in self._questions[:num]: 
            question_data.append((q_id, i.get_type(), i.get_difficulty(), i.get_difficulty()*3, i.get_q()))
            answer_data.append((q_id, 1, i.get_correct()))
            for j in i.get_incorrect():
                answer_data.append((q_id, 0, j))
            q_id+= 1
       
        db.multiexec(insert_question, question_data)
        db.multiexec(insert_answers, answer_data)
        db.commit()
       
        
    def clear_questions(self, question_ids=None):
        delete_all_q = ("DELETE FROM discordinfo.questions WHERE question_id > 0")
        delete_all_a = ("DELETE FROM discordinfo.answers WHERE question_id > 0")
        
        delete_some = ("DELETE FROM discordinfo.questions"
                       "WHERE question_id = %s")
        
        if question_ids == None:
            db.execute(delete_all_q)
            db.execute(delete_all_a)
        else:
            db.multiexec(delete_some, question_ids)
        db.commit()
      



            



