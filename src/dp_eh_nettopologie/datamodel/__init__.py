from pathlib import Path
from .dp_eh_nettopologie import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "dp_eh_nettopologie.yaml"
