from nose.tools import *
from sort.insertion_sort import *
from sort.selection_sort import *


def test_insertion_sort():
    assert_equal(insertion_sort([1, 2, 3]), [1, 2, 3])
    assert_equal(insertion_sort([3, 2, 1]), [1, 2, 3])
    assert_equal(insertion_sort([2, 1, 3]), [1, 2, 3])
    assert_equal(insertion_sort([55, -4, 34, 34, 15]), [-4, 15, 34, 34, 55])
    assert_equal(insertion_sort([0.4, 567, -10006, 23, 0, 5]), [-10006, 0, 0.4, 5, 23, 567])
    assert_equal(insertion_sort([7]), [7])
    assert_equal(insertion_sort([]), [])
    assert_equal(insertion_sort(None), None)
    
    
def test_get_index_of_minimum():
    assert_equal(get_index_of_minimum([5, 56, -1, 0.9]), 2)
    assert_equal(get_index_of_minimum([-6657.89, -6657.89, 6, -6657.89, 25]), 0)
    
    
def test_selection_sort():
    assert_equal(selection_sort([1, 2, 3]), [1, 2, 3])
    assert_equal(selection_sort([3, 2, 1]), [1, 2, 3])
    assert_equal(selection_sort([2, 1, 3]), [1, 2, 3])
    assert_equal(selection_sort([55, -4, 34, 34, 15]), [-4, 15, 34, 34, 55])
    assert_equal(selection_sort([0.4, 567, -10006, 23, 0, 5]), [-10006, 0, 0.4, 5, 23, 567])
    assert_equal(selection_sort([7]), [7])
    assert_equal(selection_sort([]), [])
    assert_equal(selection_sort(None), None)
