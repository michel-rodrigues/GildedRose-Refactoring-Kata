import unittest
from gilded_rose import ConjuredItem


class UpdateConjuredItemTest(unittest.TestCase):

    def setUp(self):
        self.quality = 12
        self.sell_in = 1
        self.item = ConjuredItem('Conjured Mana Cake', self.sell_in, self.quality)

    def test_decrement_quality_by_two(self):
        self.item.update()
        self.assertEqual(self.item.quality, self.quality - 2)
        self.assertEqual(self.item.sell_in, self.sell_in - 1)

    def test_decrement_quality_by_four_after_sell_in_limit(self):
        self.item.sell_in = 0
        self.item.update()
        self.assertEqual(self.item.quality, self.quality - 4)

    def test_quality_should_not_be_decremented_less_than_zero(self):
        self.item.quality = 0
        self.item.update()
        self.assertEqual(self.item.quality, 0)
