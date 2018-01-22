from binascii import hexlify
import ecdsa
import os
import codecs
import hashlib
import base58
import random
import secrets

def addrgen(seed=None):
    """Returns private_key, public_key, and btc_address"""
    # 0 - Having a private ECDSA key
    # create the private key randomly or with a seed
    if seed != None:
        random.seed(a=seed)
        rand_number = random.getrandbits(32)
    else:
        rand_number = os.urandom(32)
    private_key = hexlify(rand_number)
    sk = ecdsa.SigningKey.from_string(codecs.decode(private_key,
                                                    "hex"),
                                      curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    # 1 - Take the corresponding public key generated with it
    # (65 bytes, 1 byte 0x04, 32 bytes corresponding to X coordinate,
    # 32 bytes corresponding to Y coordinate)
    public_key = hexlify('\04'.encode() + vk.to_string())
    # 2 - Perform SHA-256 hashing on the public key
    # 3 - Perform RIPEMD-160 hashing on the result of SHA-256
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(codecs.decode(public_key, "hex")).digest())
    # 4 - Add version byte in front of RIPEMD-160 hash
    # (0x00 for Main Network)
    versioned_hash = '\00'.encode() + ripemd160.digest()
    # 5 - Perform SHA-256 hash on the extended RIPEMD-160 result
    # 6 - Perform SHA-256 hash on the result of the previous SHA-256 hash
    double_hash = hashlib.sha256(hashlib.sha256(versioned_hash
                                                ).digest()).digest()
    # 7 - Take the first 4 bytes of the second SHA-256 hash.
    # This is the address checksum
    checksum = double_hash[:4]
    # 8 - Add the 4 checksum bytes from stage 7 at the end of
    # extended RIPEMD-160 hash from stage 4. This is the 25-byte
    # binary Bitcoin Address.
    binary_addr = versioned_hash + checksum
    # 9 - Convert the result from a byte string into a base58 string
    # using Base58Check encoding. This is the most commonly used
    # Bitcoin Address format
    btc_address = base58.b58encode(binary_addr)
    return private_key, public_key, btc_address


if __name__ == '__main__':
    private_key, public_key, btc_address = addrgen()
    print(f'Private Key: {private_key}')
    print(f'Public_Key: {public_key}')
    print(f'BTC Address: {btc_address}')
    print("_________________________________________________________________________________")
