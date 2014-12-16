from nose.tools import *
from search.binary_search import *
from search.brute_force_search import *


def test_binary_search():
    assert_equal(binary_search([1, 2, 3], 2), 1)
    assert_equal(binary_search([1, 5, 7, 8, 16, 34, 35], 34), 5)
    assert_equal(binary_search([23, 24, 25, 55, 67, 89], 23), 0)
    assert_equal(binary_search([23, 24, 25, 55, 67, 89], 89), 5)
    assert_equal(binary_search([23, 24, 25, 55, 67, 89], 57), -1)
    assert_equal(binary_search([], 57), -1)
    assert_equal(binary_search(None, 57), -1)


def test_brute_force_search():
    assert_equal(brute_force_search([1, 2, 3], 2), 1)
    assert_equal(brute_force_search([1, 5, 7, 8, 16, 34, 35], 34), 5)
    assert_equal(brute_force_search([23, 24, 25, 55, 67, 89], 23), 0)
    assert_equal(brute_force_search([23, 24, 25, 55, 67, 89], 89), 5)
    assert_equal(brute_force_search([23, 24, 25, 55, 67, 89], 57), -1)
    assert_equal(brute_force_search([], 57), -1)
    assert_equal(brute_force_search(None, 57), -1)
    assert_equal(brute_force_search([67, 24, 23, 89, 25, 55], 89), 3)
