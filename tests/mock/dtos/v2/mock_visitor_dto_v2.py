import factory
from dtos import VisitorCreateRequestV2
from dtos import VisitorEnforcedRequest
from dtos import VisitorResponseV2

class MockVisitorCreateRequestV2(factory.Factory):
    class Meta:
        model = VisitorCreateRequestV2
    
class MockVisitorResponseV2:
    class Meta:
        model = VisitorResponseV2

    id = factory.Faker('random_int')
    token = factory.Faker('uuid4')


class MockVisitorEnforcedRequestV2(factory.Factory):
    class Meta:
        model = VisitorEnforcedRequest

    visitor = MockVisitorResponseV2()
