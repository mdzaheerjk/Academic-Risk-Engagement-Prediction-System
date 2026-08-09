from joblib import load
from utils.path_utils import MODEL_PATH

def load_model(model_name='finalized_model.joblib'):
    model_path=MODEL_PATH/model_name
    return load(model_path)