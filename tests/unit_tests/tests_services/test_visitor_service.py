import pytest
from typing import List
from models import Visitor
from services import VisitorService
from tests.mock.dtos.v2 import MockVisitorCreateRequestV2

@pytest.mark.visitor
def test_visitor_service_create(visitor_model: List[Visitor], visitor_service: VisitorService ):
    visitor_out = visitor_service.create(visitor_model)

    visitor_saved = [Visitor.query.filter(Visitor.id == v.id).first()
                     for v in visitor_model]

    assert all(type(v) == Visitor for v in visitor_out)
    assert all(v1 == v2 for v1, v2 in zip(visitor_saved, visitor_out))
    assert all(v1 == v2 for v1, v2 in zip(visitor_model, visitor_out))


@pytest.mark.visitor
def test_visitor_service_read(visitor_model: List[Visitor], visitor_service: VisitorService):
    visitor_service.create(visitor_model)
    visitor_out = [visitor_service.read_by_id(v.id) for v in visitor_model]

    assert all(type(v) == Visitor for v in visitor_out)
    assert all(v1 == v2 for v1, v2 in zip(visitor_model, visitor_out))


@pytest.mark.visitor
def test_visitor_service_update(visitor_model: List[Visitor], visitor_service: VisitorService):
    visitor_service.create(visitor_model)
    dto = MockVisitorCreateRequestV2()

    for v, email in zip(visitor_model, dto.emails):
        v.email = email

    visitor_out = [visitor_service.update(v) for v in visitor_model]

    assert all(type(v) == Visitor for v in visitor_out)
    assert all(v1 == v2 for v1, v2 in zip(visitor_model, visitor_out))

@pytest.mark.visitor
def test_visitor_read_by_token(visitor_model: List[Visitor], visitor_service: VisitorService):
    visitor_service.create(visitor_model)
    visitor_out = [visitor_service.read_by_token(v.token) for v in visitor_model]

    assert all(type(v) == Visitor for v in visitor_out)
    assert all(v1 == v2 for v1, v2 in zip(visitor_model, visitor_out))

@pytest.mark.visitor
def test_visitor_check_valid_visitor(visitor_model: List[Visitor], visitor_service: VisitorService):
    visitor_service.create(visitor_model)
    valid_visitors = [visitor_service.check_valid_visitor(v.token) for v in visitor_model]
    
    assert all(valid_visitors)
