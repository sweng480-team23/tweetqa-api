from datetime import datetime
from dtos.v1.QAModelDTOs import QAModelCreateRequest, QAModelResponse
from dtos.v1.WordCloudDTOs import WordCloudRequest, WordCloudResponse



def create_qa_model(request: QAModelCreateRequest) -> QAModelResponse:
    pass

def read_qa_model(model_uuid: str) -> QAModelResponse:
    print(model_uuid)

    response = QAModelResponse(model_uuid=model_uuid,
                    created=datetime.now(),
                    ml_type='bert',
                    ml_version='1.0',
                    bleu_score=70.0,
                    rouge_score=70.0,
                    meteor_score=70.0)

    return response, 200

def read_latest_qa_model_by_type(model_type: str) -> QAModelResponse:
    pass

def get_word_cloud(request: WordCloudRequest) -> WordCloudResponse:
    pass
