from dataclasses import dataclass
from models.qa_model import QAModel


@dataclass
class ModelAvgScore(object):
    score_avg: float
    qa_model: QAModel
