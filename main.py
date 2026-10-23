import funcs
import wish
st5chances = funcs.get5StarChances()
st4chances = funcs.get4StarChances()


def config():
    print("Введите параметры для симулятора (неверное или пустое приравнивается к 0):")
    try: p4st = int(input("Текущее 4-звёздное крутка (0-10): "))
    except: p4st = 0

    try: p5st = int(input("Текущее 5-звёздное крутка (0-90): "))
    except: p5st = 0

    try: st5const = int(input("Консты на первую ивент 4-ку в баннере (0-6): "))
    except: st5const = 0

    try: b4st1const = int(input("Консты на первую ивент 4-ку в баннере (0-6): "))
    except: b4st1const = 0

    try: b4st2const = int(input("Консты на вторую ивент 4-ку в баннере (0-6): "))
    except: b4st2const = 0

    try: b4st3const = int(input("Консты на третью ивент 4-ку в баннере (0-6): "))
    except: b4st3const = 0

    try: avlPlsInShop = int(input("Текущее количество доступных круток в магазине за пыль (0-5): "))
    except: avlPlsInShop = 0

    try: avlStardustInShop = int(input("Текущее количество доступной звездной пыли: "))
    except: avlStardustInShop = 0

    try: avlStarglitterInShop = int(input("Текущее количество доступного звездного блеска: "))
    except: avlStarglitterInShop = 0
    if p4st < 0 or p4st > 10: p4st = 0
    if p5st < 0 or p5st > 90: p5st = 0
    if st5const < 0 or st5const > 6: st5const = 0
    if b4st1const < 0 or b4st1const > 6: b4st1const = 0
    if b4st2const < 0 or b4st2const > 6: b4st2const = 0
    if b4st3const < 0 or b4st3const > 6: b4st3const = 0
    if avlPlsInShop < 0 or avlPlsInShop > 5: avlPlsInShop = 0
    if avlStardustInShop < 0: avlStardustInShop = 0
    if avlStarglitterInShop < 0: avlStarglitterInShop = 0
    return [p4st, p5st, st5const, b4st1const, b4st2const, b4st3const, avlPlsInShop, avlStardustInShop, avlStarglitterInShop]

def formWishlist(p4star, p5star, wishnum):
    return funcs.formWishlist(p4star, p5star, wishnum)