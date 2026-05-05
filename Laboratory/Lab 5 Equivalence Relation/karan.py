# %%
# Check Reflexive

S = {1, 2, 3}
R = {(1,1), (2,2), (3,3), (1,2), (2,1)}

reflexive = True
for x in S:
    if (x, x) not in R:
        reflexive = False

if reflexive:
    print("reflexive")
else:
    print("not reflexive")


# Check Symmetric

S = {1, 2, 3}
R = {(1,1), (2,2), (3,3), (1,2), (2,1)}

symmetric = True
for (a, b) in R:
    if (b, a) not in R:
        symmetric = False

if symmetric:
    print("symmetric")
else:
    print("not symmetric")


# Check Transitive

S = {1, 2, 3}
R = {(1,1), (2,2), (3,3), (1,2), (2,1)}

transitive = True
for (a, b) in R:
    for (c, d) in R:
        if b == c and (a, d) not in R:
            transitive = False

if transitive:
    print("transitive")
else:
    print("not transitive")


# Check Equivalence Relation

S = {1, 2, 3}
R = {(1,1), (2,2), (3,3), (1,2), (2,1)}

equivalence = True

for x in S:
    if (x, x) not in R:
        equivalence = False

for (a, b) in R:
    if (b, a) not in R:
        equivalence = False

for (a, b) in R:
    for (c, d) in R:
        if b == c and (a, d) not in R:
            equivalence = False

if equivalence:
    print("equivalence")
else:
    print("not equivalence")