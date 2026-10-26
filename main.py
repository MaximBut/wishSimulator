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
    if st5const < 0 or st5const > 6: st5const = 0
    if b4st1const < 0 or b4st1const > 6: b4st1const = 0
    if b4st2const < 0 or b4st2const > 6: b4st2const = 0
    if b4st3const < 0 or b4st3const > 6: b4st3const = 0
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
    return [wishnum, p4st, p5st, st5const, b4st1const, b4st2const, b4st3const, avlPlsInShop, avlStardust, avlStarglitter]

config_values = config()
wishnum = config_values[0]
p4st = config_values[1]
p5st = config_values[2]
st5const = config_values[3]
b4st1const = config_values[4]
b4st2const = config_values[5]
b4st3const = config_values[6]
avlPlsInShop = config_values[7]
avlStardust = config_values[8]
avlStarglitter = config_values[9]
pullnumber = 1

while wishnum != 0:
    wishlist = funcs.formWishlist(p4st, p5st)
    try:
        result = wish.wish(wishlist[0])
        print(f"Результат крутки {pullnumber}: {result}")
        if result == "4star":
            p4st = 1
            p5st += 1
            fourstarbanner = wish.wish(wishlist[2])
            if fourstarbanner == "banner4st":
                fourstarbanner = wish.wish(wishlist[3])
                if fourstarbanner == "fstbanner4st":
                    print("Первый 4зв баннерный персонаж")
                    if b4st1const != -1:
                        if b4st1const < 6:
                            b4st1const += 1
                            avlStarglitter += 8
                            print(f"Консты на него: {b4st1const-1} -> {b4st1const}")
                        else:
                            print("Консты на него уже максимальные (6)")
                            avlStarglitter += 20
                    else:
                        print("Получено нового 1го 4зв баннерного персонажа")
                        b4st1const = 0
                elif fourstarbanner == "scdbanner4st":
                    if b4st2const != -1:
                        print("Второй 4зв баннерный персонаж")
                        if b4st2const < 6:
                            b4st2const += 1
                            avlStarglitter += 8
                            print(f"Консты на него: {b4st2const-1} -> {b4st2const}")
                        else:
                            print("Консты на него уже максимальные (6)")
                            avlStarglitter += 20
                    else:
                        print("Получено нового 2го 4зв баннерного персонажа")
                        b4st2const = 0
                    print("Второй 4зв баннерный персонаж")
                elif fourstarbanner == "trdbanner4st":
                    if b4st3const != -1:
                        print("Третий 4зв баннерный персонаж")
                        if b4st3const < 6:
                            b4st3const += 1
                            avlStarglitter += 8
                            print(f"Консты на него: {b4st3const-1} -> {b4st3const}")
                        else:
                            print("Консты на него уже максимальные (6)")
                            avlStarglitter += 20
                    else:
                        print("Получено нового 3го 4зв баннерного персонажа")
                        b4st3const = 0
                    print("Третий 4зв баннерный персонаж")

            elif fourstarbanner == "nonbanner4st":
                print("Небаннерный 4зв персонаж")
                avlStarglitter += 8
        elif result == "5star":
            p5st = 1
            p4st += 1
            fivestarbanner = wish.wish(wishlist[1])
            if fivestarbanner == "lost5050_5st":
                print("Вы проиграли 50/50 на 5зв персонажа")
                avlStarglitter += 20
            elif fivestarbanner == "won5050_5st":   
                print("Вы выиграли 50/50 на 5зв персонажа")
                if st5const != -1:
                    if st5const < 6:
                        st5const += 1
                        avlStarglitter += 100 # Поменять
                        print(f"Консты на него: {st5const-1} -> {st5const}")
                    else:
                        print("Консты на него уже максимальные (6)")
                        avlStarglitter += 100 # Поменять
                else:
                    print("Вы получили нового баннерного 5зв персонажа")
                    st5const = 0
        else:
            p4st += 1
            p5st += 1

        wishnum -= 1
        pullnumber += 1
        
    except Exception as e:
        print(f"wishlist: {wishlist[0]}")
        print(f"Ошибка при крутке {pullnumber}: {e}")

print("Зведный блеск:", avlStarglitter)