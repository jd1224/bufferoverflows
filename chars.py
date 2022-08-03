
#start with 00 and enter a space separated list from outpu
bad = "00".split()

#generate a list of characters
print("badchars = ", end='')
for x in range(1,256):
    if "{:02x}".format(x) not in bad:
            print("\\x" + "{:02x}".format(x), end='')

#generate the mona input for immunity
print("\n!mona bytearray -cpb \"", end='')
for byte in bad:
    print(f"\\x{byte}", end='')
print("\"")