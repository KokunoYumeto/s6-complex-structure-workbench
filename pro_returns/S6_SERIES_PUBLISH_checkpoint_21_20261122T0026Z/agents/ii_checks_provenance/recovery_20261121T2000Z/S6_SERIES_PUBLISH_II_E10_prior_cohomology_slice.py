# C is the genus-two double cover of P1 and L=pi^*O(1)=K_C.
# For a positive integer a, H0(L^-a)=0 and h1(L^-a)=2a+1.
def h1_negative(a):
    assert a > 0
    return 2*a+1
structure = (1, 2, 2*h1_negative(1), h1_negative(2))
obstruction = (0, h1_negative(1), 2*h1_negative(2), h1_negative(3))
vertical = (0, 2*h1_negative(1), 4*h1_negative(2), 2*h1_negative(3))
assert structure == (1,2,6,5)
assert obstruction == (0,3,10,7)
assert vertical == (0,6,20,14)
print('E10 h(O_Y), h(g^*T_C), h(T_Y/C):', structure, obstruction, vertical)

