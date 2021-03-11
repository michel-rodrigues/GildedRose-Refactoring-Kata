def _decrease_item(item, before_sell_in, after_sell_in):
    if item.quality > 0:
        if item.sell_in > 0:
            item.quality -= before_sell_in
        else:
            item.quality -= after_sell_in
    if item.quality < 0:
        item.quality = 0
    item.sell_in -= 1


def _update_regular_item(item):
    _decrease_item(item, before_sell_in=1, after_sell_in=2)


def _update_conjured(item):
    _decrease_item(item, before_sell_in=2, after_sell_in=4)


def _update_aged_brie(item):
    item.sell_in -= 1
    if item.quality < 50:
        item.quality += 1


def _update_backstage_passes(item):
    item.sell_in -= 1
    if item.sell_in <= 0:
        item.quality = 0
    else:
        if item.sell_in > 10:
            item.quality += 1
        elif 5 < item.sell_in <= 10:
            item.quality += 2
        elif item.sell_in <= 5:
            item.quality += 3
        if item.quality > 50:
            item.quality = 50


def _update_sulfuras(item):
    pass
