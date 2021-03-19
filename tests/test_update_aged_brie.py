import unittest
from gilded_rose import AgedBrie


class UpdateAgedBrieItemTest(unittest.TestCase):

    def setUp(self):
        self.quality = 12
        self.sell_in = 20
        self.item = AgedBrie('Aged BRie', self.sell_in, self.quality)

    def test_quality_always_is_increased_by_one(self):
        self.item.sell_in = 1
        self.item.update()
        self.assertEqual(self.item.quality, self.quality + 1)
        self.assertEqual(self.item.sell_in, 0)
        self.item.update()
        self.assertEqual(self.item.quality, self.quality + 2)

    def test_quality_should_not_be_incremented_greather_than_fifty(self):
        self.item.quality = 49
        self.item.update()
        self.assertEqual(self.item.quality, 50)
        self.assertEqual(self.item.sell_in, self.sell_in - 1)
        self.item.update()
        self.assertEqual(self.item.quality, 50)
        self.assertEqual(self.item.sell_in, self.sell_in - 2)
