import ecdsa
import codecs
from .addrgen import addrgen
import pickle


class Wallet(object):
    """
    A Basic Heirarchial deterministic wallet class.
    """
    def __init__(self, node="127.0.0.0.0:5000"):
        self.key_pair_address = []  # List of tuples (private_key,
                                 #                 public_key,
                                 #                 address)
        self.active_kpa = ()  # Key pair used to send and recieve transactions 
        self.unspent_transactions = []  # List of tuples (payable_public_key,
                                        #                transaction_id)
        self.balance = 0
        self.node = node

    def load_wallet_file(self, wallet, path):
        """
        Loads key pairs and addresses from
        wallet file
        :param wallet: <object> Wallet Object
        :param path: <str> Path to wallet file
        """
        wallet_f = open(path, 'rb')
        wallet = pickle.load(wallet_f)
        wallet_f.close()
        self.key_pair_address = wallet[0]
        self.active_kpa = wallet[1]
        self.unspent_transactions = wallet[2]
        return None

    def write_wallet_file(self, file_name="wallet.dat"):
        """
        Pickles Wallet
        :param wallet: <object> Wallet Object
        :file_name: <str>  Optional wallet name
        """
        wallet = [self.key_pair_address, self.active_kpa,
                  self.unspent_transactions]
        wallet_obj = open(file_name, 'wb')
        pickle.dump(wallet, wallet_obj)
        wallet_obj.close()
        return None

    # TODO update find_unspent_transactions function
    def find_unspent_transactions(self, blockchain):
        """
        Search blockchain for transactions signed with
        public key in self.public_keys
        :param blockchain: <list> A blockchain
        """
        pass

    # TODO update refresh balance function 
    def refresh_balance(self):
        """
        Refreshes balance based on unspent transactions
        """
        pass

    def generate_address(self, seed):
        """
        Generates a key pair and BTC address
        """
        if len(key_pair_address) == 0:
            key_pair_address = addrgen()
        else:
            if seed == None:
                sd = seed
            else:
                sd = len(self.key_pair_address) - 1
            key_pair_address = addrgen(seed=sd[0])
        self.key_pair_address.append(key_pair_address)
        self.active_kpa = key_pair_address
        print(key_pair_address)
        return key_pair_address

    def sign(private_key, msg):
        """
        :param private_key: b<str> Private Key
        :param msg: b<str> encoded message
        """
        sk = ecdsa.SigningKey.from_string(codecs.decode(private_key, "hex"),
                                          curve=ecdsa.SECP256k1)
        return sk.sign(msg.encode())

    def verify(public_key, signed_msg, msg):
        """
        :param public_key: b<str> Public key
        :param signed_msg: b<str> Message signed with private key
        :param msg: b<str> unsigned message
        """
        vk = ecdsa.VerifyingKey.from_string(codecs.decode(
                         public_key, "hex"),
                         curve=ecdsa.SECP256k1)
        return vk.verify(signed_msg, msg.encode())

    def send(self, amount, recipient):
        """
        Send amount to recipient. Parse through UTXOs
        to find collective transactions >= amount.
        Create a new transaction referencing the UTXOs,
        recipient and a signed hash.
        """
        pass

