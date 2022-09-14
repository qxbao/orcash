import functools
from utility.wallet import Wallet

class Verification:
    @staticmethod
    def verify_chain(blockchain):
        for (i, block) in enumerate(blockchain):
            if i == 0:
                continue
            if block.last_hash != blockchain[i - 1].hashme(block.proof):
                return False
        return True
    
    @staticmethod
    def check_transaction(transaction, transactions, check_balance):
        sender_balance = check_balance()
        just_spent = [trans.amount for trans in transactions if trans.sender == transaction.sender]
        just_received = [trans.amount for trans in transactions if trans.receiver == transaction.sender]
        just_spent = functools.reduce(lambda a, b: a + b, just_spent, 0)
        just_received = functools.reduce(lambda a, b: a + b, just_received, 0)
        if sender_balance >= transaction.amount - just_received + just_spent:
            return True and Wallet.verify_transaction(transaction)
        return False

    @classmethod
    def check_transactions(cls, transactions, check_balance):
        return all([cls.check_transaction(trans, transactions, check_balance) for trans in transactions])