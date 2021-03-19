import unittest
from gilded_rose import Sulfuras


class UpdateSulfurasItemTest(unittest.TestCase):

    # fails on original implementation
    def test_legendary_items_quality_should_not_be_updated(self):
        item = Sulfuras('Sulfuras, Hand of Ragnaros', sell_in=None, quality=80)
        item.update()
        self.assertEqual(item.quality, 80)
