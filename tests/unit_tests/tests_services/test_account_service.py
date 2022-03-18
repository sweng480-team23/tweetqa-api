import pytest
from models import Account
from services import AccountService

@pytest.mark.account
def test_account_service_create(account_model: Account, account_service: AccountService):

    account_out = account_service.create(account_model)
    account_saved = Account.query.filter(Account.id == Account.id).first()

    assert account_saved is not None
    assert account_out is not None
    assert account_saved == account_out
    assert account_out == account_model


@pytest.mark.account
def test_acccount_service_read(account_model: Account, account_service: AccountService):

    account_service.create(account_model)
    account_out = account_service.read_by_id(account_model.id)

    assert account_out is not None
    assert account_out == account_model


@pytest.mark.account
def test_account_service_update(account_model: Account, account_service: AccountService):

    account_service.create(account_model)

    account_model.email = 'updated_tester@psu.edu'
    account_out = account_service.update(account_model)

    assert account_out is not None
    assert account_out == account_model


@pytest.mark.account
def test_account_service_login(account_model: Account, account_service: AccountService):

    account_service.create(account_model)

    account_model.email = 'updated_tester@psu.edu'
    account_out = account_service.update(account_model)

    assert account_out is not None
    assert account_out == account_model

