# The careful bioinformatician should check if there are other short regions in the genome
# exhibiting multiple occurrences of a n-mer and its complement. After all, maybe therse strings
# occur as repeats throughout the entire genome, rather than just in the ori region. The goal is 
# to create a program to find all occurrences of a pattern in a string.

def findPatternMatching(dna_sequence, pattern):

    matching_positions = []

    for position in range(0, len(dna_sequence) - len(pattern)):
        if dna_sequence[position:position+len(pattern)] == pattern:
            matching_positions.append(position)
    
    return matching_positions

if __name__ == '__main__': 

    # If it is an extremely large input, you can better store it in a .txt file and then open and read its content from
    # this program.    
    dna_sequence = input()
    pattern = input()

    matching_positions = findPatternMatching(dna_sequence, pattern)

    print(*matching_positions, sep=" ")
