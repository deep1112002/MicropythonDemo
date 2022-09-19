import gc
from sys import modules
def reload_obj(mod):
    mod_name=mod.__name__
    del modules[mod_name]
    gc.collect()
    return __import__(mod_name)