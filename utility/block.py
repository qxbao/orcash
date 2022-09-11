from time import time
from hashlib import sha256

class Block:
    def __init__(self, index, last_hash, data, proof, timestamp = time()):
        self.index = index
        self.last_hash = last_hash
        self.data = data
        self.timestamp = timestamp
        self.proof = proof

    def hashme(self, proof):
        text = '@'.join(str(self.timestamp) + str(self.last_hash) + str(self.data) + str(proof))
        return sha256(text.encode()).hexdigest()