from controllers import db
from models.QAModel import QAModel

class QAModelService(object):
    def create_qa_model(self, model: QAModel) -> QAModel:
        pass

    def read_qa_model_by_uuid(self, model_uuid: str) -> QAModel:
        pass

    def read_all_qa_model_by_type(self, model_type: str) -> list:
        pass

    def read_latest_qa_model_by_type(self, model_type: str) -> QAModel:
        pass