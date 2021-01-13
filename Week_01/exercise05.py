# We defined a k-mer as a "clump" if it appears many times within a short interval of the genome. More formally, given integers L 
# and t, a k-mer Pattern forms an (L,t)-clump inside a (longer) string Genome if there is an interval of Genome of length L in
# which this k-mer appears at least t times. (This definition assumes that the k-mer completely fits within the interval). This 
# also does not take reverse complements into account yet.) The goal is to create a program to find patterns forming clumps in a 
# string.

import exercise02

def findClumps(dna_sequence, k, window_len, t):

    patterns = set()
    dna_sequence_len = len(dna_sequence)

    for x in range (0, dna_sequence_len - window_len):

        current_window = dna_sequence[x:x+window_len]
        window_frequency_table = exercise02.createFrequencyTable(current_window, k)

        for key in window_frequency_table:
            if window_frequency_table[key] >= t:
                patterns.add(key)
    
    return patterns

if __name__ == '__main__':

    dna_sequence = input()
    k = int(input())
    window_len = int(input())
    t = int(input())

    patterns = findClumps(dna_sequence, k, window_len, t)

    print(*patterns, sep=" ")