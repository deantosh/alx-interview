#!/usr/bin/python3
"""
Write a method that determines if a given data set represents a valid
UTF-8 encoding.
 - Prototype: def validUTF8(data)
 - Return: True if data is a valid UTF-8 encoding, else return False
 - A character in UTF-8 can be 1 to 4 bytes long
 - The data set can contain multiple characters
 - The data will be represented by a list of integers
 - Each integer represents 1 byte of data, therefore you only need to
   handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """ Check if data is a valid UTF-8 encoded """
    num_bytes = 0

    for byte in data:
        # mask value > 255 handle only 8 lsb
        byte &= 0xFF

        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1  # Expect 1 continuation byte
            elif (byte >> 4) == 0b1110:
                num_bytes = 2  # Expect 2 continuation byte
            elif (byte >> 3) == 0b11110:
                num_bytes = 3  # Expect 3 continuation byte
            elif (byte >> 7) != 0:
                # If not a single byte
                return False
        else:
            # check continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
