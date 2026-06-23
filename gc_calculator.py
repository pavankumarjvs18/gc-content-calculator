DNA_sequence=input("Enter the DNA sequence: ").upper()
if len(DNA_sequence)==0:
    print("DNA sequence cannot be empty.")
    exit()
# checks if the input DNA sequence is empty or not.
for nucleotide in DNA_sequence:
    if nucleotide not in ['A', 'T', 'G', 'C']:  
        print("Invalid DNA sequence. Please check the input")
        exit()
# The above DNA sequence contains the nucleotides G, A, T, and C whose GC content we want to calculate and program will check if input is valid or not. If not valid, it will exit and give an error message.
No_of_Guanines=DNA_sequence.count('G')
# counts the numbers of Guanines in the DNA sequence
No_of_Cytosines=DNA_sequence.count('C')
# counts the numbers of Cytosines in the DNA sequence
Length_of_DNA_strand=len(DNA_sequence)
# calculates the length of the DNA sequence
GC_content=((No_of_Guanines+No_of_Cytosines)/Length_of_DNA_strand)*100
#calculates the GC content of the DNA strand
print("The GC content of the DNA strand is {} %:".format(GC_content))
