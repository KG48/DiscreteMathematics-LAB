# %%
print("Logical Equivalence")


# %%
print("Truth Table :- DeMorgans Law")
print("p\t q\t p\u2228q\t \u00ac(p\u2228q)\t \u00acp\u2227\u00acq")
print("------------------------------------------")

equivalent = True

for p in [True, False]:
    for q in [True, False]:
        column_3 = p or q
        column_4 = not(p or q)
        column_5 = not p and (not q)

        print(p, "\t", q, "\t", column_3, "\t", column_4, "\t", column_5)

        if column_4 != column_5:
            equivalent =  False
if equivalent:
    print("yes, both operations are equivalent")
else:
    print("no, both operations are not equivalent")


# %%
print("p\tq\t¬p\t¬q\t¬(p∧q)\t¬p∨¬q")
print("-----------------------------------------------")

equivalent = True

for p in [True, False]:
    for q in [True, False]:
        not_p = not p
        not_q = not q
        left = not (p and q)
        right = not p or not q

        print(p, "\t", q, "\t", not_p, "\t", not_q, "\t", left, "\t", right)

        if left != right:
            equivalent = False

if equivalent:
    print("Yes, both operations are equivalent.")
else:
    print("No, both operations are not equivalent.")

# %%

print("p\t q\t p\u2227q\t \u00acp\u2227\u00acq\t p\u2194q\t (\u00acp\u2228q)\u2227(\u00acp\u2228q)")
print("------------------------------------------------------")

equivalent = True

for p in [True, False]:
    for q in [True, False]:
        column_3 = p and q
        column_4 = (not p) and (not q)
        column_5 = (not p or q) and (not p or q)
        column_6 = (not p or q) and (not p or q)

        print(p, "\t", q, "\t", column_3, "\t", column_4, "\t", column_5, "\t", column_6)

        if column_5 != column_6:
            equivalent = False

if equivalent:
    print("Yes, both operations are equivalent.")
else:
    print("No, both operations are not equivalent.")

# %%
