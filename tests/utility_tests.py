from nose.tools import *
from utility.list_utilities import *


def test_swap():
    lst = [1, 2]
    swap(lst, 0, 1)
    assert_equal(lst, [2, 1])

    lst = [1, 2, 3, 4]
    swap(lst, 1, 3)
    assert_equal(lst, [1, 4, 3, 2])
