# We say that Pattern is a most frequent k-mer in Text if it maximizes Count(Text, Pattern) among all k-mers. The goal is to create a program to
# find the most frequent k-mers in a string.

def findFrequentWords(dna_sequence, k):

    frequency_table = createFrequencyTable(dna_sequence, k)

    max = 0

    for k_mer in frequency_table:
        if frequency_table[k_mer] > max:
            max = frequency_table[k_mer]
    
    most_frequent_words = []
    for key, value in frequency_table.items():
        if value == max:
            most_frequent_words.append(key)

    return most_frequent_words

def createFrequencyTable(dna_sequence, k): 

    frequency_table = {}
    dna_sequence_len = len(dna_sequence)

    for x in range (0, dna_sequence_len-(k-1)):

        if dna_sequence[x:x+k] not in frequency_table:
            frequency_table[dna_sequence[x:x+k]] = 1
        else:
            frequency_table[dna_sequence[x:x+k]] += 1

    return frequency_table

if __name__ == '__main__':

    dna_sequence = input()
    k = input()

    most_frequent_words = findFrequentWords(dna_sequence, int(k))

    print(most_frequent_words)


