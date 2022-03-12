import factory
from decouple import config
from dtos import VisitorCreateRequestV2
from dtos import VisitorEnforcedRequest
from dtos import VisitorResponseV2


class MockVisitorCreateRequestV2(factory.Factory):
    class Meta:
        model = VisitorCreateRequestV2

    invitor_account = factory.Faker('random_int')
    emails = factory.List([factory.Faker('email')])


class MockVisitorResponseV2(factory.Factory):
    class Meta:
        model = VisitorResponseV2

    id = factory.Faker('random_int')
    token = factory.Faker('uuid4')


class MockVisitorEnforcedRequestV2(factory.Factory):
    class Meta:
        model = VisitorEnforcedRequest

    visitor = MockVisitorResponseV2()
