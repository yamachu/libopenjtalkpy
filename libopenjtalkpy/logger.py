from logging import getLogger, StreamHandler


_logger = getLogger('libopenjtalkpy')
_st_handler = StreamHandler()
_logger.addHandler(_st_handler)


def _get_logger():
    return _logger
