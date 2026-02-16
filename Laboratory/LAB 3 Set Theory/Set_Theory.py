# %%
print("Set Theory")

# %%
print("1. Union")

A = {2,4,8,9,1,3,0}
B = {4,3,8}

print("A \u222A B = ", A | B)

# %%
print("2. Intersection")

A = {2,4,8,9,1,3,0}
B = {4,3,8}

print("A \u2229 B = ", A & B)

# %%
print("3. Difference")

A = {2,4,8,9,1,3,0}
B = {4,3,8}

print("A - B", A - B)
print("B - A", B - A)

# %%
print("4. Subset")
 
A = {2,4,8,9,1,3,0}
B = {4,3,8}

if A.issubset(B):
    print("Yes, A is Subset of B, A \u2286 B")
else :
    print("No, A is not subset of B.")

if B.issubset(A):
    print("Yes, B is subset of A, B \u2286 A")
else :
    print("No, B is not subset of A.")