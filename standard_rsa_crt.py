from gmpy2 import invert, powmod
from libnum import n2s, s2n

p = 9648423029010515676590551740010426534945737639235739800643989352039852507298491399561035009163427050370107570733633350911691280297777160200625281665378483
q = 11874843837980297032092405848653656852760910154543380907650040190704283358909208578251063047732443992230647903887510065547947313543299303261986053486569407
e = 65537
m_str = 'hans114514'

m = s2n(m_str)
print(f'原始明文数字：{m}')
print('-' * 30)

n = p * q
phi = (p - 1) * (q - 1)
d = invert(e, phi)
c = powmod(m, e, n)
print(f'密文 c: {c}')

dp = d % (p - 1)
dq = d % (q - 1)
m_p = powmod(c, dp, p)
m_q = powmod(c, dq, q)
q_inv = invert(q, p)
# 用 Garner 公式合并
h = (q_inv * (m_p - m_q)) % p
m_dec_crt = m_q + h * q

print(f'解密出的数字：{m_dec_crt}')
print(f'还原的字符串：{n2s(int(m_dec_crt)).decode("utf-8")}')
