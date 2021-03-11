import unittest
from items import CONJURED_PREFIX, Item, update_special_item


class UpdateConjuredItemTest(unittest.TestCase):

    def setUp(self):
        self.quality = 12
        self.sell_in = 1
        self.item = Item(f'{CONJURED_PREFIX} Mana Cake', self.sell_in, self.quality)

    def test_decrement_quality_by_two(self):
        update_special_item(self.item)
        self.assertEqual(self.item.quality, self.quality - 2)
        self.assertEqual(self.item.sell_in, self.sell_in - 1)

    def test_decrement_quality_by_four_after_sell_in_limit(self):
        self.item.sell_in = 0
        update_special_item(self.item)
        self.assertEqual(self.item.quality, self.quality - 4)

    def test_quality_should_not_be_decremented_less_than_zero(self):
        self.item.quality = 0
        update_special_item(self.item)
        self.assertEqual(self.item.quality, 0)
