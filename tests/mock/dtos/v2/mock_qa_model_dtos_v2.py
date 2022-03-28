import factory
from factory import fuzzy
from factory.random import randgen
from dtos import QAModelCreateRequestV2
from .mock_visitor_dto_v2 import MockVisitorEnforcedRequestV2


class FuzzyVersion(fuzzy.BaseFuzzyAttribute):
    def fuzz(self):
        maj = randgen.randint(10, 99)
        min = randgen.randint(100, 999)
        return f'{maj}.{min}'


class MockQAModelCreateRequestV2(MockVisitorEnforcedRequestV2):
    class Meta:
        model = QAModelCreateRequestV2

    ml_type = fuzzy.FuzzyChoice(['BERT',
                                'BERT-FINE-TUNED',
                                 'XLNET',
                                 'NLTK-GENERIC'])
    ml_version = FuzzyVersion()
    bleu_score = fuzzy.FuzzyFloat(0.0, 1.0, 2)
    rouge_score = fuzzy.FuzzyFloat(0.0, 1.0, 2)
    meteor_score = fuzzy.FuzzyFloat(0.0, 1.0, 2)
