from decimal import Decimal
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

DATA_DIR = Path(__file__).resolve().parent / "data"
FIVESTARFILE = DATA_DIR / "5stChances.txt"
FOURSTARFILE = DATA_DIR / "4stChances.txt"
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
def file_config(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        wishnum = int(lines[0].strip())
        p4st = int(lines[1].strip())
        p5st = int(lines[2].strip())
        st5const = int(lines[3].strip())
        b4st1const = int(lines[4].strip())
        b4st2const = int(lines[5].strip())
        b4st3const = int(lines[6].strip())
        avlPlsInShop = int(lines[7].strip())
        avlStardust = int(lines[8].strip())
        avlStarglitter = int(lines[9].strip())

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
    print(f"Количество круток за пыль: {pullsInShop} + {min(pullsInShop, sumStardust // 90)}")
    print("---------------------")