from dependency_injector import containers, providers
import services


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[
        "controllers.v2"
    ])
    visitor_service = providers.Factory(services.VisitorService)
    training_service = providers.Factory(services.TrainingService)
    prediction_service = providers.Factory(services.PredictionService)
    model_service = providers.Factory(services.QAModelService)
    data_service = providers.Factory(services.DataService)
    account_service = providers.Factory(services.AccountService)
