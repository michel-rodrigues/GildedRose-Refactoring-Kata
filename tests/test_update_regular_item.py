import unittest
from gilded_rose import RegularItem


class UpdateRegularItemTest(unittest.TestCase):

    def setUp(self):
        self.quality = 12
        self.sell_in = 20
        self.item = RegularItem('Regular Item', self.sell_in, self.quality)

    def test_decrement_sell_in_by_one(self):
        self.item.update()
        self.assertEqual(self.item.sell_in, self.sell_in - 1)

    def test_decrement_quality_by_one_before_sell_in_limit(self):
        self.item.sell_in = 1
        self.item.update()
        self.assertEqual(self.item.quality, self.quality - 1)

    def test_decrement_quality_by_two_after_sell_in_limit(self):
        self.item.sell_in = 0
        self.item.update()
        self.assertEqual(self.item.quality, self.quality - 2)

    def test_quality_should_not_be_decremented_less_than_zero(self):
        self.item.quality = 0
        self.item.update()
        self.assertEqual(self.item.quality, 0)
