# %%
print("Hello, World!")


# %%
print("Truth Table:- OR")
print("p\t  q\t p\u2228q")
print("----------------------")

for p in [True, False]:
    for q in [True, False]:

        print(p, "\t", q, "\t", p or q)

# %%
print("Truth Table :- NOT")
print("p\t  q\t  \u00acp\t  \u00acq")
print("------------------------------")

for p in [True, False]:
    for q in [True, False]:
        print(p,"\t", q, "\t", not p, "\t", not q)
# %%
print("Truth Table :- AND")
print("p\t q\t  p\u2227q")
print("----------------------")

for p in [True, False]:
    for q in [True, False]:
        print(p,"\t", q, "\t", p and q)

# %%
print("Truth Table :- Implication/If-else")
print("p\t q\t p\u2192q")
print("-----------------------")

for p in [True, False]:
    for q in [True, False]:
        print(p,"\t", q, "\t", not p or q)
# %%
print("Truth Table :- Biconditonal/if and only if")
print("p\t q\t p\u2194q")
print("----------------------")

for p in [True, False]:
    for q in [True, False]:
        print(p,"\t", q,"\t", (not p or q) and (not q or p))
# %%

print("Truth Table :- For 0 and 1 (Biconditional)")
print("p\t q\t p\u2194q")
print("---------------------")

for p in [1, 0]:
    for q in [1, 0]:
        print(p,"\t", q, "\t", int((not p or q) and (not q or p)))

# %%
