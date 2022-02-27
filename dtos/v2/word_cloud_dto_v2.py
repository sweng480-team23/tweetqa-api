from dataclasses import dataclass
from typing import List
from tqatypes.word_response import WordResponse


@dataclass
class WordCloudResponseV2(object):
    model_id: int
    words: List[WordResponse]
