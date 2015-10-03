cornerA = max(E, A)
cornerB = max(F, B)
cornerC = min(G, C)
cornerD = min(H, D)

a = (D-B)*(C-A)
b = (H-F)*(G-E)
i = max(cornerD-cornerB, 0)*max(cornerC-cornerA, 0)
if not a or not b:
    return a+b
else:
    return a+b-i
