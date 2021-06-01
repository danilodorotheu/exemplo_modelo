import pytest
from utils import util

def test_getParams():
    result = util.getParams("loc")
    assert dict == type(result)
