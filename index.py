from hashlib import sha256
import sys
sys.path.append('class/')
import functools
from block import Block
from transaction import Transaction
from blockchain import Blockchain

origin_block = Block(1, '', 'The Origin and Powerful Block', 0, 0)

blockchain = Blockchain(origin_block)
transactions = []

def check_balance(name):
    spent_inblock = [[trans['amount'] for trans in block.data if trans['sender'] == name] for block in blockchain.data if type(block.data) is list]
    received_inblock = [[trans['amount'] for trans in block.data if trans['receiver'] == name] for block in blockchain.data if type(block.data) is list]
    spent = 0
    received = 0
    
    for money in spent_inblock:
        spent += sum(money)
    
    for money in received_inblock:
        received += sum(money)
    return received - spent

def check_transaction(transaction):
    sender_balance = check_balance(transaction.sender)
    just_spent = [trans.amount for trans in transactions if trans.sender == transaction.sender]
    just_received = [trans.amount for trans in transactions if trans.receiver == transaction.sender]
    just_spent = functools.reduce(lambda a, b: a + b, just_spent, 0)
    just_received = functools.reduce(lambda a, b: a + b, just_received, 0)
    if sender_balance > transaction.amount + just_received - just_spent:
        return True
    return False


def transfer():
    sender = input('Người gửi: ')
    receiver = input('Người nhận: ')
    amount = float(input('Số tiền: '))
    contract = Transaction(sender, receiver, amount)
    if check_transaction(contract):
        transactions.append(contract)
        return True
    return False


def mine_block(name):
    global transactions
    block = blockchain.last_block()
    proof = 0
    while(True):
        string = '@'.join(str(block.timestamp) + block.last_hash + str(block.data) + str(proof))
        hashed = sha256(string.encode()).hexdigest()
        if all([letter == '0' for letter in hashed[:blockchain.difficult]]):
            print('{}: THÀNH CÔNG!'.format(hashed))
            print('Bạn đã đào thành công block số {}. Đang xác minh tính chân thực...'.format(len(blockchain.data) + 1))
            if blockchain.last_block().hashme(proof) == hashed:
                print('---HÀM BĂM TRÙNG KHỚP---')
                reward = Transaction('Mine', name, 2.5)
                transactions.append(reward)
                new_block = Block(len(blockchain.data) + 1, hashed, [trans.__dict__ for trans in transactions], proof)
                blockchain.add_block(new_block)
                transactions = []
                print('{} nhận được 2.5 coin. Xin chúc mừng '.format(name))
            else:
                print('Phát hiện thông tin sai lệch. Block không được chấp thuận')
            break
        print('{}: KHÔNG THÀNH CÔNG'.format(hashed))
        proof+=1


while (True):
    cmd = input('Vui lòng nhập lệnh:')
    if cmd == 'quit':
        break;
    if cmd == 'transfer':
        if transfer():
            print('Chuyển tiền thành công')
        else:
            print('Chuyển tiền thất bại')
        continue
    if cmd == 'mine':
        name = input('Nhập tên: ')
        mine_block(name)
        continue
    if cmd == 'check':
        print([block.__dict__ for block in blockchain.data])
    if cmd == 'balance':
        name = input('Nhập tên: ')
        print(check_balance(name))