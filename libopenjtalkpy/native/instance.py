'''Container of LibOpenJTalk Library Instance
'''

import ctypes

from libopenjtalkpy import _LibOpenJTalk_LIBRARY_PATH


_LibOpenJTalk = ctypes.cdll.LoadLibrary(_LibOpenJTalk_LIBRARY_PATH)
