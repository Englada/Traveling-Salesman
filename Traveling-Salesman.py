import random
import copy

distances = [
    (102, 10),
    (103, 15),
    (104, 20),
    (201, 10),
    (203, 35),
    (204, 25),
    (301, 15),
    (302, 35),
    (304, 30),
    (401, 20),
    (402, 25),
    (403, 30)
]


def distance(p1, p2):
    places = p1 * 100 + p2
    for i in distances:
        if i[0] == places:
            return i[1]

arr = [1, 2, 3, 4]


def shortest(array):
    ans = []
    anss = []
    arrr = copy.deepcopy(array)
    while len(arrr) > 0:
        x = random.choice(arrr)
        ans.append(x)
        arrr.remove(x)
    ans.append(ans[0])
    for i in range(len(ans) - 1):
        y = distance(ans[i], ans[i + 1])
        anss.append(y)
    ans.append(anss)
    ans.append(sum(anss))

    return ans


def fin():
    final = [0]
    counter = 0
    new = []
    x = shortest(arr)
    while counter < 24:
        if x in final:
            new.append("true")
            # print new
            x = shortest(arr)
            if len(final) > 23 and len(new) > 100:
                break
        else:
            # print False
            final.append(x)
            # print final
            x = shortest(arr)
            counter += 1
    # final.remove(0)
    return final


def last():
    x = fin()
    x.pop(0)
    array = []
    for i in x:
        if i[6] == 80:
            array.append(i)
    return array


shortest(arr)
# print fin()
print last()
