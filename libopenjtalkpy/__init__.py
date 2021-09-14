'''LibOpenJTalk library wrapper
'''

import sys
import pkg_resources


def _get_platform():
    '''Get current platform

    Returns:
        str: current platform (win, mac, linux) and (32, 64) or ""
    '''

    platform = ''
    if sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
        platform = 'win'
    elif sys.platform.startswith('darwin'):
        platform = 'mac'
    elif sys.platform.startswith('linux'):
        platform = 'linux'
    return "{}_{}".format(platform, 64 if sys.maxsize > 2**32 else 32)


def _get_library(platform):
    '''Get native LibOpenJTalk library name

    Args:
        platform (str): current platform

    Returns:
        str: Library file name

    Raises:
        Exception: When current platform not win, mac or linux, throw
    '''

    if platform == 'win_32':
        return 'libopenjtalk_32.dll'
    elif platform == 'win_64':
        return 'libopenjtalk_64.dll'
    elif platform.startswith('mac'):
        return 'libopenjtalk.dylib'
    elif platform.startswith('linux'):
        return 'libopenjtalk.so'
    else:
        raise Exception('This architecture is not supported')


# def get_native_library_version():
#     '''Get native library version

#     Returns:
#         str: NativeLibraryVersion
#             format: {version-tag}_{libopenjtalk-base-commit-hash}
#     '''

#     import ctypes
#     from libopenjtalkpy.helper import _safe_func_modify


#     instance = ctypes.cdll.LoadLibrary(_LibOpenJTalk_LIBRARY_PATH)
#     getWorldLibraryInfo = _safe_func_modify(instance, 'getWorldLibraryInfo', ctypes.c_char_p, None)

#     return getWorldLibraryInfo().decode('utf-8').strip()


def get_native_library_path():
    '''Get native library path

    Returns:
        str: NativeLibraryPath
    '''

    return _LibOpenJTalk_LIBRARY_PATH


_LibOpenJTalk_LIBRARY_PATH = pkg_resources.resource_filename(__name__, _get_library(_get_platform()))
