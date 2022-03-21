from typing import Type
from dacite import from_dict
from containers import Container
from controllers.v2.abstract.abstract_create_read_controller_v2 import AbstractCreateReadControllerV2
from dtos.v2.account_dto_v2 import AccountLoginRequestV2, AccountLoginResponseV2
from services.account_service import AccountService
from dependency_injector.wiring import inject, Provide
from services.visitor_service import VisitorService

class AccountsView(AbstractCreateReadControllerV2):
    """Controller Class to handle Admin Account Operations"""

    @inject
    def __init__(
            self,
            visitor_service: VisitorService = Provide[Container.visitor_service],
            account_service: AccountService = Provide[Container.account_service],           
    ):
        super().__init__(
            service=account_service,
            visitor_service=visitor_service,
            response_dto=AccountLoginResponseV2,
            request_dto=AccountLoginRequestV2,
        )

    def admin_login(self, request:dict):
        """Controller function to perform admin login authentication and return the token"""

        dto: Type[AccountLoginRequestV2] = from_dict(data_class=self.request_dto, data = request)
        if dto.email is not None:
            try:
                login_admin = self.service.login(dto.email, dto.password)
                login_response = self.response_dto.from_model(login_admin)
                return login_response, 200
            except Exception as e:
                print(e)
                return None, 404
        else:
            return None, 403
