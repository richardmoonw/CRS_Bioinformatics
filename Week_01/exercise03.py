# Given a nucleotide p, we denote its complementary nucleotide as p*. The reverse component
# of a string Pattern = p1 ... pn is the string Patternrc = pn* ... p1* formed by taking the 
# complement of each nucleotide in Pattern, then reversing the result string. The goal is to
# create a program to find the reverse complement of a DNA string. 

def findReverseComplement(leading_strand):

    lagging_strand = ""

    for nucleobase in leading_strand:
        if nucleobase == "A":
            lagging_strand += "T"
        elif nucleobase == "C":
            lagging_strand += "G"
        elif nucleobase == "G":
            lagging_strand += "C"
        elif nucleobase == "T":
            lagging_strand += "A"
    
    reversed_lagging_strand = lagging_strand[::-1]

    return reversed_lagging_strand

if __name__ == '__main__':

    leading_strand = input()

    reversed_lagging_strand = findReverseComplement(leading_strand)

    print(reversed_lagging_strand)

