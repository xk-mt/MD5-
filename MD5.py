
import hashlib

# a = input('MD5加密文本：')
a='1'
m = hashlib.md5()
for b in range(50):
    m.update(a.encode(encoding='utf-8'))
    a = m.hexdigest()
    print('MD5加密密文：' + a)
m.update(a.encode(encoding='utf-8'))
a = m.hexdigest()
# input('MD5加密密文：' + a)
print('MD5加密密文：' + a)
