import pytest
from unittest.mock import patch
from numlist import List

# -------------------------------------------
# Fixtures and test cases for NaturalNumbersList class
# -------------------------------------------
@pytest.fixture
def empty_list():
    """ List instance with n=0 for testing empty list scenarios """
    obj = List(0)
    return obj

@pytest.fixture
def negative_n():
    """ List instance with negative n for testing invalid input scenarios """
    obj = List(-5)
    return obj  

@pytest.fixture
def filled_list():
    """ List instance with n=5 for testing normal scenarios """
    obj = List(5)
    obj.natural_numbers = [0, 1, 2, 3, 4]
    return obj

@pytest.fixture
def filled_list_with_duplicates():
    """ List instance with n=5 and duplicates for testing mode calculation """
    obj = List(5)
    obj.natural_numbers = [0, 1, 2, 2, 3]
    return obj

@pytest.fixture
def even_length_list():
    """ List instance with n=6 for testing median calculation with even length list """
    obj = List(6)
    obj.natural_numbers = [0, 1, 2, 3, 4, 5]
    return obj

# --------------------------------
# __init__ tests
# _____________________________
class TestInit:
    def test_n_is_set(self):
        lst = List(10)
        assert lst.n == 10
    
    def test_natural_numbers_is_empty_list(self):
        lst = List(10)
        assert lst.natural_numbers == []
    
#--------------------------------
# get_list tests
# --------------------------------
class TestGetList:
    @patch('builtins.input', side_effect=['0', '1', '2', '3', '4'])
    def test_get_list_filled(self, mock_input, filled_list):
        result = filled_list.get_list()
        assert result == [0, 1, 2, 3, 4]
    @patch('builtins.input', side_effect=[])
    def test_get_list_empty(self, mock_input, empty_list):
        result = empty_list.get_list()
        assert result == []

