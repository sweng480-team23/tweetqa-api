import factory
from factory import fuzzy
from dtos import PredictionCreateRequestV2
from dtos import PredictionUpdateRequestV2
from dtos import PredictionResponseV2

from .mock_data_dtos_v2 import MockDataCreateRequestV2
from .mock_visitor_dto_v2 import MockVisitorEnforcedRequestV2


class MockPredictionCreateRequestV2(MockVisitorEnforcedRequestV2):
    class Meta:
        model = PredictionCreateRequestV2

    model_id = factory.Faker('random_int')
    datum = MockDataCreateRequestV2()

class MockPredictionUpdateRequestV2(MockVisitorEnforcedRequestV2):
    class Meta:
        model = PredictionUpdateRequestV2

    id = factory.Faker('random_int')
    is_correct = fuzzy.FuzzyChoice([True, False])
    alt_answer = factory.Faker('text', max_nb_chars=280)

