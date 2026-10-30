from decimal import Decimal

FIVESTARFILE = "5stChances.txt";
FOURSTARFILE = "4stChances.txt";
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
