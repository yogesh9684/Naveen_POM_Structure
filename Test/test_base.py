import pytest
import unittest


'''Base class for inheriting the Fixtures'''

@pytest.mark.usefixtures("init__driver")
class BaseTest():
    pass