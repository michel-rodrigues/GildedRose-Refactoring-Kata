# -*- coding: utf-8 -*-

BACKSTAGE_PASSES_PREFIX = 'Backstage passes'
SULFURAS_PREFIX = 'Sulfuras'
AGED_BRIE_PREFIX = 'Aged Brie'


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f'Item({self.name}, {self.sell_in}, {self.quality})'


def update_regular_item(item):
    if item.quality > 0:
        if item.sell_in > 0:
            item.quality -= 1
        else:
            item.quality -= 2
    item.sell_in -= 1


def update_aged_brie(item):
    item.quality += 1
    item.sell_in -= 1


def update_backstage_passes(item):
    if item.sell_in <= 0:
        item.quality = 0
    else:
        if item.sell_in > 10 and item.quality <= 50:
            item.quality += 1
        else:
            if 6 < item.sell_in <= 10 and item.quality <= 50:
                item.quality += 2
            elif item.sell_in <= 5 and item.quality <= 50:
                item.quality += 3
    item.sell_in -= 1


def update_sulfuras(item):
    pass


SPECIAL_CASES = (
    (AGED_BRIE_PREFIX, update_aged_brie),
    (SULFURAS_PREFIX, update_sulfuras),
    (BACKSTAGE_PASSES_PREFIX, update_backstage_passes),
)


def update_special_item(item):
    for prefix, handler in SPECIAL_CASES:
        if item.name.startswith(prefix):
            handler(item)


def is_special_item(item):
    return any((
        item.name.startswith(SULFURAS_PREFIX),
        item.name.startswith(AGED_BRIE_PREFIX),
        item.name.startswith(BACKSTAGE_PASSES_PREFIX),
    ))


class GildedRose():

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.quality == 50:
                item.sell_in -= 1
            else:
                if is_special_item(item):
                    update_special_item(item)
                else:
                    update_regular_item(item)
