import binascii
import struct
hex_str = '47494638396101000100800000000000ffffff21f9' + \
    '0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(hex_str)
print(len(gif))

print(gif[:6] == b'GIF89a')
print(gif[:6] == 'GIF89a')
print(type(gif))
print(type('GIF89a'))
print(type(b'GIF89a'))

wight, hight = struct.unpack('<HH', gif[6:10])
print(wight, hight)
