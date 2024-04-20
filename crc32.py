import libscrc

f = open("FFFFF.bin", mode="rb")

# Reading file data with read() method
data = f.read()

# Printing our byte sequenced data
print(data)

# Closing the opened file
f.close()

crc32 = libscrc.mpeg2(data)
print(crc32)