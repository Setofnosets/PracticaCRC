from bitarray import bitarray

def compute(filename: str, divisor: bitarray, len_crc: int) -> tuple[bitarray, bitarray]:
    """    This function computes the CRC of a plain-text file
             arguments:
             filename: the file containing the plain-text
             divisor: the generator polynomial
             len_crc: The number of redundant bits (r)    """


def mod2_div(dividend: bitarray, divisor: bitarray) -> bitarray:
    """    This function performs mod-2 divison (without carry)
             Arguments:
             dividend: a bitarray holding the dividend
             divisor: a bitarray holding the divisor
             returns:    remainder: a bitarray holding the divider    """


def burst_error(msg: bitarray, n: int, seed: int) -> bitarray:
    """    This function generates a error burst of length n
              Arguments:
              msg: A bitarray holding the message to be corrupted
              n: The length of the error burst
              seed: An integer to set the RNG (MT19937)
              Returns:    A corrupted message     """