from .special_items_handlers import _update_aged_brie, _update_backstage_passes, _update_sulfuras


BACKSTAGE_PASSES_PREFIX = 'Backstage passes'
SULFURAS_PREFIX = 'Sulfuras'
AGED_BRIE_PREFIX = 'Aged Brie'


SPECIAL_CASES = (
    (AGED_BRIE_PREFIX, _update_aged_brie),
    (SULFURAS_PREFIX, _update_sulfuras),
    (BACKSTAGE_PASSES_PREFIX, _update_backstage_passes),
)


def is_special_item(item):
    return any((
        item.name.startswith(SULFURAS_PREFIX),
        item.name.startswith(AGED_BRIE_PREFIX),
        item.name.startswith(BACKSTAGE_PASSES_PREFIX),
    ))


def update_special_item(item):
    for prefix, handler in SPECIAL_CASES:
        if item.name.startswith(prefix):
            handler(item)


def update_regular_item(item):
    if item.quality > 0:
        if item.sell_in > 0:
            item.quality -= 1
        else:
            item.quality -= 2
    if item.quality < 0:
        item.quality = 0
    item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f'Item({self.name}, {self.sell_in}, {self.quality})'
