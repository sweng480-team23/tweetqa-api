


from containers import Container
from controllers.v2.abstract.abstract_create_read_controller_v2 import AbstractCreateReadControllerV2
from controllers.v2.abstract.abstract_read_controller_v2 import AbstractReadControllerV2
from dtos.v2.account_dto_v2 import AccountLoginRequestV2, AccountLoginResponseV2
from services import account_service
from services.account_service import AccountService
from dependency_injector.wiring import inject, Provide



class AccountsView(AbstractReadControllerV2):

    @inject
    def __init__(
            self,
            account_service: AccountService = Provide[Container.account_service],
    ):
        super().__init__(
            service=account_service,
            response_dto=AccountLoginResponseV2,
            # request_dto=AccountLoginRequestV2
        )
        self.service = account_service

    def admin_login(self, request:dict):
        """Controller function to perform admin login authentication and return the token"""

        dto_admin = AccountLoginRequestV2(request)
        print(dto_admin)
        print(dto_admin.email)
        print(dto_admin.password)
        new_accservice = AccountService()
        try:
            login_admin = new_accservice.login(dto_admin.email, dto_admin.password)
            login_response = AccountLoginResponseV2(login_admin)
            return login_response, 200
        
        except Exception as e:
            print(e)
            return None, 404
