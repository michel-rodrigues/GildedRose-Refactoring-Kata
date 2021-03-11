import unittest
from items import AGED_BRIE_PREFIX, Item, update_special_item


class UpdateAgedBrieItemTest(unittest.TestCase):

    def setUp(self):
        self.quality = 12
        self.sell_in = 20
        self.item = Item(AGED_BRIE_PREFIX, self.sell_in, self.quality)

    # fails on original implementation
    def test_quality_always_is_increased_by_one(self):
        self.item.sell_in = 1
        update_special_item(self.item)
        self.assertEqual(self.item.quality, self.quality + 1)
        self.assertEqual(self.item.sell_in, 0)
        update_special_item(self.item)
        self.assertEqual(self.item.quality, self.quality + 2)

    def test_quality_should_not_be_incremented_greather_than_fifty(self):
        self.item.name = AGED_BRIE_PREFIX
        self.item.quality = 49
        update_special_item(self.item)
        self.assertEqual(self.item.quality, 50)
        self.assertEqual(self.item.sell_in, self.sell_in - 1)
        update_special_item(self.item)
        self.assertEqual(self.item.quality, 50)
        self.assertEqual(self.item.sell_in, self.sell_in - 2)
