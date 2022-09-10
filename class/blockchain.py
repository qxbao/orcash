class Blockchain:
    difficult = 3

    def __init__(self, first_block):
        self.first_block = first_block
        self.data = [first_block]

    def last_block(self):
        return self.data[-1]

    def add_block(self, new_block):
        new_block.index = len(self.data) + 1
        self.data.append(new_block)

    def verify(self):
        for (i, block) in enumerate(self.data):
            if i == 0:
                continue
            if block.hash != block.hashme():
                return False
            if block.last_hash != self.data[i - 1].hashme():
                return False
        return True