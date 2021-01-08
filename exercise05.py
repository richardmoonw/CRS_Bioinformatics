# We defined a k-mer as a "clump" if it appears many times within a short interval of the genome. More formally, given integers L 
# and t, a k-mer Pattern forms an (L,t)-clump inside a (longer) string Genome if there is an interval of Genome of length L in
# which this k-mer appears at least t times. (This definition assumes that the k-mer completely fits within the interval). This 
# also does not take reverse complements into account yet.) The goal is to create a program to find patterns forming clumps in a 
# string.

import exercise04

def findClumps(dna_sequence, k, window_len, t):

    patterns = []
    dna_sequence_len = len(dna_sequence)

    for x in range (0, dna_sequence_len - window_len):

        current_window = dna_sequence[x:x+window_len]
        exercise04.findPatternMatching(current_window, k)