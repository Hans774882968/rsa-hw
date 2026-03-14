[TOC]

## buuctf、青岑CTF等平台的RSA题

主要关注点：吸收里面的数论知识

- RSAROLL：RSA模板题，但滚动拼接flag
- rsarsa：RSA模板题
- 初识RSA（可在青岑CTF提交）：RSA模板题，附加对欧拉函数的简单理解
- RSA1：RSA的中国剩余定理解密加速优化模板题
- RSA3：RSA的共模攻击模板题

其他代码：

- standard_rsa.py：标准RSA解密代码
- standard_rsa_crt.py：RSA的中国剩余定理解密加速优化模板代码。这两个文件是用来做对比的
- rsa_mermaid_helper.py：画mermaid流程图需要准备一组比较小的案例数据
- rsa_garner_mermaid_helper.py：画d_p、d_q加速RSA解密的mermaid流程图的辅助代码
- buu_rsa1_crt.py：buu RSA1这题直接用**中国剩余定理**也能做

## 青岑CTF《初识RSA》（题源：NewStar2025-Week1）

搜到WriteUp： https://piyuanzhoulv.github.io/2025/11/05/NewStar2025-WP-PDF/%E5%9C%86%E5%91%A8%E7%8E%87WP-Week1.pdf

题目给了`[Cry]初识rsa.py`：

```python
from Crypto.Util.number import *
import hashlib

key = b'??????'
assert len(key) == 6
KEY = hashlib.md5(key).hexdigest().encode()
print('KEY=', KEY)

flag = b'flag{?????????????}'

m = bytes_to_long(flag)

e = 65537
p = getPrime(512)
q = getPrime(512)
n = pow(p, 3) * pow(q, 2)
c = pow(m, e, n)

P = p ^ (bytes_to_long(key))

print("P=", P)
print("n=", n)
print("c=", c)

'''
注释还给了KEY、P、n、c的值
'''
```

首先我们看能无脑解出来的变量：根据提示“MD5 码怎么解呢？好像有在线工具”，找到这个网站 https://www.cmd5.com/default.aspx 。输入md5密文`5ae9b7f211e23aac3df5f2b8f3b8eada`，查到是`crypto`。大P是小p异或`bytes_to_long(key)`，所以小p就是大P异或`bytes_to_long(key)`。

接下来我们根据`[Cry]初识rsa.py`里的RSA加密过程来推出解密过程：

1. n和p已知，所以可以直接用gmpy2求出q：`q, _ = iroot(n // p // p // p, 2)`
2. p和q是素数，`e = 65537, n = p ** 3 * q ** 2, c = pow(m, e, n)`。由欧拉定理，明文就是`m = pow(c, d, n)`。其中d为e在模 $\phi(n)$ 意义下的逆元，用gmpy2来求：`d = invert(e, phi)`
3. 根据欧拉函数的表达式得 $\phi(n) = p ^ 2 * (p - 1) * q * (q - 1)$

另一版题解（copy from https://github.com/Hans774882968/slidev-math-videos/blob/main/video-blogs/%E3%80%90slidev%E3%80%91%E7%AA%81%E7%84%B6%E5%8F%91%E7%8E%B0%E5%AD%A6RSA%E6%98%AF%E5%85%A5%E9%97%A8%E6%95%B0%E8%AE%BA%E7%9A%84%E5%A5%BD%E5%8A%9E%E6%B3%95.md ）：

读代码：

1. 给了`key`变量的md5值`KEY`，需要据此求出`key`
2. 给了`P, n, c`。如果求出`key`，就能用`P, key`求出`p`
3. 代码展示了RSA加密过程，目标是解出明文

解题过程：

1. 根据提示“MD5 码怎么解呢？好像有在线工具”，找一个[在线网站](https://www.cmd5.com/default.aspx)就能得到`key`
2. `P = p ^ (bytes_to_long(key))`（异或符号），所以`p = P ^ (bytes_to_long(key))`
3. n和p已知，所以可以直接用gmpy2的`iroot`（开n次方根）求出q：`q, _ = iroot(n // p // p // p, 2)`
4. p和q是素数， $e = 65537,\ n = p^3 * q^2,\ c = m^e\ mod\ n$ 。由欧拉定理，明文就是 $m = c^d\ mod\ n$ 。其中d为e在模 $\phi(n)$ 意义下的逆元，用gmpy2来求：`d = invert(e, phi)`
5. 根据欧拉函数的表达式得 $\phi(n) = p ^ 2 * (p - 1) * q * (q - 1)$

## buu rsa 请少侠自己摸索

ras是一个非常神秘的算法，那么它神秘在哪里 请少侠自己摸索！ 注意：得到的 flag 请包上 flag{} 提交

- 法1：用到名为`rsa`的包。`buu_rsa_请少侠自己摸索\buu_rsa_shaoxia_rsa.py`
- 法2：直接用`gmpy2`求解。`buu_rsa_请少侠自己摸索\buu_rsa_shaoxia.py`。因为开头有坏数据所以没法 decode 。而 rsa 这个包能帮我们自动去掉坏数据

`rsa`包的安装：`pip install --user rsa`

通过阅读源码可知，`libnum`的`s2n`和`rsa`包的`decrypt`方法主要都是用`int.from_bytes(raw_bytes, "big", signed=False)`来把字符串转为int的
