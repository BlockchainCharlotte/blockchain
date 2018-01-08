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

    def load_wallet_file(self, wallet, path):
        """
        Loads key pairs and addresses from
        wallet file
        :param wallet: <object> Wallet Object
        :param path: <str> Path to wallet file
        """
        wallet_f = open(path, 'r')
        pickle.load(wallet_f)
        wallet_f.close()

    def write_wallet_file(self, wallet, file_name="wallet.dat"):
        """
        Pickles Wallet
        :param wallet: <object> Wallet Object
        :file_name: <str>  Optional wallet name
        """
        wallet_obj = open(file_name, 'wb')
        pickle.dump(wallet, wallet_obj)
        wallet_obj.close()

    def find_unspent_transactions(self, blockchain):
        """
        Search blockchain for transactions signed with
        public key in self.public_keys
        :param blockchain: <list> A blockchain
        """
        pass

    def generate_address(self):
        key_pair_address = addrgen()
        self.key_pair_address.append(key_pair_address)
        self.active_kpa = key_pair_address
        print(key_pair_address)
        return key_pair_address

    def sign(private_key, msg):
        sk = ecdsa.SigningKey.from_string(codecs.decode(private_key, "hex"),
                                          curve=ecdsa.SECP256k1)
        return sk.sign(msg.encode())

    def verify(public_key, signed_msg, msg):
        vk = ecdsa.VerifyingKey.from_string(codecs.decode(
                         public_key, "hex"),
                         curve=ecdsa.SECP256k1)
        return vk.verify(signed_msg, msg.encode())
