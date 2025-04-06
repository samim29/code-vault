# Example DNA sequence
dna_sequence = "ATCGATCGATCGTACGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA"
nucleotide_count={"A":0,"T":0,"G":0,"C":0}
for nucleotide in dna_sequence:
    if nucleotide in nucleotide_count:
        nucleotide_count[nucleotide]+=1
for nucleotide,count in nucleotide_count.items():
    print(f"{nucleotide}:{count}")