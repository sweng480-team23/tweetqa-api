


from dtos.v2.account_dto_v2 import AccountLoginRequestV2, AccountLoginResponseV2
from services.account_service import AccountService


def admin_login(request:dict):
    """Controller function to perform admin login authentication and return the token"""

    dto_admin = AccountLoginRequestV2(request)

    new_accservice = AccountService()
    try:
        login_admin = new_accservice.login(dto_admin.email, dto_admin.password)
        login_response = AccountLoginResponseV2(login_admin)
        return login_response, 200
        
    except Exception as e:
        print(e)
        return None, 404