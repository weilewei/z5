from .file import File, N5File, ZarrFile
from .attribute_manager import set_json_encoder, set_json_decoder

__version__ = "1.4.1"
__version_info__ = tuple(int(i) for i in  __version__.split("."))

