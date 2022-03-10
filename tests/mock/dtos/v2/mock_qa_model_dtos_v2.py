import factory
from factory import fuzzy
from dtos import QAModelCreateRequestV2
from .mock_visitor_dto_v2 import MockVisitorEnforcedRequestV2

class MockQAModelCreateRequestV2(factory.Factory):
    class Meta:
        model = QAModelCreateRequestV2

    
    ml_type = fuzzy.FuzzyChoice(['BERT',
                                'BERT-FINE-TUNED',
                                'XLNET',
                                'NLTK-GENERIC'])
                                
    ml_version = fuzzy.FuzzyInteger(100, 999)
    bleu_score = fuzzy.FuzzyFloat(0.0, 1.0, 2)
    rouge_score = fuzzy.FuzzyFloat(0.0, 1.0, 2)
    meteor_score = fuzzy.FuzzyFloat(0.0, 1.0, 2)
    visitor = MockVisitorEnforcedRequestV2()