import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from lib.bot import TriviaGameProcessing
import unittest
import lib.db.db as db



mock_json = [{'category': 'Entertainment: Comics', 'type': 'multiple', 'difficulty': 'hard', 'question': 'What year was the first San Diego Comic-Con?', 'correct_answer': '1970', 'incorrect_answers': ['2000', '1990', '1985']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'What do the video games No Man’s Sky and Mighty No. 9 have in common?', 'correct_answer': 'Both were announced in 2013.', 'incorrect_answers': ['Both were crowdfunded.', 'Both were developed by indie studios.', 'Both were released for the PlayStation 3.']}, {'category': 'Entertainment: Comics', 'type': 'multiple', 'difficulty': 'hard', 'question': 'In 1978, Superman teamed up with what celebrity, to defeat an alien invasion?', 'correct_answer': 'Muhammad Ali', 'incorrect_answers': ['Mike Tyson', 'Sylvester Stallone', 'Arnold Schwarzenegger']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'Who is the victim mentioned in the second KG-8 incident, in Ace attorney Investigations, Case 4?', 'correct_answer': 'Deid Mann', 'incorrect_answers': ['Frank Sahwit', 'Shey De Killer', 'Raymond Shields']}, {'category': 'Mythology', 'type': 'multiple', 'difficulty': 'hard', 'question': 'Which Norse God has a horse named Sleipnir?', 'correct_answer': 'Odin', 'incorrect_answers': ['Thor', 'Frigg', 'Balder']}]

class TriviaTests(unittest.TestCase):
    
    def setUp(self) -> None:
        self._text = TriviaGameProcessing.retrieve_trivia(5, "hard")
        self._trivia =TriviaGameProcessing.Trivia(mock_json)
        

    def test_retrieval(self):
        self.assertIsInstance(self._text, list)
            
    def test_questons(self):
        self.assertIsInstance(self._trivia, TriviaGameProcessing.TriviaProcessing)
        questions = self._trivia.get_questions()
        self.assertIsInstance(questions, list)
        for i, j in zip(mock_json, questions):
            self.assertEqual(i['question'], j.get_q())
    
    def test_answers(self):
        for i in self._trivia.get_questions():
            print(i.get_correct())

if __name__ == '__main__':
    print("populating trivia db")
    trivia = TriviaGameProcessing.Trivia(mock_json)
    trivia.clear_questions()
    trivia.input_questions()
    print(trivia.get_random_question())
    
    

