# There is an importan reason to look for frequent words in the ori because for various biological processes, certain nucleotide strings
# often appear surprisingly often in small regions of the genome. This is often because certain proteins can only bind to DNA if a specific
# string of nucleotides is present and if there are more occurrences of the string, then it is more likely that binding will successfully 
# occur. We will use the term k-mer to refer to a string of length k and define Count(Text, Pattern) as the number of times that a k-mer
# Pattern appears as a substring of Text. The goal is to create a program that implements the Count function.

def countPattern(dna_sequence, pattern):
    
    count = 0
    dna_sequence_len = len(dna_sequence)
    pattern_len = len(pattern)

    for x in range(0, dna_sequence_len-(pattern_len-1)):

        if dna_sequence[x:x+pattern_len] == pattern:
            count += 1
        
    return count

if __name__ == '__main__':

    dna_sequence = input()
    pattern = input()

    count = countPattern(dna_sequence, pattern)

    print(str(count))

