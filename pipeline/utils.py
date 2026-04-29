import logging
logging.basicConfig(level=logging,INFO)
logger = logging.getLogger(__name__)

from .utils import logger
def run_preprocessing(years: list[int]):
  logger info("Loading data for years: %s", years)
  ...
