from utility.block import Block
from utility.blockchain import Blockchain
from utility.transaction import Transaction
from utility.verification import Verification as moderator
from utility.wallet import Wallet

class Node:
    def __init__(self):
        self.wallet = Wallet()
        self.blockchain = Blockchain(None)
    
    def create_wallet(self):
        self.wallet.create()
        self.blockchain = Blockchain(self.wallet.public_key)

    def transfer(self):
        receiver = input('Người nhận: ')
        amount = float(input('Số tiền: '))
        signature = self.wallet.sign_transaction(self.wallet.public_key, receiver, amount)
        contract = Transaction(self.wallet.public_key, receiver, amount, signature)
        if moderator.check_transaction(contract, self.blockchain.get_trans(), self.check_balance):
            if moderator.check_transactions(self.blockchain.get_trans(), self.check_balance):
                return self.blockchain.add_trans(contract)
        return False

    def check_balance(self):
        spent_inblock = [[trans['amount'] for trans in block.data if trans['sender'] == self.wallet.public_key] for block in self.blockchain.get_data() if type(block.data) is list]
        received_inblock = [[trans['amount'] for trans in block.data if trans['receiver'] == self.wallet.public_key] for block in self.blockchain.get_data() if type(block.data) is list]
        spent = 0
        received = 0
        
        for money in spent_inblock:
            spent += sum(money)
        
        for money in received_inblock:
            received += sum(money)
        return received - spent