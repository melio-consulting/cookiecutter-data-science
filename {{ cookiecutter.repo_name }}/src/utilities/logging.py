# *--- coding: utf-8 ---*
""" Logging utilities."""
import sys
import logging

log_levels = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL,
}

_default_log_level = logging.INFO


def _get_library_name() -> str:
    # return __name__.split(".")[0]
    return "mission"


def _get_file_name(name: str) -> str:
    return name.split(_get_library_name())[-1].split(".")[0].replace("/", ".")


def get_logger(name: str = None, log_level: int = None):
    """Create custom logger"""

    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    logger = logging.getLogger(_get_library_name())

    if len(logger.handlers) == 0:
        stream_handler = logging.StreamHandler(stream=sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False

    if name is not None:
        logger = logging.getLogger(_get_library_name() + _get_file_name(name))

    if log_level is None:
        logger.setLevel(_default_log_level)
    else:
        logger.setLevel(log_levels[log_level])

    return logger
