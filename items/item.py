from .items_handlers import (
    _update_aged_brie,
    _update_backstage_passes,
    _update_conjured,
    _update_regular_item,
    _update_sulfuras,
)


AGED_BRIE_PREFIX = 'Aged Brie'
BACKSTAGE_PASSES_PREFIX = 'Backstage passes'
CONJURED_PREFIX = 'Conjured'
SULFURAS_PREFIX = 'Sulfuras'

SPECIAL_CASES = (
    (AGED_BRIE_PREFIX, _update_aged_brie),
    (BACKSTAGE_PASSES_PREFIX, _update_backstage_passes),
    (CONJURED_PREFIX, _update_conjured),
    (SULFURAS_PREFIX, _update_sulfuras),
)


def is_special_item(item):
    return any((
        item.name.startswith(AGED_BRIE_PREFIX),
        item.name.startswith(BACKSTAGE_PASSES_PREFIX),
        item.name.startswith(CONJURED_PREFIX),
        item.name.startswith(SULFURAS_PREFIX),
    ))


def update_special_item(item):
    for prefix, handler in SPECIAL_CASES:
        if item.name.startswith(prefix):
            handler(item)


def update_regular_item(item):
    _update_regular_item()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f'Item({self.name}, {self.sell_in}, {self.quality})'
