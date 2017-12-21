def onehot(tile):
    """
    牌のクラスをワンホットベクトルで返す
    @param tile:牌の種類
    return:
    34クラスのonehot
        |- m*:マンズの*[0:8]
        |- p*:筒子の*[9:17]
        |_- s*:ソウズの*[18:26]
        |- (e,s,w,n):(東、南、西、北)[27:30]
        |- haku:白[31]
        |- hatsu:發[32]
        |- chun:中[33]
    """
    if tile == "m1":
        return [0 if _ != 0 else 1 for _ in range(34)]
    elif tile == "m2":
        return [0 if _ != 1 else 1 for _ in range(34)]
    elif tile == "m3":
        return [0 if _ != 2 else 1 for _ in range(34)]
    elif tile == "m4":
        return [0 if _ != 3 else 1 for _ in range(34)]
    elif tile == "m5":
        return [0 if _ != 4 else 1 for _ in range(34)]
    elif tile == "m5d":
        return [0 if _ != 4 else 1 for _ in range(34)]
    elif tile == "m6":
        return [0 if _ != 5 else 1 for _ in range(34)]
    elif tile == "m7":
        return [0 if _ != 6 else 1 for _ in range(34)]
    elif tile == "m8":
        return [0 if _ != 7 else 1 for _ in range(34)]
    elif tile == "m9":
        return [0 if _ != 8 else 1 for _ in range(34)]
    elif tile == "p1":
        return [0 if _ != 9 else 1 for _ in range(34)]
    elif tile == "p2":
        return [0 if _ != 10 else 1 for _ in range(34)]
    elif tile == "p3":
        return [0 if _ != 11 else 1 for _ in range(34)]
    elif tile == "p4":
        return [0 if _ != 12 else 1 for _ in range(34)]
    elif tile == "p5":
        return [0 if _ != 13 else 1 for _ in range(34)]
    elif tile == "p5d":
        return [0 if _ != 13 else 1 for _ in range(34)]
    elif tile == "p6":
        return [0 if _ != 14 else 1 for _ in range(34)]
    elif tile == "p7":
        return [0 if _ != 15 else 1 for _ in range(34)]
    elif tile == "p8":
        return [0 if _ != 16 else 1 for _ in range(34)]
    elif tile == "p9":
        return [0 if _ != 17 else 1 for _ in range(34)]
    elif tile == "s1":
        return [0 if _ != 18 else 1 for _ in range(34)]
    elif tile == "s2":
        return [0 if _ != 19 else 1 for _ in range(34)]
    elif tile == "s3":
        return [0 if _ != 20 else 1 for _ in range(34)]
    elif tile == "s4":
        return [0 if _ != 21 else 1 for _ in range(34)]
    elif tile == "s5":
        return [0 if _ != 22 else 1 for _ in range(34)]
    elif tile == "s5d":
        return [0 if _ != 22 else 1 for _ in range(34)]
    elif tile == "s6":
        return [0 if _ != 23 else 1 for _ in range(34)]
    elif tile == "s7":
        return [0 if _ != 24 else 1 for _ in range(34)]
    elif tile == "s8":
        return [0 if _ != 25 else 1 for _ in range(34)]
    elif tile == "s9":
        return [0 if _ != 26 else 1 for _ in range(34)]
    elif tile == "e":
        return [0 if _ != 27 else 1 for _ in range(34)]
    elif tile == "s":
        return [0 if _ != 28 else 1 for _ in range(34)]
    elif tile == "w":
        return [0 if _ != 29 else 1 for _ in range(34)]
    elif tile == "n":
        return [0 if _ != 30 else 1 for _ in range(34)]
    elif tile == "haku":
        return [0 if _ != 31 else 1 for _ in range(34)]
    elif tile == "hatsu":
        return [0 if _ != 32 else 1 for _ in range(34)]
    elif tile == "chun":
        return [0 if _ != 33 else 1 for _ in range(34)]
    print(tile)
