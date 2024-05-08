def bingo_check(card:list) -> bool:
    res_r = [0 for i in range(5)]
    res_c = [0 for i in range(5)]
    for i,r in enumerate(card):
        for j,c in enumerate(r):
            if c == "x":
                res_r[i] += 1
                res_c[j] += 1
    res = True
    for i in res_r:
        if i == 5:
            return True
        elif i == 0:
            res = False
    #return False right away if res is False since if there is bingo either in
    #columes or diagonals there must be at least one x in each row
    if res:
        for i in res_c:
            if i == 5:
                return True
            elif i == 0:
                res = False
    else:
        return res
    return res

print(bingo_check([
  [45, "x", 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, 39, 44],
  [21, "x", 24, 30, 52]
]))
#True

print(bingo_check([
  ["x", 43, 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, 65, "x", 83, 54],
  [67, 98, 39, "x", 44],
  [21, 59, 24, 30, "x"]
]))
#True

print(bingo_check([
  ["x", "x", "x", "x", "x"],
  [64, 12, 47, 32, 90],
  [37, 16, 68, 83, 54],
  [67, 19, 98, 39, 44],
  [21, 75, 24, 30, 52]
]))
#True

print(bingo_check([
  [45, "x", 31, 74, 87],
  [64, 78, 47, "x", 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, "x", 44],
  [21, "x", 24, 30, 52]
]))
#False