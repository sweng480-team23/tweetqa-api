import requests
from models.training_model import Training
from .abstract.create_read_service import CreateReadService


class TrainingService(CreateReadService):

    def __init__(self):
        super().__init__(Training)

    def create(self, training) -> (str, int):
        data: dict = {
            "epochs": training.epochs,
            "learning_rate": training.learningRate,
            "batch_size": training.batchSize,
            "base_model": training.baseModel,
            "last_x_labels": training.lastXLabels,
            "include_user_labels": training.includeUserLabels,
            "pipeline_host": 'https://426311df09ff6461-dot-us-central1.pipelines.googleusercontent.com'
        }
        response: requests.Response = requests.post(
            url='https://tweetqa-pipeline-service-d62rdgteaa-uc.a.run.app',
            json=data)

        if response.status_code == 200:
            new_training = super().create(training)
            return f"New Model Training has successfully started with parameters: {new_training}", response.status_code
        else:
            return f"An error occurred when initiating model training.  " \
                f"Status code: {response.status_code}, Reason: {response.reason}", response.status_code
