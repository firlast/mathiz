from http_pyparser.parser import HTTPData
from wsblib.request import RequestData

from .mathiz import Mathiz

http_data = HTTPData()
request = RequestData(http_data, (), {})

__version__ = '0.1.0'
