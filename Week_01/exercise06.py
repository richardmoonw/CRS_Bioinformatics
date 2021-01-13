# We defined a k-mer as a "clump" if it appears many times within a short interval of the genome. More formally, given integers L 
# and t, a k-mer Pattern forms an (L,t)-clump inside a (longer) string Genome if there is an interval of Genome of length L in
# which this k-mer appears at least t times. (This definition assumes that the k-mer completely fits within the interval). This 
# also does not take reverse complements into account yet.) The goal is to create a program to find patterns forming clumps in a 
# string.


def findClumps(dna_sequence, k, window_len, t):

    dna_sequence_len = len(dna_sequence)
    count = 0
    k_mers = {}

    for x in range (0, dna_sequence_len - (k-1)):

        if dna_sequence[x:x+k] not in k_mers:
            k_mers[dna_sequence[x:x+k]] = []

        k_mers[dna_sequence[x:x+k]].append(x)

    for key in k_mers:
        
        # If there are more than t repetitions.
        if len(k_mers[key]) >= t:

            for x in range(0, len(k_mers[key]) - (t-1)):

                if((k_mers[key][x+(t-1)] + k) - k_mers[key][x] <= window_len):
                    count += 1
                    break

    return count

if __name__ == '__main__':

    dna_sequence_file = open("dataset.txt", "r")
    dna_sequence = dna_sequence_file.read()
    k = int(input())
    window_len = int(input())
    t = int(input())

    count = findClumps(dna_sequence, k, window_len, t)

    print(str(count))
