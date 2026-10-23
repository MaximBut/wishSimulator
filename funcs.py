FIVESTARFILE = "5stChances.txt";
FOURSTARFILE = "4stChances.txt";
fisc = []
fosc = []

def get5StarChances():
    with open(FIVESTARFILE, "r") as f:
        chances = f.read().strip()
    return chances

def get4StarChances():
    with open(FOURSTARFILE, "r") as f:
        chances = f.read().strip()
    return chances

def formWishlist(wishnum, fostpity, fistpity):
    s5 = get5StarChances()
    s4 = get4StarChances()
    reslist = []
    if fostpity == 10:
        fostpity = 0
        reslist.append([
            "3star", 0,
            "4star", 100,
            "5star", 0
        ])
    elif fistpity == 90:
        fistpity = 0
        reslist.append([
            "3star", 0,
            "4star", 100,
            "5star", 0
        ])
    else:
        reslist.append([
            "3star", 100 - float(s4) - float(s5),
            "4star", float(s4),
            "5star", float(s5)
        ])

    reslist.append([
        "lost5050_5st", 50,
        "won5050_5st", 50
    ])

    reslist.append([
        "banner4st", 50,
        "nonbanner4st", 50
    ])
    return reslist