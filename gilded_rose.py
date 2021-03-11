# -*- coding: utf-8 -*-

BACKSTAGE_PASSES_PREFIX = 'Backstage passes'
SULFURAS_PREFIX = 'Sulfuras'
AGED_BRIE_PREFIX = 'Aged Brie'


class GildedRose():

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name.startswith(SULFURAS_PREFIX):
                continue
            if not item.name.startswith(AGED_BRIE_PREFIX) and not item.name.startswith(BACKSTAGE_PASSES_PREFIX):
                if item.quality > 0:
                    if not item.name.startswith(SULFURAS_PREFIX):
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name.startswith(BACKSTAGE_PASSES_PREFIX):
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if not item.name.startswith(SULFURAS_PREFIX):
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if not item.name.startswith(AGED_BRIE_PREFIX):
                    if not item.name.startswith(BACKSTAGE_PASSES_PREFIX):
                        if item.quality > 0:
                            if not item.name.startswith(SULFURAS_PREFIX):
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50 and not item.name.startswith(AGED_BRIE_PREFIX):
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f'Item({self.name}, {self.sell_in}, {self.quality})'
