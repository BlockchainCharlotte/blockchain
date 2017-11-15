import ecdsa
import codecs
from addrgen import addrgen
import pickle


class Wallet(object):

    def __init__(self):
        self.key_pair_address = []  # List of tuples (private_key,
                                 #                 public_key,
                                 #                 address)
        self.active_kpa = ()  # Key pair used to send and recieve transactions 
        self.unspent_transactions = []  # List of tuples (payable_public_key,
                                        #                transaction_id)
        self.balance = 0

    def load_wallet_file(self):
        """Loads key pairs and addresses from
        wallet file"""
        pass

    def write_wallet_file(self, wallet, file_name="wallet.dat"):
        """Pickles Wallet"""
        wallet_obj = open(file_name, 'wb')
        pickle.dump(wallet, wallet_obj)
        wallet_obj.close()

    def find_unspent_transactions(self, blockchain):
        """
        Search blockchain for transactions signed with
        public key in self.public_keys
        """
        pass

    def generate_address(self):
        key_pair_address = addrgen()
        self.key_pair_address.append(key_pair_address)
        self.active_kpa = key_pair_address
        return 

    def sign(private_key, msg):
        sk = ecdsa.SigningKey.from_string(codecs.decode(private_key, "hex"),
                                          curve=ecdsa.SECP256k1)
        return sk.sign(msg.encode())

    def verify(public_key, signed_msg, msg):
        vk = ecdsa.VerifyingKey.from_string(codecs.decode(
                         public_key, "hex"),
                         curve=ecdsa.SECP256k1)
        return vk.verify(signed_msg, msg.encode())
