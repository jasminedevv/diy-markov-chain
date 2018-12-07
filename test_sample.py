import pytest
from dictogram import Dictogram
from listogram import Listogram
from sample import *

hist1 = Dictogram(["one", "fish"])

def test_cumulative_dist():
    # dist1 = cumulative_dist(hist1)
    assert True