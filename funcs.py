from decimal import Decimal
from pathlib import Path
from configvars import *

fisc = []
fosc = []

def get5StarChances():
    chances = []
    with open(FIVESTARFILE, "r") as f:
        for line in f:
            chances.append(float(line))
    return chances
def get4StarChances():
    chances = []
    with open(FOURSTARFILE, "r") as f:
        for line in f:
            chances.append(float(line))
    return chances
def formWishlist(fostpity, fistpity, star4guarantee, star5guarantee):
    s5 = get5StarChances()
    s4 = get4StarChances()
    reslist = []
    if fistpity == 90:
        reslist.append([
            ["3star", 0],
            ["4star", 0],
            ["5star", 100]
        ])
    elif fostpity == 10:
        reslist.append([
            ["3star", 0],
            ["4star", 100],
            ["5star", 0]
        ])
    else:
        if (100 - Decimal(str(s5[fistpity])) - Decimal(str(s4[fostpity]))) < 0:
            reslist.append([
                ["3star", 0],
                ["4star", Decimal(str(s4[fostpity]))],
                ["5star", Decimal(str(s5[fistpity]))]
            ])
        else:
            reslist.append([
                ["3star", 100 - Decimal(str(s5[fistpity])) - Decimal(str(s4[fostpity]))],
                ["4star", Decimal(str(s4[fostpity]))],
                ["5star", Decimal(str(s5[fistpity]))]
            ])

    if not star5guarantee:
        reslist.append([
            ["lost5050_5st", 50],
            ["won5050_5st", 50]
        ])
    else:
        reslist.append([
            ["lost5050_5st", 0],
            ["won5050_5st", 100]
        ])

    if not star4guarantee:
        reslist.append([
            ["banner4st", 50],
            ["nonbanner4st", 50]
        ])
    else:
        reslist.append([
            ["banner4st", 100],
            ["nonbanner4st", 0]
        ])

    reslist.append([
        ["fstbanner4st", 33.4],
        ["scdbanner4st", 33.3],
        ["trdbanner4st", 33.3]
    ])

    another4stchars = list([i, 5.26] for i in get4starNameList(getLang()) if i not in SELECTEDCHARS)
    another4stchars[0] = [another4stchars[0][0], 5.32]
    reslist.extend(another4stchars)
    
    return reslist
def config():
    print("Введите параметры для симулятора (неверное или пустое приравнивается к 0):")
    try: wishnum = int(input("Количество круток для симуляции (1-10000): "))
    except: wishnum = 0

    try: p4st = int(input("Текущая 4-звёздное крутка (0-10): "))
    except: p4st = 0

    try: p5st = int(input("Текущая 5-звёздное крутка (0-90): "))
    except: p5st = 0

    try: st5const = int(input("Консты на легу (0-6); Пустое приравнивается к отсутствию: "))
    except: st5const = -1

    if SELECTCERTAIN4STARS:
        charlist = get4starNameList(getLang())
        selectedlist = []
        while len(selectedlist) < 3:
            name = input("Введите имя персонажа (0 для просмотра списка): ")
            if name == "0":
                print("Список доступных 4-звёздных персонажей:")
                for j, n in enumerate(get4starNameList(getLang()), start=1):
                    print(f"{j}. {n}")
                continue
            elif name and (name not in charlist or name in selectedlist):
                print("Ошибка: выбранный персонаж не найден в списке или уже выбран.\nПовторите попытку.")
                continue
            elif name and name in charlist and name not in selectedlist:
                print(f"Выбран персонаж: {name}")
                selectedlist.append(name)

        SELECTEDCHARS.extend(selectedlist)


    try: b4st1const = int(input("Консты на первую ивент 4-ку в баннере (0-6); Пустое приравнивается к отсутствию: "))
    except: b4st1const = -1

    try: b4st2const = int(input("Консты на вторую ивент 4-ку в баннере (0-6); Пустое приравнивается к отсутствию: "))
    except: b4st2const = -1

    try: b4st3const = int(input("Консты на третью ивент 4-ку в баннере (0-6); Пустое приравнивается к отсутствию: "))
    except: b4st3const = -1

    try: avlPlsInShop = int(input("Текущее количество доступных круток в магазине за пыль (0-5): "))
    except: avlPlsInShop = 0

    try: avlStardust = int(input("Текущее количество доступной звездной пыли: "))
    except: avlStardust = 0

    try: avlStarglitter = int(input("Текущее количество доступного звездного блеска: "))
    except: avlStarglitter = 0
    if wishnum < 1 or wishnum > 10000: wishnum = 0
    if p4st < 0 or p4st > 10: p4st = 0
    if p5st < 0 or p5st > 90: p5st = 0
    if st5const < -1 or st5const > 6: st5const = -1
    if b4st1const < -1 or b4st1const > 6: b4st1const = -1
    if b4st2const < -1 or b4st2const > 6: b4st2const = -1
    if b4st3const < -1 or b4st3const > 6: b4st3const = -1
    if avlPlsInShop < 0 or avlPlsInShop > 5: avlPlsInShop = 0
    if avlStardust < 0: avlStardust = 0
    if avlStarglitter < 0: avlStarglitter = 0
    return [wishnum, p4st, p5st, st5const, b4st1const, b4st2const, b4st3const, avlPlsInShop, avlStardust, avlStarglitter]
def finalreport(startwishnum, wishnum, p4st, p5st, st5const, b4st1const, b4st2const, b4st3const, pullsInShop, sumStardust, sumStarglitter):
    print("\n---------------------")
    print("Симуляция завершена!")
    print(f"Количество круток для симуляции: {startwishnum} + {wishnum - startwishnum}")
    print(f"Текущая 4-звёздное крутка: {p4st}")
    print(f"Текущая 5-звёздное крутка: {p5st}")
    if st5const == -1:
        print("Ивент лега не выпала")
    else:
        print(f"Консты на легу: {st5const}")

    if b4st1const == -1:
        print("Первая баннерная четверка не выпала")
    else:
        print(f"Консты на первую ивент 4-ку в баннере: {b4st1const}")

    if b4st2const == -1:
        print("Вторая баннерная четверка не выпала")
    else:
        print(f"Консты на вторую ивент 4-ку в баннере: {b4st2const}")

    if b4st3const == -1:
        print("Третья баннерная четверка не выпала")
    else:
        print(f"Консты на третью ивент 4-ку в баннере: {b4st3const}")
    print("---------------------")
    print(f"Общий блеск и пыль, полученные в процессе симуляции: {sumStarglitter}, {sumStardust}")
    print(f"Количество доступных круток в магазине за пыль: {pullsInShop}")
    print(f"Количество круток за блеск: {sumStarglitter // 20}")
    print(f"Количество круток за пыль: {wishnum - startwishnum - (sumStarglitter // 20)}")
    print("---------------------")
    if SELECTCERTAIN4STARS:
        print("Консты на четверки не из баннера:")
        names = [
            name for name in get4starNameList(getLang())
            if name not in SELECTEDCHARS
        ]
        with open(FOURSTARCONSTELLATIONS, "r") as f:
            constellations = [line.strip() for line in f]
        for number, (name, constellation) in enumerate(zip(names, constellations), start=1):
            print(f"{number}. {name} - {constellation}")
        print("---------------------")


def getLang(newlang=None):
    if newlang is not None:
        with open (LANGFILE, "w") as f:
            f.write(newlang)
        return newlang
    
    with open (LANGFILE, "r") as f:
        return f.read().strip()
    f.close()

def get4starNameList(lang):
    f = FOURSTARNAMEENFILE if lang == 'en' else FOURSTARNAMERUFILE
    with open (f, "r") as file:
        return [line.strip() for line in file]

def update4starConstellation(name):
    names = get4starNameList(getLang())
    if name not in names:
        raise ValueError(f"Unknown 4-star character: {name}")

    with open(FOURSTARCONSTELLATIONS, "r") as file:
        constellations = [int(line.strip()) for line in file]

    if len(constellations) != len(names):
        raise ValueError("4-star constellation data does not match the character list")

    index = names.index(name)
    previous = constellations[index]
    constellations[index] = min(previous + 1, 6)

    with open(FOURSTARCONSTELLATIONS, "w") as file:
        file.writelines(f"{constellation}\n" for constellation in constellations)

    return previous, constellations[index]

def defineCertain4stars(status):
    global SELECTCERTAIN4STARS
    SELECTCERTAIN4STARS = status