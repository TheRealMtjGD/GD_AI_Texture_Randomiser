import dotenv as __dotenv__
import os as __os__
__dotenv__.load_dotenv()

GD_RESOURCES_PATH = __os__.getenv('gdres_path')
FLUX_MODEL = f'FLUX.1-{__os__.getenv('flux_1_model')}'
FLUX_API_KEY = __os__.getenv('bfl_api_key')
QUALITY = __os__.getenv('quality')