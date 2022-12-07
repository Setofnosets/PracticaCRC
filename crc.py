from bitarray import bitarray
from bitarray import util
import random

def compute(filename: str, divisor: bitarray, len_crc: int) -> tuple[bitarray, bitarray]:
    """    This function computes the CRC of a plain-text file
             arguments:
             filename: the file containing the plain-text
             divisor: the generator polynomial
             len_crc: The number of redundant bits (r)    """
    # Read the file
    file = open(filename, encoding="UTF-8", mode="r")
    text = file.read()
    msg = bitarray()
    msg.frombytes(text.encode('utf-8'))
    # Append r zeros
    crc = bitarray(len_crc)
    crc.setall(0)
    # Mod 2 division
    rem = mod2_div(msg + crc, divisor)
    return msg, rem

def mod2_div(dividend: bitarray, divisor: bitarray) -> bitarray:
    """    This function performs mod-2 divison (without carry)
             Arguments:
             dividend: a bitarray holding the dividend
             divisor: a bitarray holding the divisor
             returns:    remainder: a bitarray holding the divider    """
    while len(dividend) >= len(divisor):
        j = 0
        # Iterate until the first 1 is found
        while dividend[j] == 0 or j == len(dividend)-1:
            j += 1
        # XOR operation
        for i in range(len(divisor)):
            dividend[j] = dividend[j] ^ divisor[i]
            j += 1
        # Remove leading zeros
        dividend = util.strip(dividend, 'left')
    while len(dividend) < len(divisor)-1:
        dividend.insert(0, 0)
    if dividend == bitarray(''):
        dividend = bitarray(len(divisor))
        dividend.setall(0)
    return dividend

def burst_error(msg: bitarray, n: int, seed: int) -> bitarray:
    """    This function generates an error burst of length n
              Arguments:
              msg: A bitarray holding the message to be corrupted
              n: The length of the error burst
              seed: An integer to set the RNG (MT19937)
              Returns:    A corrupted message     """
    # Set the seed
    random.seed(seed)
    # Generate a random index
    index = random.randint(0, len(msg)-n)
    # Generate the error burst
    for i in range(n):
        random_bit = random.randint(0, 1)
        if i == 0 or i == n-1:
            msg[index+i] = msg[index+i] ^ 1
        else:
            msg[index+i] = msg[index+i] ^ random_bit
    return msg
