import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4


class Transaction(object):
    #TODO create transaction object complete with validation function
    # New transaction generation, etc
    def __init__(self, sender, utxo, outputs):
        self.sender = sender
        self.utxo = utxo
        self.outputs = outputs
        self.signed_hash = None

    def new(self, sender, unspent_transactions, outputs,
                    signed_hash=None):
        """
        Creates a new transaction to go into the next mined Block.
        Takes the senders public key, a list of unspent transactions,
        a dictionary of output addresses with amounts and the signed
        hash_details.

        Total amount of outputs should be less than or equal to
        the total amount included in transactions in unspent_transactions.

        :param sender: <str> Senders public key
        :param unspent_transactions: <list> A list of unspent transactions
        :param outputs: <dict> A dictionary of addresses and amounts
        :return: <int> The index of the Block that will hold this transaction
        """
        transaction = {
                 'timestamp': time(),
                 'sender': sender,
                 'unspent_transactions': unspent_transactions,
                 'outputs': outputs, # Format: {'recipient': 1,
                                     #          'recipient2': 10}
                 'signed_hash': signed_hash,
        }
        hash_details = {key: transaction[key] for key in ['outputs',
                                                          'sender',
                                                          'unspent_transactions']}
        transaction['hash'] = self.hash(hash_details)
        self.current_transactions.append(transaction)

        return self.last_block['index'] + 1

        def validate_transaction(self, transaction, blockchain):
            """
            Parse  blockchain to validate known utxos and
            signatures.
            """
            pass

