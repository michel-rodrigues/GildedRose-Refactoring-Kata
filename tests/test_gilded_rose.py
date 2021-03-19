import unittest
from gilded_rose import GildedRose, BackstagePasses, RegularItem


class GildedRoseTest(unittest.TestCase):

    def setUp(self):
        self.quality = 12
        self.sell_in = 20

    def test_update_regular_item(self):
        item = RegularItem('Regular Item', self.sell_in, self.quality)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, self.quality - 1)
        self.assertEqual(item.sell_in, self.sell_in - 1)

    def test_update_special_item(self):
        item = BackstagePasses(
            'Backstage passes to a Pink Floyd concert',
            self.sell_in,
            self.quality,
        )
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, self.quality + 1)
        self.assertEqual(item.sell_in, self.sell_in - 1)
