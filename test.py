from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import Crypto.Random
import binascii

private_key = RSA.generate(1024, Crypto.Random.new().read)
public_key = private_key.publickey()
a,b =  binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'), binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
print(private_key.exportKey(format='DER'))