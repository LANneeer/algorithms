# Tuples
#
# 1
tpl = (100, 200, 300)
print(tuple([f"{i}" for i in tpl]))

# 2
tpls = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_tpls = []
for tpl in tpls:
    new_tpls.append((*tpl[:2], 100))
print(new_tpls)

# 3
multipliers = (4, 3, 2, 2, -1, 18)
j = 1
for i in multipliers:
    j *= i
print(j)

# 4
tpls = [(10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)]
avgs = []
for tpl in tpls:
    avg = 0
    for i in tpl:
        avg += i
    avg /= len(tpl)
    avgs.append(avg)
print(avgs)

# 5
tpls = (
    ("Red", "White", "Blue"),
    ("Green", "Pink", "Purple"),
    ("Orange", "Yellow", "Lime"),
)
string = "White"
print(f"Check if {string} present in tuple of tuples")
contains = False
for tpl in tpls:
    for s in tpl:
        if string == s:
            contains = True
            break
print(contains)

# Dicts
#
# 1
dct = {0: 10, 1: 20}
key = 2
val = 30
dct[key] = val

print(dct)

# 2
d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}

# 3
n = 5
dct = {}
for i in range(1, 5 + 1):
    dct[i] = i * i
print(dct)

# 4
dct = {1: 10, 2: 20, 3: 10, 4: 40}
tmp = {}
dupl = []
for i, v in dct.items():
    if v not in tmp.keys():
        tmp[v] = i
    else:
        dupl.append(i)
for dup in dupl:
    dct.pop(dup)
print(dct)

# 5
d3 = {}
for k, v in d1.items():
    if k in d3.keys():
        d3[k] += v
    else:
        d3[k] = v

for k, v in d2.items():
    if k in d3.keys():
        d3[k] += v
    else:
        d3[k] = v
print(d3)

# Sets
#
# 1
st = {1, 2, 4, -1, 9}

mmin = mmax = None
for i in st:
    if mmin is None:
        mmin = i
    elif i < mmin:
        mmin = i
    if mmax is None:
        mmax = i
    elif i > mmax:
        mmax = i
print("min:", mmin, "mmax:", mmax)

# 2
print(len(st))

# 3
v = 4
contains = False
for i in st:
    if v == i:
        contains = True
        break
print(contains)
