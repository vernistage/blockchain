class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

    def new_block(self):
        # Creates a new Block and adds it to the chain
        pass

    def new_transaction(self, sender, recipient, amount):
        # Adds a new transaction to the list of transactions
        # Creates a new transaction to go into the next mined Block
        """
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
        pass

    @staticmethod
    def hash(block):
        # Hashes a block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass
