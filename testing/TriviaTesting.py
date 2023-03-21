import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from lib.bot import TriviaGame

if __name__ == '__main__':
    text = (TriviaGame.retrieve_trivia(5, "hard"))
    print("full json {}\n".format(text))

    t = TriviaGame.Trivia(text)
    print("questions = {}\n".format(t.get_questions()))