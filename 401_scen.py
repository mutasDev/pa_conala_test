#convert a hex-string representation to actual bytes


def hex_to_bytes(hex_string):

byte_array = bytearray.fromhex(hex_string)

return byte_array