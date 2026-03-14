from gmpy2 import invert, powmod
from libnum import n2s, s2n

e = 65537
# 0xC0332C5C64AE47182F6C1C876D42336910545A58F7EEFEFC0BCAAF5AF341CCDD 十进制是77位
n = 86934482296048119190666062003494800588905656017203025617216654058378322103517
# factordb 分解得 p 和 q 都是39位
p = 285960468890451637935629440372639283459
q = 304008741604601924494328155975272418463
phi = (p - 1) * (q - 1)
d = invert(e, phi)
# 我这里是在项目根目录执行的
with open('buu_rsa_请少侠自己摸索/flag.enc', 'rb') as f:
    data = f.read()
    c = s2n(data)
m = powmod(c, d, n)
print(n2s(int(m)))  # b'\x02\x9d {zR\x1e\x08\xe4\xe6\x18\x06\x00flag{decrypt_256}\n'
# 因为开头有坏数据所以没法 decode 。而 rsa 这个包能帮我们自动去掉坏数据
