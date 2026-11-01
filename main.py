import funcs
import wish
st5chances = funcs.get5StarChances()
st4chances = funcs.get4StarChances()

def selected_4star_name(index):
    if index < len(funcs.SELECTEDCHARS):
        return funcs.SELECTEDCHARS[index]
    return funcs.text(
        f"{index + 1}-й баннерный 4-звёздный персонаж",
        f"{index + 1}st event 4-star character",
    )

if __name__ == "__main__":
    print(funcs.text("Симулятор круток", "Wish simulator"))
    print("---------------------")
    if funcs.getLang() != "en" and funcs.getLang() != "ru":
        lang = input("Enter language for character names (en/ru): ")
        lang = funcs.getLang(lang)
    
    if (input(funcs.text("Определять ли определенных 4-звёздных персонажей? (1 - да, 0 - нет): ", "Select specific 4-star characters? (1 - yes, 0 - no): ")) == "1"):
        funcs.SELECTCERTAIN4STARS = True

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
                print(funcs.text(f"Крутка {pullnumber}: 3зв", f"Pull {pullnumber}: 3-star"))
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
                        character_name = selected_4star_name(0)
                        print(funcs.text(f"Крутка {pullnumber}: {character_name}", f"Pull {pullnumber}: {character_name}"))
                        if b4st1const != -1:
                            if b4st1const < 6:
                                b4st1const += 1
                                avlStarglitter += 8
                                sumStarglitter += 8
                                print(funcs.text(f"Консты на {character_name}: {b4st1const-1} -> {b4st1const}", f"{character_name} constellations: {b4st1const-1} -> {b4st1const}"))
                            else:
                                print(funcs.text(f"Консты на {character_name} уже максимальные (6)", f"{character_name} is already at maximum constellations (6)"))
                                avlStarglitter += 20
                                sumStarglitter += 20
                        else:
                            print(funcs.text(f"Крутка {pullnumber}: Получен новый персонаж {character_name}", f"Pull {pullnumber}: New character obtained: {character_name}"))
                            b4st1const = 0
                    elif fourstarbanner == "scdbanner4st":
                        character_name = selected_4star_name(1)
                        if b4st2const != -1:
                            print(funcs.text(f"Крутка {pullnumber}: {character_name}", f"Pull {pullnumber}: {character_name}"))
                            if b4st2const < 6:
                                b4st2const += 1
                                avlStarglitter += 8
                                sumStarglitter += 8
                                print(funcs.text(f"Консты на {character_name}: {b4st2const-1} -> {b4st2const}", f"{character_name} constellations: {b4st2const-1} -> {b4st2const}"))
                            else:
                                print(funcs.text(f"Консты на {character_name} уже максимальные (6)", f"{character_name} is already at maximum constellations (6)"))
                                avlStarglitter += 20
                                sumStarglitter += 20
                        else:
                            print(funcs.text(f"Крутка {pullnumber}: Получен новый персонаж {character_name}", f"Pull {pullnumber}: New character obtained: {character_name}"))
                            b4st2const = 0
                    elif fourstarbanner == "trdbanner4st":
                        character_name = selected_4star_name(2)
                        if b4st3const != -1:
                            print(funcs.text(f"Крутка {pullnumber}: {character_name}", f"Pull {pullnumber}: {character_name}"))
                            if b4st3const < 6:
                                b4st3const += 1
                                avlStarglitter += 8
                                sumStarglitter += 8
                                print(funcs.text(f"Консты на {character_name}: {b4st3const-1} -> {b4st3const}", f"{character_name} constellations: {b4st3const-1} -> {b4st3const}"))
                            else:
                                print(funcs.text(f"Консты на {character_name} уже максимальные (6)", f"{character_name} is already at maximum constellations (6)"))
                                avlStarglitter += 20
                                sumStarglitter += 20
                        else:
                            print(funcs.text(f"Крутка {pullnumber}: Получен новый персонаж {character_name}", f"Pull {pullnumber}: New character obtained: {character_name}"))
                            b4st3const = 0

                elif fourstarbanner == "nonbanner4st":
                    character_name = wish.wish(wishlist[4:])
                    previous_constellation, current_constellation = funcs.update4starConstellation(character_name)
                    print(funcs.text(f"Крутка {pullnumber}: {character_name}", f"Pull {pullnumber}: {character_name}"))
                    if current_constellation > previous_constellation:
                        print(funcs.text(f"Консты на {character_name}: {previous_constellation} -> {current_constellation}", f"{character_name} constellations: {previous_constellation} -> {current_constellation}"))
                    else:
                        print(funcs.text(f"Консты на {character_name} уже максимальные (6)", f"{character_name} is already at maximum constellations (6)"))
                    star4guarantee = True
                    avlStarglitter += 8
                    sumStarglitter += 8
            elif result == "5star":
                p5st = 1
                p4st += 1
                fivestarbanner = wish.wish(wishlist[1])
                if fivestarbanner == "lost5050_5st":
                    print(funcs.text(f"Крутка {pullnumber}: Вы проиграли 50/50 на 5зв персонажа", f"Pull {pullnumber}: Lost the 50/50 for the 5-star character"))
                    avlStarglitter += 20
                    sumStarglitter += 20
                    star5guarantee = True
                elif fivestarbanner == "won5050_5st":
                    if star5guarantee:
                        print(funcs.text(f"Крутка {pullnumber}: 5зв персонаж по гаранту", f"Pull {pullnumber}: Guaranteed 5-star character"))
                    else:
                        print(funcs.text(f"Крутка {pullnumber}: Вы выиграли 50/50 на 5зв персонажа", f"Pull {pullnumber}: Won the 50/50 for the 5-star character"))
                    star5guarantee = False
                    if st5const != -1:
                        if st5const < 6:
                            st5const += 1
                            avlStarglitter += 40
                            sumStarglitter += 100
                            print(funcs.text(f"Консты на него: {st5const-1} -> {st5const}", f"Character constellations: {st5const-1} -> {st5const}"))
                        else:
                            print(funcs.text("Консты на него уже максимальные (6)", "Character is already at maximum constellations (6)"))
                            avlStarglitter += 100
                            sumStarglitter += 100
                    else:
                        print(funcs.text(f"Крутка {pullnumber}: Вы получили нового баннерного 5зв персонажа", f"Pull {pullnumber}: New event 5-star character obtained"))
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
            print(funcs.text(f"wishlist: {wishlist[0]}", f"Wishlist: {wishlist[0]}"))
            print(funcs.text(f"Ошибка при крутке {pullnumber}: {e}", f"Error on pull {pullnumber}: {e}"))
            break

    funcs.finalreport(startwishnum, wishnum, p4st, p5st, st5const, b4st1const, b4st2const, b4st3const, avlPlsInShop, sumStardust, sumStarglitter)