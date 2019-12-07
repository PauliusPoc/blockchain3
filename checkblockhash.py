import hashlib
from struct import pack, unpack, unpack_from
from binascii import unhexlify
from bitcoin.rpc import RawProxy
import datetime, calendar
import sys

import hashlib
from struct import pack, unpack, unpack_from
from binascii import unhexlify
from bitcoin.rpc import RawProxy
import datetime, calendar
import sys

def to_little_endian(hexstring):
    ba = bytearray.fromhex(hexstring)
    ba.reverse()
    s = ''.join(format(x, '02x') for x in ba)
    return s


p = RawProxy()
blockheight = int(sys.argv[1])

blockhash = p.getblockhash(blockheight)
block = p.getblock(blockhash)

header_hex = (to_little_endian(block['versionHex']) + to_little_endian(block['previousblockhash'])
                      + to_little_endian(block['merkleroot']) + to_little_endian(format(int(block['time']), 'x'))
                      + to_little_endian(block['bits']) + to_little_endian(format(int(block['nonce']), 'x')))

headerByte = unhexlify(header_hex)
hash = hashlib.sha256(hashlib.sha256(headerByte).digest()).digest()
hash = hash[::-1].hex()

if hash == block['hash']:
    print("[V] Bloko hash'as yra teisingas!")
else:
    print("[X] Bloko hash'as yra neteisingas!")