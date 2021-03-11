# -*- coding: utf-8 -*-
import unittest

from gilded_rose import BACKSTAGE_PASSES_PREFIX, Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def setUp(self):
        self.quality = 12
        self.sell_in = 20
        self.item = Item('Regular Item', self.sell_in, self.quality)

    def test_decrement_sell_in_by_one(self):
        gilded_rose = GildedRose([self.item])
        gilded_rose.update_quality()
        self.assertEqual(self.item.sell_in, self.sell_in - 1)

    def test_decrement_quality_by_one_before_sell_in_limit(self):
        gilded_rose = GildedRose([self.item])
        gilded_rose.update_quality()
        self.assertEqual(self.item.quality, self.quality - 1)

    def test_decrement_quality_by_two_after_sell_in_limit(self):
        """When sell_in is less than 1."""
        self.item.sell_in = 0
        gilded_rose = GildedRose([self.item])
        gilded_rose.update_quality()
        self.assertEqual(self.item.quality, self.quality - 2)

    def test_quality_should_not_be_decremented_less_than_zero(self):
        self.item.quality = 0
        gilded_rose = GildedRose([self.item])
        gilded_rose.update_quality()
        self.assertEqual(self.item.quality, 0)

    def test_aged_brie_quality_always_is_increased_by_one(self):
        self.item.name = 'Aged Brie'
        self.item.sell_in = 1
        gilded_rose = GildedRose([self.item])
        gilded_rose.update_quality()
        self.assertEqual(self.item.quality, self.quality + 1)
        self.assertEqual(self.item.sell_in, 0)
        gilded_rose.update_quality()
        self.assertEqual(self.item.quality, self.quality + 2)
        self.assertEqual(self.item.sell_in, -1)


    def test_quality_should_not_be_incremented_greather_than_fifty(self):
        self.item.name = 'Aged Brie'
        self.item.quality = 49
        gilded_rose = GildedRose([self.item])
        gilded_rose.update_quality()
        self.assertEqual(self.item.quality, 50)
        self.assertEqual(self.item.sell_in, self.sell_in - 1)
        gilded_rose.update_quality()
        self.assertEqual(self.item.quality, 50)
        self.assertEqual(self.item.sell_in, self.sell_in - 2)

    def test_legendary_items_quality_should_not_be_updated(self):
        self.item.name = 'Sulfuras, Hand of Ragnaros'
        self.item.sell_in = None
        gilded_rose = GildedRose([self.item])
        gilded_rose.update_quality()
        self.assertEqual(self.item.quality, self.quality)

    def test_backstage_passes_quality_should_be_incremented_by_one_before_sell_in_limit(self):
        self.item.name = BACKSTAGE_PASSES_PREFIX + ' to a Pink Floyd concert'
        gilded_rose = GildedRose([self.item])
        gilded_rose.update_quality()
        self.assertEqual(self.item.quality, self.quality + 1)

    def test_backstage_passes_quality_should_be_incremented_by_two_ten_days_before_sell_in_limit(self):
        self.item.sell_in = 10
        self.item.name = BACKSTAGE_PASSES_PREFIX + ' to a Rammstein concert'
        gilded_rose = GildedRose([self.item])
        gilded_rose.update_quality()
        self.assertEqual(self.item.quality, self.quality + 2)

    def test_backstage_passes_quality_should_be_incremented_by_three_five_days_before_sell_in_limit(self):
        self.item.sell_in = 5
        self.item.name = BACKSTAGE_PASSES_PREFIX + ' to a Sepultura concert'
        gilded_rose = GildedRose([self.item])
        gilded_rose.update_quality()
        self.assertEqual(self.item.quality, self.quality + 3)

    def test_backstage_passes_quality_should_be_zero_after_sell_in_limit(self):
        self.item.sell_in = 0
        self.item.name = BACKSTAGE_PASSES_PREFIX + ' to a Tea Party concert'
        gilded_rose = GildedRose([self.item])
        gilded_rose.update_quality()
        self.assertEqual(self.item.quality, 0)


if __name__ == '__main__':
    unittest.main()
