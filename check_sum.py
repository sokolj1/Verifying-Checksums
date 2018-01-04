import struct
import crcmod.predefined as crc
import sys, numpy as np

crc32func = crc.mkCrcFun('Crc32') # makes Crc-32 checksum method assigned to crc32func
byte = struct.Struct('<HLL')      # uses struct module to retrieve 10 little endian bytes in dataset.dat
initial_list = []                 # empty list for all unpacked data (unchecked values and the checksums)
final_list = []                   # empty list for encoded values run through the checksum method

with open('dataset.dat','rb') as f:            # opens and reads binary file dataset.dat
    while True:
        data = f.read(byte.size)               # continously reads in 10 bytes per line until end of file
        if not data:                           # when file ends, break
            break
        data_final = byte.unpack(data)         # interprets binary data as three number tuple
        initial_list.append(data_final)        # appends tuples to initial list

    unchecked_values = [str(i[1]) for i in initial_list]              # stores unchecked values
    encoded_values = [i.encode('utf-8') for i in unchecked_values]    # encodes unchecked values as utf-8(pyt3)
    given_checksums = [str(i[2]) for i in initial_list]               # stores provided checksum values

for i in encoded_values:                          # for loop runs encoded values into checksum method
        checked_values = str(crc32func(i))
        final_list.append(checked_values)     # stores now checked encoded values in final_list

array = np.array(final_list) == np.array(given_checksums)      # compares checked values to provided checksums
print(array)                                             # prints the comparisons, yields two false values
false_values = np.where(array==False)                    # extracts the list index where array is false
print(false_values)                                      # prints the false values 13 and 37



