from base64 import decode
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import Crypto.Random
import binascii

class Wallet:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        
    def load(self):
        pass

    def create(self):
        private_key = RSA.generate(1024, Crypto.Random.new().read)
        public_key = private_key.publickey()
        self.private_key, self.public_key = binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'), binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
    
    def sign_transaction(self, sender, receiver, amount):
        signer = PKCS1_v1_5.new( RSA.importKey( binascii.unhexlify(self.private_key) ) )
        hashed = SHA256.new((str(sender) + str(receiver) + str(amount)).encode('utf-8'))
        signature = signer.sign(hashed)
        return binascii.hexlify(signature).decode('ascii')

    @staticmethod
    def verify_transaction(transaction):
        if transaction.sender == 'Mine':
            return True
        public_key = RSA.importKey(binascii.unhexlify(transaction.sender))
        verifier = PKCS1_v1_5.new(public_key)
        hashed = SHA256.new((str(transaction.sender) + str(transaction.receiver) + str(transaction.amount)).encode('utf-8'))
        return verifier.verify(hashed, binascii.unhexlify(transaction.signature))