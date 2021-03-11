import unittest
from items import Item, SULFURAS_PREFIX, update_special_item

class UpdateSulfurasItemTest(unittest.TestCase):

    # fails on original implementation
    def test_legendary_items_quality_should_not_be_updated(self):
        item = Item(f'{SULFURAS_PREFIX}, Hand of Ragnaros', sell_in=None, quality=80)
        update_special_item(item)
        self.assertEqual(item.quality, 80)
