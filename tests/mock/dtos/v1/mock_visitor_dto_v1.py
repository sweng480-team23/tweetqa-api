import factory
from dtos.v2.visitor_dto_v2 import VisitorCreateRequest
from dtos.v2.visitor_dto_v2 import VisitorResponse

class MockVisitorCreateRequest(factory.Factory):
    class Meta:
        model = VisitorCreateRequest

    invitor_account = 1
    email = factory.faker('email')


class MockVisitorResponse(factory.Factory):
    class Meta:
        model = VisitorResponse

    id = factory.faker('random_int')
    token: factory.faker('uuid4')
