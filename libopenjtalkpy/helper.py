from libopenjtalkpy import _LibOpenJTalk_LIBRARY_PATH
from libopenjtalkpy.logger import _get_logger


def _safe_func_modify(instance, symbole_name, restype, argtypes):
    _tmp_func = None

    try:
        _tmp_func = instance[symbole_name]
        _tmp_func.restype = restype
        _tmp_func.argtypes = argtypes

    except Exception:
        _get_logger().error(
            'Symbol {} is not included in {}'.format(symbole_name, _LibOpenJTalk_LIBRARY_PATH))

    return _tmp_func
