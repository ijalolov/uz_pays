from .base import *
try:
    from .local_settings import *
except ModuleNotFoundError:
    pass
