import unittest
from gilded_rose import GildedRose
from items import BACKSTAGE_PASSES_PREFIX, Item


class GildedRoseTest(unittest.TestCase):

    def setUp(self):
        self.quality = 12
        self.sell_in = 20
        self.item = Item('Regular Item', self.sell_in, self.quality)

    def test_update_regular_item(self):
        gilded_rose = GildedRose([self.item])
        gilded_rose.update_quality()
        self.assertEqual(self.item.quality, self.quality - 1)
        self.assertEqual(self.item.sell_in, self.sell_in - 1)

    def test_update_special_item(self):
        self.item.name = f'{BACKSTAGE_PASSES_PREFIX} to a System of a Down concert'
        gilded_rose = GildedRose([self.item])
        gilded_rose.update_quality()
        self.assertEqual(self.item.quality, self.quality + 1)
        self.assertEqual(self.item.sell_in, self.sell_in - 1)
