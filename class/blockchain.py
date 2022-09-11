from hashlib import sha256
import math
from block import Block
from verification import Verification as moderator
from transaction import Transaction


class Blockchain:
    def __init__(self, hosting_node_id):
        genesis = Block(1, '', 'The most powerful Block (^^)', 0, 0)
        self.__data = [genesis]
        self.reward = math.floor(50 * (0.9 ** (len(self.get_data()) // 190704)))
        self.difficult = 3 + math.ceil(7 * (len(self.get_data()) / 19072004))
        self.__transactions = []
        self.hosting_node = hosting_node_id

    def get_data(self):
        return self.__data.copy()

    def get_trans(self):
        return self.__transactions.copy()

    def last_block(self):
        return self.get_data()[-1]

    def add_block(self, new_block):
        new_block.index = len(self.get_data()) + 1
        self.__data.append(new_block)

    def add_trans(self, transaction):
        self.__transactions.append(transaction)

    def mine(self):
        block = self.last_block()
        proof = 0
        while(True):
            string = '@'.join(str(block.timestamp) + block.last_hash + str(block.data) + str(proof))
            hashed = sha256(string.encode()).hexdigest()
            if all([letter == '0' for letter in hashed[:self.difficult]]):
                print('{}: THÀNH CÔNG!'.format(hashed))
                print('Bạn đã đào thành công block số {}. Đang xác minh tính chân thực...'.format(len(self.get_data())))
                if self.last_block().hashme(proof) == hashed:
                    print('---HÀM BĂM TRÙNG KHỚP---')
                    if not moderator.verify_chain(self.get_data()):
                        return print('Blockchain xuất hiện xung đột thông tin. Block của bạn không được chấp thuận')
                    print('---KẾT QUẢ ĐÃ ĐƯỢC XÁC MINH---')
                    reward = Transaction('Mine', self.hosting_node, self.reward)
                    self.add_trans(reward)
                    new_block = Block(len(self.get_data()) + 1, hashed, [trans.__dict__ for trans in self.get_trans()], proof)
                    self.add_block(new_block)
                    self.__transactions = []
                    print('{} nhận được {} coin. Xin chúc mừng '.format(self.hosting_node, self.reward))
                else:
                    print('Phát hiện thông tin sai lệch. Block không được chấp thuận')
                break
            print('{}: KHÔNG THÀNH CÔNG'.format(hashed))
            proof+=1