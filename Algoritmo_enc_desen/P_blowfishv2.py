#DES DATA ENCRYPTION STANDARD
from Crypto.Cipher import Blowfish
from struct import pack

bs = Blowfish.block_size
key = b'FCFM'
cipher = Blowfish.new(key, Blowfish.MODE_CBC)
text = b'Texto cifrado compa'
plen = bs - len(text) % bs
padding = [plen]*plen
padding = pack('b'*plen, *padding)
msg = cipher.iv + cipher.encrypt(text + padding)
print(msg)

iv = msg[:bs] #vector de inicializacion
msg = msg[bs:] #se elimina la primer parte del relleno de encriptacion
cipher = Blowfish.new(key, Blowfish.MODE_CBC,iv)
msgdes = cipher.decrypt(msg)

last_byte = msgdes[-1] #ultimo byte
msgdes = msgdes[:- (last_byte if type(last_byte) is int else ord(last_byte))]
print(repr(msgdes))