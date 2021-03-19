import unittest
from gilded_rose import BackstagePasses


class UpdateBackstagePassesItemTest(unittest.TestCase):

    def setUp(self):
        self.quality = 12
        self.sell_in = 20
        self.item = BackstagePasses(
            'Backstage passes to a Pink Floyd concert',
            self.sell_in,
            self.quality,
        )

    def test_quality_should_be_incremented_by_one_before_sell_in_limit(self):
        self.item.update()
        self.assertEqual(self.item.quality, self.quality + 1)

    def test_quality_should_be_incremented_by_two_ten_days_before_sell_in_limit(self):
        self.item.sell_in = 10
        self.item.update()
        self.assertEqual(self.item.quality, self.quality + 2)

    def test_quality_should_be_incremented_by_three_five_days_before_sell_in_limit(self):
        self.item.sell_in = 5
        self.item.update()
        self.assertEqual(self.item.quality, self.quality + 3)

    # fails on original implementation
    def test_quality_should_be_zero_after_sell_in_limit(self):
        self.item.sell_in = 1
        self.item.update()
        self.assertEqual(self.item.quality, 0)
        self.assertEqual(self.item.sell_in, 0)

    def test_quality_should_not_be_incremented_over_fifty(self):
        self.item.sell_in = 10
        self.item.quality = 49
        self.item.update()
        self.assertEqual(self.item.quality, 50)
