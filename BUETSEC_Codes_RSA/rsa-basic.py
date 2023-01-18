#   Pico GYM Problem
#   Mind your Ps and Qs
# pycryptodome
from Cryptodome.Util.number import inverse

p = 1899107986527483535344517113948531328331
q = 674357869540600933870145899564746495319033


# public key, n
N = 1280678415822214057864524798453297819181910621573945477544758171055968245116423923
# public key, e
E = 65537
# ciphertext
C = 62324783949134119159408816513334912534343517300880137691662780895409992760262021

phi = (p-1)*(q-1)
d = inverse(E, phi)

# m = plaintext
m = pow(C, d, N)
print(m)


hex_val = hex(m)[2:]
print(hex_val)

# print(hex_val)
ascii_val = bytes.fromhex(hex_val).decode("utf-8")
print(ascii_val)
