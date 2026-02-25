import pytest
from unittest.mock import patch
from problem1 import NaturalNumbers

# -------------------------------------------
# Fixtures and test cases for NaturalNumbers class
# -------------------------------------------
@pytest.fixture
def empty_list():
    """ Natural Numbers instance with n=0 for testing empty list scenarios """
    obj = NaturalNumbers(0)
    return obj

@pytest.fixture
def negative_n():
    """ Natural Numbers instance with negative n for testing invalid input scenarios """
    obj = NaturalNumbers(-5)
    return obj

@pytest.fixture
def filled_list():
    """ Natural Numbers instance with n=5 for testing normal scenarios """
    obj = NaturalNumbers(5)
    obj.natural_numbers = [0, 1, 2, 3, 4]
    return obj

@pytest.fixture
def filled_list_with_duplicates():
    """ Natural Numbers instance with n=5 and duplicates for testing mode calculation """
    obj = NaturalNumbers(5)
    obj.natural_numbers = [0, 1, 2, 2, 3]
    return obj

@pytest.fixture
def even_length_list():
    """ Natural Numbers instance with n=6 for testing median calculation with even length list """
    obj = NaturalNumbers(6)
    obj.natural_numbers = [0, 1, 2, 3, 4, 5]
    return obj

# --------------------------------
# __init__ tests
# _____________________________

class TestInit:
    def test_n_is_set(self):
        nn = NaturalNumbers(10)
        return nn.n == 10
    
    def test_natural_numbers_is_empty_list(self):
        nn = NaturalNumbers(10)
        return nn.natural_numbers == []
#--------------------------------
# create_list tests
# --------------------------------

class TestCreateList:
    def test_negative_n_prints_message(self, negative_n, capsys):
        negative_n.create_list()
        captured = capsys.readouterr()
        assert captured.out.strip() == "There is no list of natural numbers"

    def test_zero_n_create_empty_list(self, empty_list):
        with patch('builtins.input', return_value="0"):
            empty_list.create_list()
        assert empty_list.natural_numbers == []
    
    def test_create_list_from_input(self):
        obj = NaturalNumbers(5)
        with patch('builtins.input', side_effect=["0", "1", "2", "3", "4"]):
            obj.create_list()
        assert obj.natural_numbers == [0, 1, 2, 3, 4]

    def test_list_length_matches_n(self):
        obj = NaturalNumbers(5)
        with patch('builtins.input', side_effect=["0", "1", "2", "3", "4"]):
            obj.create_list()
        assert len(obj.natural_numbers) == obj.n

##---------
# mean tests
# --------------------------------

class TestMean:
    def test_mean_empty_list(self, empty_list, capsys):
        empty_list.mean()
        captured = capsys.readouterr()
        assert "empty" in captured.out

    def test_mean_calculation(self, filled_list,capsys):
        filled_list.mean()
        captured = capsys.readouterr()
        assert "2.0" in captured.out
    
    def test_mean_prints_result(self, filled_list,capsys):
        filled_list.mean()
        captured = capsys.readouterr()
        assert "The mean of the list of natural numbers is: 2.0" in captured.out

# --------------------------------
# median tests
# --------------------------------

class TestMedian:

    def test_median_empty_list(self, empty_list, capsys):
        empty_list.median()
        captured = capsys.readouterr()
        assert "empty" in captured.out

    def test_median_calculation_odd_length(self, filled_list, capsys):
        filled_list.median()
        captured = capsys.readouterr()
        assert "2" in captured.out

    def test_median_calculation_even_length(self, even_length_list, capsys):
        even_length_list.median()
        captured = capsys.readouterr()
        assert "2.5" in captured.out

    def test_median_prints_result(self, filled_list, capsys):
        filled_list.median()
        captured = capsys.readouterr()
        assert "The median of the list of natural numbers is: 2" in captured.out

# --------------------------------
# mode tests
# --------------------------------

class TestMode:
    
    def test_mode_empty_list(self, empty_list, capsys):
        empty_list.mode()
        captured = capsys.readouterr()
        assert "empty" in captured.out

    def test_mode_calculation_no_duplicates(self, filled_list, capsys):
        filled_list.mode()
        captured = capsys.readouterr()
        assert "0" in captured.out or "1" in captured.out or "2" in captured.out or "3" in captured.out or "4" in captured.out

    def test_mode_calculation_with_duplicates(self, filled_list_with_duplicates, capsys):
        filled_list_with_duplicates.mode()
        captured = capsys.readouterr()
        assert "2" in captured.out

    def test_mode_prints_result(self, filled_list_with_duplicates, capsys):
        filled_list_with_duplicates.mode()
        captured = capsys.readouterr()
        assert "The mode(s) of the list of natural numbers is/are: [2]" in captured.out

