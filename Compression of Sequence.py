def compress(sequence):
    base = max(sequence)+1
    seq_length = len(sequence)
    value = 0
    for element in sequence:
        value += element * base**(seq_length-1)
        seq_length -= 1
    return value, base, len(sequence)

def decompress(value, base, seq_length):
    seq = []
    while value >= base:
        remainder = value % base
        seq.insert(0,remainder)
        value -= remainder
        value = int(value/base)
    seq.insert(0,value)
    seq = [0]*(seq_length - len(seq))+seq
    return sequence

import random
sequence = [random.randint(0, 1) for _ in range(1000)]
value, base, seq_length = compress(sequence)
seq = decompress(value, base, seq_length)

print(seq==sequence)#Checking the Accuracy if True means 100%
