import unittest
from items import Item, update_regular_item


class UpdateRegularItemTest(unittest.TestCase):

    def setUp(self):
        self.quality = 12
        self.sell_in = 20
        self.item = Item('Regular Item', self.sell_in, self.quality)

    def test_decrement_sell_in_by_one(self):
        update_regular_item(self.item)
        self.assertEqual(self.item.sell_in, self.sell_in - 1)

    def test_decrement_quality_by_one_before_sell_in_limit(self):
        self.sell_in = 1
        update_regular_item(self.item)
        self.assertEqual(self.item.quality, self.quality - 1)

    def test_decrement_quality_by_two_after_sell_in_limit(self):
        self.item.sell_in = 0
        update_regular_item(self.item)
        self.assertEqual(self.item.quality, self.quality - 2)

    def test_quality_should_not_be_decremented_less_than_zero(self):
        self.item.quality = 0
        update_regular_item(self.item)
        self.assertEqual(self.item.quality, 0)

    def test_quality_should_not_be_decremented_less_than_zero_even_after_sell_in_limit(self):
        self.item.quality = 1
        self.item.sell_in = 0
        update_regular_item(self.item)
        self.assertEqual(self.item.quality, 0)
