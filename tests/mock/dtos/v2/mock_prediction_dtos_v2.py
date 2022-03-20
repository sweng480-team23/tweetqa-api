import factory
from dtos import PredictionCreateRequestV2
from dtos import PredictionUpdateRequestV2
from dtos import PredictionResponseV2

from .mock_data_dtos_v2 import MockDataCreateRequestV2


class MockPredictionCreateRequestV2(factory.Factory):
    class Meta:
        model = PredictionCreateRequestV2

    model_id = None
    datum = MockDataCreateRequestV2()


