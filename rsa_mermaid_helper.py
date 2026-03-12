from gmpy2 import invert, powmod, gcd
from libnum import n2s, s2n

p = 456457
q = 999217
n = p * q
e = 23
phi = (p - 1) * (q - 1)
d = invert(e, phi)
g_e_phi = gcd(e, phi)
assert g_e_phi == 1
print(f'RSA参数：p = {p}, q = {q}, n = {n}, phi = {phi}, e = {e}, d = {d}')

m_str = 'hans7'
m = s2n(m_str)
print(f'原始明文数字：{m}')
print('-' * 30)

c = powmod(m, e, n)
print(f'密文 c: {c}')

m_dec_standard = powmod(c, d, n)
print(f'解密出的数字：{m_dec_standard}')
print(f'还原的字符串：{n2s(int(m_dec_standard)).decode("utf-8")}')
