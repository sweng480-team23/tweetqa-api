from datetime import date
import factory
import string
from factory import fuzzy

from dtos import DataCreateRequestV2
from dtos import DataResponseV2
from dtos import DataUpdateRequestV2
from dtos import DataCollectionResponseV2
from .mock_visitor_dto_v2 import MockVisitorEnforcedRequestV2

class MockDataCreateRequestV2(factory.Factory):
    class Meta:
        model = DataCreateRequestV2

    tweet = factory.Faker('text', max_nb_chars=400)
    question = factory.Faker('text', max_nb_chars=280)
    answer = factory.Faker('text', max_nb_chars=280)
    visitor = MockVisitorEnforcedRequestV2()

class MockDataResponseV2(factory.Factory):
    class Meta:
        model = DataResponseV2

    qid = fuzzy.FuzzyText(length=35, chars=string.ascii_letters + string.digits)
    tweet = factory.Faker('text', max_nb_chars=400)
    question = factory.Faker('text', max_nb_chars=280)
    answer = factory.Faker('text', max_nb_chars=280)
    created_date = factory.Faker('date_between_dates',
                                date_start=date(2021, 1, 1),
                                end_date=date.today())
    updated_date = factory.Faker('date_between_dates',
                                date_start=factory.SelfAttribute('..created_date'),
                                end_date=factory.SelfAttribute('..created_date'))
    source = 'SWENG480'
    start_position = factory.Faker('pyint', min_value=0, max_value=399) 
    end_position = factory.Faker('pyint', min_value=factory.SelfAttribute('..start_position'),
                                max_value=400)

class MockDataUpdateRequestV2(factory.Factory):
    class Meta:
        model = DataUpdateRequestV2

    qid = fuzzy.FuzzyText(length=35, chars=string.ascii_letters + string.digits)
    answer = factory.Faker('text', max_nb_chars=280)
    start_position = factory.Faker('pyint', min_value=0, max_value=399) 
    end_position = factory.Faker('pyint', min_value=factory.SelfAttribute('..start_position'),
                                max_value=400)
                                
class MockDataCollectionResponseV2(factory.Factory):
    class Meta:
        model = DataCollectionResponseV2

    # TODO: Implement once the DTO is implemented 