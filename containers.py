from dependency_injector import containers, providers
import services


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[
        "controllers.v2"
    ])
    visitor_service = providers.Factory(services.VisitorService)
    prediction_service = providers.Factory(services.PredictionService)
    model_service = providers.Factory(services.QAModelService)
    data_service = providers.Factory(services.DataService)
