class GildedRose():

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f'Item({self.name}, {self.sell_in}, {self.quality})'


def _decrease_item(item, before_sell_in, after_sell_in):
    if item.quality > 0:
        if item.sell_in > 0:
            item.quality -= before_sell_in
        else:
            item.quality -= after_sell_in
    if item.quality < 0:
        item.quality = 0
    item.sell_in -= 1


class RegularItem(Item):

    def update(self):
        _decrease_item(self, before_sell_in=1, after_sell_in=2)


class ConjuredItem(Item):

    def update(self):
        _decrease_item(self, before_sell_in=2, after_sell_in=4)


class AgedBrie(Item):

    def update(self):
        self.sell_in -= 1
        if self.quality < 50:
            self.quality += 1


class BackstagePasses(Item):

    def update(self):
        self.sell_in -= 1
        if self.sell_in <= 0:
            self.quality = 0
        else:
            if self.sell_in > 10:
                self.quality += 1
            elif 5 < self.sell_in <= 10:
                self.quality += 2
            elif self.sell_in <= 5:
                self.quality += 3
            if self.quality > 50:
                self.quality = 50


class Sulfuras(Item):

    def update(self):
        pass
