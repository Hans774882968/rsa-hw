from gmpy2 import invert, powmod, gcd
from libnum import n2s, s2n

p = 456457
q = 999217
n = p * q
e = 23
phi = (p - 1) * (q - 1)
d = invert(e, phi)
dp = d % (p - 1)
dq = d % (q - 1)
g_e_phi = gcd(e, phi)
assert g_e_phi == 1
print(f'RSA参数：p = {p}, q = {q}, n = {n}, phi = {phi}, e = {e}, d = {d}, dp = {dp}, dq = {dq}')

m_str = 'hans7'
m = s2n(m_str)
print(f'原始明文数字：{m}')
print('-' * 30)

c = powmod(m, e, n)
print(f'密文 c: {c}')

m_p = powmod(c, dp, p)
m_q = powmod(c, dq, q)
q_inv = invert(q, p)
print(f'm_p = {m_p}, m_q = {m_q}, q_inv = {q_inv}')
# 用 Garner 公式合并
h = (q_inv * (m_p - m_q)) % p
m_dec_crt = m_q + h * q
print(f'解密出的数字：{m_dec_crt}')
print(f'还原的字符串：{n2s(int(m_dec_crt)).decode("utf-8")}')
