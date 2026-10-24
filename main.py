import funcs
import wish
st5chances = funcs.get5StarChances()
st4chances = funcs.get4StarChances()

def formWishlist(p4star, p5star):
    return funcs.formWishlist(p4star, p5star)

def config():
    print("Введите параметры для симулятора (неверное или пустое приравнивается к 0):")
    try: wishnum = int(input("Количество круток для симуляции (1-10000): "))
    except: wishnum = 0

    try: p4st = int(input("Текущее 4-звёздное крутка (0-10): "))
    except: p4st = 0

    try: p5st = int(input("Текущее 5-звёздное крутка (0-90): "))
    except: p5st = 0

    try: st5const = int(input("Консты на легу: "))
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
    if wishnum < 1 or wishnum > 10000: wishnum = 0
    if p4st < 0 or p4st > 10: p4st = 0
    if p5st < 0 or p5st > 90: p5st = 0
    if st5const < 0 or st5const > 6: st5const = 0
    if b4st1const < 0 or b4st1const > 6: b4st1const = 0
    if b4st2const < 0 or b4st2const > 6: b4st2const = 0
    if b4st3const < 0 or b4st3const > 6: b4st3const = 0
    if avlPlsInShop < 0 or avlPlsInShop > 5: avlPlsInShop = 0
    if avlStardustInShop < 0: avlStardustInShop = 0
    if avlStarglitterInShop < 0: avlStarglitterInShop = 0
    return [wishnum, p4st, p5st, st5const, b4st1const, b4st2const, b4st3const, avlPlsInShop, avlStardustInShop, avlStarglitterInShop]

config_values = config()
wishnum = config_values[0]
p4st = config_values[1]
p5st = config_values[2]
st5const = config_values[3]
b4st1const = config_values[4]
b4st2const = config_values[5]
b4st3const = config_values[6]
avlPlsInShop = config_values[7]
avlStardustInShop = config_values[8]
avlStarglitterInShop = config_values[9]

for i in range(wishnum):
    wishlist = funcs.formWishlist(p4st, p5st)
    try:
        result = wish.wish(wishlist[0])
        print(f"Результат крутки {i+1}: {result}")
        if result == "4star":
            p4st = 1
            p5st += 1
        elif result == "5star":
            p5st = 1
            p4st += 1
        else:
            p4st += 1
            p5st += 1
        
    except Exception as e:
        print(f"wishlist: {wishlist[0]}")
        print(f"Ошибка при крутке {i+1}: {e}")
