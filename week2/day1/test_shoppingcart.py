import pytest
from shoppingcart import ShoppingCart, Item
# -------------------------------------------
# Fixtures and test cases for ShoppingCart class
# -------------------------------------------
@pytest.fixture
def empty_cart():
    """ ShoppingCart instance with n=0 for testing empty cart scenarios """
    obj = ShoppingCart(0)
    return obj

@pytest.fixture
def filled_cart():
    """ ShoppingCart instance with n=3 for testing normal scenarios """
    obj = ShoppingCart(3)
    obj.itemlist = [
        Item(qty=2, price=10.0, name='Item1'),
        Item(qty=1, price=20.0, name='Item2'),
        Item(qty=3, price=5.0, name='Item3')
    ]
    return obj

# --------------------------------
# add_items_incart tests
# --------------------------------
class TestAddItemsInCart:

    def test_add_item_to_cart(self, empty_cart):
        empty_cart.add_items_incart(qty=2, name='Item1', price=10.0)
        assert len(empty_cart.itemlist) == 1
        assert empty_cart.itemlist[0].name == 'Item1'
        assert empty_cart.itemlist[0].qty == 2
        assert empty_cart.itemlist[0].price == 10.0
    
    def test_add_duplicate_item_to_cart(self, filled_cart):
        filled_cart.add_items_incart(qty=1, name='Item1', price=10.0)
        assert len(filled_cart.itemlist) == 3  # No new item should be added
        assert filled_cart.itemlist[0].name == 'Item1'
        assert filled_cart.itemlist[0].qty == 2
        assert filled_cart.itemlist[0].price == 10.0
    
    def test_add_item_to_full_cart(self, filled_cart):
        filled_cart.add_items_incart(qty=1, name='Item4', price=15.0)
        assert len(filled_cart.itemlist) == 3  # No new item should be added
        assert all(item.name != 'Item4' for item in filled_cart.itemlist)

    def test_add_item_with_invalid_input(self, empty_cart):
        empty_cart.add_items_incart(qty=-1, name='Item1', price=10.0)
        assert len(empty_cart.itemlist) == 0  # No item should be added due to invalid quantity
        empty_cart.add_items_incart(qty=2, name='', price=10.0)
        assert len(empty_cart.itemlist) == 0  # No item should be added due to empty name
        empty_cart.add_items_incart(qty=2, name='Item1', price=-5.0)
        assert len(empty_cart.itemlist) == 0  # No item should be added due to negative price
    
    def test_add_item_with_valid_input(self, empty_cart):
        empty_cart.add_items_incart(qty=2, name='Item1', price=10.0)
        assert len(empty_cart.itemlist) == 1  # Item should be added successfully
        assert empty_cart.itemlist[0].name == 'Item1'
        assert empty_cart.itemlist[0].qty == 2
        assert empty_cart.itemlist[0].price == 10.0
    
    def test_add_item_with_valid_input_to_filled_cart(self, filled_cart):
        filled_cart.add_items_incart(qty=1, name='Item4', price=15.0)
        assert len(filled_cart.itemlist) == 3  # No new item should be added since cart is full
        assert all(item.name != 'Item4' for item in filled_cart.itemlist)
    
    def test_add_item_with_invalid_input_to_filled_cart(self, filled_cart):
        filled_cart.add_items_incart(qty=-1, name='Item4', price=15.0)
        assert len(filled_cart.itemlist) == 3  # No new item should be added due to invalid quantity
        filled_cart.add_items_incart(qty=1, name='', price=15.0)
        assert len(filled_cart.itemlist) == 3  # No new item should be added due to empty name
        filled_cart.add_items_incart(qty=1, name='Item4', price=-5.0)
        assert len(filled_cart.itemlist) == 3  # No new item should be added due to negative price
    
    def test_add_item_with_valid_input_to_empty_cart(self, empty_cart):
        empty_cart.add_items_incart(qty=2, name='Item1', price=10.0)
        assert len(empty_cart.itemlist) == 1  # Item should be added successfully
        assert empty_cart.itemlist[0].name == 'Item1'
        assert empty_cart.itemlist[0].qty == 2
        assert empty_cart.itemlist[0].price == 10.0
    
    def test_add_item_with_invalid_input_to_empty_cart(self, empty_cart):
        empty_cart.add_items_incart(qty=-1, name='Item1', price=10.0)
        assert len(empty_cart.itemlist) == 0  # No item should be added due to invalid quantity
        empty_cart.add_items_incart(qty=2, name='', price=10.0)
        assert len(empty_cart.itemlist) == 0  # No item should be added due to empty name
        empty_cart.add_items_incart(qty=2, name='Item1', price=-5.0)
        assert len(empty_cart.itemlist) == 0  # No item should be added due to negative price
    
