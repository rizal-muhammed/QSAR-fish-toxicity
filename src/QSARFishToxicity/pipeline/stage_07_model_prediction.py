from QSARFishToxicity.config.configuration import ConfigurationManager
from QSARFishToxicity.components.prediction import Prediction


class PredictionPipeline:
    def __init__(self) -> None:
        pass

    def main(self, ):
        config = ConfigurationManager()
        prediction_config = config.get_prediction_config()
        prediction_params = config.get_prediction_params()

        prediction = Prediction(config=prediction_config,
                                params=prediction_params,)
        best_model = prediction.load_model()
        predicted_LC50 = prediction.predict(best_model)
        print(predicted_LC50)

