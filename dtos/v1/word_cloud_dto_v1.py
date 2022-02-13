from dataclasses import dataclass
from typing import List
from tqatypes.word_response import WordResponse


@dataclass
class WordCloudResponse(object):
    model_id: int
    words: List[WordResponse]

    def __init__(self, model_id, words) -> None:
        self.model_id = model_id
        self.words = words
