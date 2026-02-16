# %%
print("Cartesian Product And Cardanility")

# %%
A = {2,3}
B = {1,4}

cartesian_prod = [(a,b) for a in A for b in B]
cardanility = len(cartesian_prod)

print("Set A = ", A)
print("Set B = ", B)
print("Cartesian Product (A * B) = ", cartesian_prod)
print("Cardanility = ", cardanility)
