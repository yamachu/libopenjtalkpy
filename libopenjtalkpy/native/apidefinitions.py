'''Definition of LibOpenJTalk apis
'''

import ctypes

from libopenjtalkpy import helper
from libopenjtalkpy.native import instance


_Open_JTalk_initialize = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_initialize', ctypes.c_void_p,
    [])

_Open_JTalk_clear = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_clear', None,
    [ctypes.POINTER(ctypes.c_void_p)])

_Open_JTalk_load = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_load', ctypes.c_int,
    [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])

_Open_JTalk_destroy_buffer = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_destroy_buffer', None,
    [ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_short))])

_Open_JTalk_synthesis_buffer = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_synthesis_buffer', ctypes.c_int,
    [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_short))])

_Open_JTalk_synthesis = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_synthesis', ctypes.c_int,
    [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])

_Open_JTalk_extract_label = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_extract_label', ctypes.c_int,
    [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_char_p)), ctypes.POINTER(ctypes.c_int)])

_Open_JTalk_synthesis_labels = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_synthesis_labels', ctypes.c_int,
    [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])

_Open_JTalk_resynthesis_buffer = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_resynthesis_buffer', ctypes.c_int,
    [ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_short))])

_Open_JTalk_resynthesis = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_resynthesis', ctypes.c_int,
    [ctypes.c_void_p, ctypes.c_char_p])

_Open_JTalk_dict_gen = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_dict_gen', ctypes.c_int,
    [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])

_Open_JTalk_set_sampling_frequency = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_set_sampling_frequency', None,
    [ctypes.c_void_p, ctypes.c_size_t])

_Open_JTalk_set_fperiod = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_set_fperiod', None,
    [ctypes.c_void_p, ctypes.c_size_t])

_Open_JTalk_set_alpha = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_set_alpha', None,
    [ctypes.c_void_p, ctypes.c_double])

_Open_JTalk_set_beta = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_set_beta', None,
    [ctypes.c_void_p, ctypes.c_double])

_Open_JTalk_set_speed = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_set_speed', None,
    [ctypes.c_void_p, ctypes.c_double])

_Open_JTalk_add_half_tone = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_add_half_tone', None,
    [ctypes.c_void_p, ctypes.c_double])

_Open_JTalk_set_msd_threshold = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_set_msd_threshold', None,
    [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_double])

_Open_JTalk_set_gv_weight = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_set_gv_weight', None,
    [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_double])

_Open_JTalk_set_volume = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_set_volume', None,
    [ctypes.c_void_p, ctypes.c_double])

_Open_JTalk_set_audio_buff_size = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_set_audio_buff_size', None,
    [ctypes.c_void_p, ctypes.c_size_t])

_Open_JTalk_set_lf0_array = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_set_lf0_array', None,
    [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.c_size_t])

_Open_JTalk_set_lf0 = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_set_lf0', None,
    [ctypes.c_void_p, ctypes.c_double, ctypes.c_size_t])

_Open_JTalk_get_lf0_length = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_get_lf0_length', ctypes.c_int,
    [ctypes.c_void_p])

_Open_JTalk_get_lf0_array = helper._safe_func_modify(instance._LibOpenJTalk,
    'Open_JTalk_get_lf0_array', None,
    [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.c_size_t])
