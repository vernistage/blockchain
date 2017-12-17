import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

    def new_block(self):
        """
        Creates a new Block and adds it to the chain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        # Adds a new transaction to the list of transactions
        # Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the sender
        :param recipient: <str> Address of recipient
        :param amount: <int> amount
        :return: <int> The index of the Block will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amunt': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """ Creats a sha-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """

    @property
    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
