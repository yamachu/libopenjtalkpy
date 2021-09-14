from libopenjtalkpy.native import apis
from pprint import pprint


instance = apis.initialize()
ok = apis.load(instance,
    "PATH_TO_open_jtalk_dic_utf_8-1.11",
    "PATH_TO_nitech_jp_atr503_m001.htsvoice")

labels = apis.extract_labels(instance, "こんにちは")
pprint(labels)

labels = apis.extract_labels(instance, "さようなら")
pprint(labels)
