import os
import binascii

# os.urandom()を利用して、秘密鍵をASCII形式で作成してください
secret_key = os.urandom(32)
print(secret_key)
print(binascii.hexlify(secret_key))

# secret_key2 = os.urandom(1)
# print(secret_key2)
# print(binascii.hexlify(b'0'))
# print(int(binascii.hexlify(b'0'),16))

# print(int('bdd03cb27bfd5c61254e693f246a0a2ee9dc66ac698936d5d932fafe6012f1d5',16))
# print(bin(int('bdd03cb27bfd5c61254e693f246a0a2ee9dc66ac698936d5d932fafe6012f1d5',16)))