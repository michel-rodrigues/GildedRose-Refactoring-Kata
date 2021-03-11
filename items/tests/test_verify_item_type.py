import unittest

from items import (
    AGED_BRIE_PREFIX,
    BACKSTAGE_PASSES_PREFIX,
    SULFURAS_PREFIX,
    Item,
    is_special_item,
)

class VerifyItemTypeTest(unittest.TestCase):

    def setUp(self):
        self.quality = 12
        self.sell_in = 20
        self.item = Item('Regular Item', self.sell_in, self.quality)

    def test_regular_item_is_not_special_item(self):
        self.assertFalse(is_special_item(self.item))

    def test_aged_brie_is_special_item(self):
        self.item.name = AGED_BRIE_PREFIX
        self.assertTrue(is_special_item(self.item))

    def test_sulfuras_is_special_item(self):
        self.item.name = f'{SULFURAS_PREFIX}, Hand of Ragnaros'
        self.assertTrue(is_special_item(self.item))

    def test_backstage_passes_is_special_item(self):
        self.item.name = f'{BACKSTAGE_PASSES_PREFIX} to a Rammstein concert'
        self.assertTrue(is_special_item(self.item))
