
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

'''
For usage: https://liodeus.github.io/2020/08/11/bufferOverflow.html#:~:text=Now%20to%20found%20those%20bad%20characters%20use%20this,again%20%3A%20%21mona%20compare%20-f%20C%3Amona%3CPATH%3Ebytearray.bin%20-a%20%3CESP_ADDRESS%3E
We will send bad characters recursively and analyze if they need to be removed. Let generate the list of bad characters with mona :

!mona bytearray -b "\x00"
Copy the results in the variable payload. And re-run exploit.py, the application should crash. Now to found those bad characters use this command :

!mona compare -f C:\mona\<PATH>\bytearray.bin -a <ESP_ADDRESS>
If BadChars are found, we need to exclude them as well.

!mona bytearray -b "\x00 + <BAD_CHARS>"

# Example
!mona bytearray -b "\x00\x01\x02\x03"
Then compare again :

!mona compare -f C:\mona\<PATH>\bytearray.bin -a <ESP_ADDRESS>
Repeat those two steps until the results status returns Unmodified, this indicates that no more bad characters exist.
'''
