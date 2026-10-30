import funcs
import wish
st5chances = funcs.get5StarChances()
st4chances = funcs.get4StarChances()

if __name__ == "__main__":
    print("Симулятор круток")
    print("---------------------")
    source = int(input("Выберите источник конфигурации (1 - файл, 2 - ввод вручную): "))
    if source == 1:
        fname = input("Введите путь к файлу конфигурации: ")
        fconfig_values = funcs.file_config(fname)
        wishnum = fconfig_values[0]
        p4st = fconfig_values[1]
        p5st = fconfig_values[2]
        st5const = fconfig_values[3]
        b4st1const = fconfig_values[4]
        b4st2const = fconfig_values[5]
        b4st3const = fconfig_values[6]
        avlPlsInShop = fconfig_values[7]
        avlStardust = fconfig_values[8]
        avlStarglitter = fconfig_values[9]
    else:
        config_values = funcs.config()
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
    startwishnum = wishnum
    sumStarglitter = avlStarglitter
    sumStardust = avlStardust
    pullsInShop = avlPlsInShop
    star4guarantee = False
    star5guarantee = False

    while wishnum > 0 and pullnumber != wishnum + 1:
        wishlist = funcs.formWishlist(p4st, p5st, star4guarantee, star5guarantee)
        try:
            result = wish.wish(wishlist[0])
            if result == "3star":
                print(f"Крутка {pullnumber}: 3зв персонаж")
                avlStardust += 20
                sumStardust += 20
            
            if result == "4star":
                p4st = 1
                p5st += 1
                fourstarbanner = wish.wish(wishlist[2])
                if fourstarbanner == "banner4st":
                    star4guarantee = False
                    fourstarbanner = wish.wish(wishlist[3])
                    if fourstarbanner == "fstbanner4st":
                        print(f"Крутка {pullnumber}: Первый 4зв баннерный персонаж")
                        if b4st1const != -1:
                            if b4st1const < 6:
                                b4st1const += 1
                                avlStarglitter += 8
                                sumStarglitter += 8
                                print(f"Консты на него: {b4st1const-1} -> {b4st1const}")
                            else:
                                print("Консты на него уже максимальные (6)")
                                avlStarglitter += 20
                                sumStarglitter += 20
                        else:
                            print(f"Крутка {pullnumber}: Получено нового 1го 4зв баннерного персонажа")
                            b4st1const = 0
                    elif fourstarbanner == "scdbanner4st":
                        if b4st2const != -1:
                            print(f"Крутка {pullnumber}: Второй 4зв баннерный персонаж")
                            if b4st2const < 6:
                                b4st2const += 1
                                avlStarglitter += 8
                                sumStarglitter += 8
                                print(f"Консты на него: {b4st2const-1} -> {b4st2const}")
                            else:
                                print("Консты на него уже максимальные (6)")
                                avlStarglitter += 20
                                sumStarglitter += 20
                        else:
                            print(f"Крутка {pullnumber}: Получено нового 2го 4зв баннерного персонажа")
                            b4st2const = 0
                    elif fourstarbanner == "trdbanner4st":
                        if b4st3const != -1:
                            print(f"Крутка {pullnumber}: Третий 4зв баннерный персонаж")
                            if b4st3const < 6:
                                b4st3const += 1
                                avlStarglitter += 8
                                sumStarglitter += 8
                                print(f"Консты на него: {b4st3const-1} -> {b4st3const}")
                            else:
                                print("Консты на него уже максимальные (6)")
                                avlStarglitter += 20
                                sumStarglitter += 20
                        else:
                            print(f"Крутка {pullnumber}: Получено нового 3го 4зв баннерного персонажа")
                            b4st3const = 0

                elif fourstarbanner == "nonbanner4st":
                    print(f"Крутка {pullnumber}: Небаннерный 4зв персонаж")
                    star4guarantee = True
                    avlStarglitter += 8
                    sumStarglitter += 8
            elif result == "5star":
                p5st = 1
                p4st += 1
                fivestarbanner = wish.wish(wishlist[1])
                if fivestarbanner == "lost5050_5st":
                    print(f"Крутка {pullnumber}: Вы проиграли 50/50 на 5зв персонажа")
                    avlStarglitter += 20
                    sumStarglitter += 20
                    star5guarantee = True
                elif fivestarbanner == "won5050_5st":
                    if star5guarantee:
                        print(f"Крутка {pullnumber}: 5зв персонаж по гаранту")
                    else:
                        print(f"Крутка {pullnumber}: Вы выиграли 50/50 на 5зв персонажа")
                    star5guarantee = False
                    if st5const != -1:
                        if st5const < 6:
                            st5const += 1
                            avlStarglitter += 40
                            sumStarglitter += 100
                            print(f"Консты на него: {st5const-1} -> {st5const}")
                        else:
                            print("Консты на него уже максимальные (6)")
                            avlStarglitter += 100
                            sumStarglitter += 100
                    else:
                        print(f"Крутка {pullnumber}: Вы получили нового баннерного 5зв персонажа")
                        st5const = 0
            else:
                p4st += 1
                p5st += 1

            pullnumber += 1

            if pullnumber == wishnum:
                wishes_from_starglitter = avlStarglitter // 20
                avlStarglitter %= 20
                wishes_from_shop = min(avlPlsInShop, avlStardust // 90)
                avlStardust -= wishes_from_shop * 90
                avlPlsInShop -= wishes_from_shop
                wishnum += wishes_from_starglitter + wishes_from_shop

        except Exception as e:
            print(f"wishlist: {wishlist[0]}")
            print(f"Ошибка при крутке {pullnumber}: {e}")
            break

    funcs.finalreport(startwishnum, wishnum, p4st, p5st, st5const, b4st1const, b4st2const, b4st3const, avlPlsInShop, avlStardust, avlStarglitter)