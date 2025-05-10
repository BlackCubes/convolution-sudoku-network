import logging

from .config import LOG_LEVEL
from .enums import ConvolutionSudokuNetworkEnum

LOG_FMT_DBG = "%(levelname)s:%(message)s:%(pathname)s:%(funcName)s:%(lineno)d"


class LogLevels(ConvolutionSudokuNetworkEnum):
    info = "INFO"
    warn = "WARN"
    error = "ERROR"
    debug = "DEBUG"


def configure_logging():
    log_level = str(LOG_LEVEL).upper()
    log_levels = list(LogLevels)

    if log_level not in log_levels:
        logging.basicConfig(level=LogLevels.error)
        return

    if log_level == LogLevels.debug:
        logging.basicConfig(level=log_level, format=LOG_FMT_DBG)
        return

    logging.basicConfig(level=log_level)
