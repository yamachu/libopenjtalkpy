'''Utils of ctypes
'''

import sys

def free(p):
    if sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
        from ctypes import windll


        return windll.kernel32.HeapFree(None, None, p)
    else:
        from ctypes import CDLL
        from ctypes.util import find_library


        libc = CDLL(find_library('c'))

        return libc.free(p)
