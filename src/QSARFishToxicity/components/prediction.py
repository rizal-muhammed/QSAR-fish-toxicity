import pickle
import numpy as np
import pandas as pd

from QSARFishToxicity.logging import logger
from QSARFishToxicity.entity import PredictionConfig, PredictionParams


class Prediction:
    def __init__(self, config: PredictionConfig, params:PredictionParams) -> None:
        self.config = config
        self.params = params

    def load_model(self, ):
        """
            This method loads the best model and returns .

            Parameters
            ----------
            None

            Returns
            -------
            Returns the best model.

            Raises
            ------
            Exception
        
        """
        try:
            logger.info(f""" Loading the best model...""")

            model_file_path = self.config.model_dir
            with open(model_file_path, "rb") as file:
                self.model = pickle.load(file)
            
            logger.info(f""" Loading best model is successful.""")
            return self.model
        
        except Exception as e:
            logger.exception(f""" Exception while loading the best model. 
                             Exception message : {str(e)}""")
            raise e
    
    def predict(self, model):
        """
            This method predicts LC50 value with best model and returns .

            Parameters
            ----------
            model : 
                Model for prediction

            Returns
            -------
            LC50 : float
                Returns the LC50 value predicted by the model.

            Raises
            ------
            Exception
        
        """
        try:
            CIC0 = self.params.CIC0
            SM1_Dz = self.params.SM1_Dz
            GATS1i = self.params.GATS1i
            NdsCH = self.params.NdsCH
            NdssC = self.params.NdssC
            MLOGP = self.params.MLOGP

            input = np.array([[CIC0, SM1_Dz, GATS1i, NdsCH, NdssC, MLOGP]], dtype=float)
            predicted_LC50 = model.predict(input.values)

            return predicted_LC50

        except Exception as e:
            logger.exception(f"""Exception while prediction. Exception message: {str(e)}""")
            raise e

