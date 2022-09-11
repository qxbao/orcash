from blockchain import Blockchain
from transaction import Transaction
from verification import Verification as moderator
from uuid import uuid4

class Node:
    def __init__(self):
        self.id = uuid4()
        self.blockchain = Blockchain(self.id)
    
    def transfer(self):
        receiver = input('Người nhận: ')
        amount = float(input('Số tiền: '))
        contract = Transaction(self.id, receiver, amount)
        if moderator.check_transaction(contract, self.blockchain.get_trans(), self.check_balance):
            if moderator.check_transactions(self.blockchain.get_trans(), self.check_balance):
                self.blockchain.add_trans(contract)
                return True
        return False

    def check_balance(self):
        spent_inblock = [[trans['amount'] for trans in block.data if trans['sender'] == self.id] for block in self.blockchain.get_data() if type(block.data) is list]
        received_inblock = [[trans['amount'] for trans in block.data if trans['receiver'] == self.id] for block in self.blockchain.get_data() if type(block.data) is list]
        spent = 0
        received = 0
        
        for money in spent_inblock:
            spent += sum(money)
        
        for money in received_inblock:
            received += sum(money)
        return received - spent