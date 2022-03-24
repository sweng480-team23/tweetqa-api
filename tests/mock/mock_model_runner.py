import string
from typing import Tuple
import random


class MockModelRunner(object):
    def answer_tweet_question(self, tweet, question) -> Tuple[str, int, int]:
        answer = ''.join(random.choices(string.ascii_letters, k=150))

        return answer, 0, 0