'''APIs of LibOpenJTalk
'''

import ctypes

from libopenjtalkpy.native import apidefinitions, utils


def initialize():
    '''Initialize OpenJTalk Instance

    Args:

    Returns:
        ctypes.c_void_p: OpenJTalk Instance
    '''

    return apidefinitions._Open_JTalk_initialize()


def load(instance, dict_dir_path, voice_model_path, user_dict_path = None):
    '''Load dictionaries and voice model

    Args:
        instance ctypes.c_void_p: OpenJTalk Instance
        dict_dir_path str:
        voice_model_path str:
        user_dict_path str | None:

    Returns:
        boolean: success or not
    '''
    
    dict_dir_path_buf = ctypes.create_string_buffer(dict_dir_path.encode('utf-8'))
    voice_model_path_buf = ctypes.create_string_buffer(voice_model_path.encode('utf-8'))
    user_dict_path_buf = None if user_dict_path is None else ctypes.create_string_buffer(voice_model_path.encode('utf-8'))

    return apidefinitions._Open_JTalk_load(instance, dict_dir_path_buf, voice_model_path_buf, user_dict_path_buf) == 1


def extract_labels(instance, text):
    '''

    Args:
        instance ctypes.c_void_p: OpenJTalk Instance
        text str: target text

    Returns:
        List[str]: full-context labels
    '''

    label_length = ctypes.c_int()

    p = ctypes.POINTER(ctypes.c_char_p)()
    a = ctypes.create_string_buffer(text.encode('utf-8'))
    v = apidefinitions._Open_JTalk_extract_label(instance, a, ctypes.byref(p), ctypes.byref(label_length))

    pp = ctypes.cast(p, ctypes.POINTER(ctypes.c_char_p))

    labels = [pp[i].decode('utf-8') for i in list(range(label_length.value))]

    # FIXME: これだと動かない…freeしないとだめだろうけど動かないので頑張る
    # for i in list(range(label_length.value)):
    #     utils.free(ctypes.cast(pp[i], ctypes.c_char_p))

    utils.free(pp)

    return labels
