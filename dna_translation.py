# dna_translation.py
# my program to change DNA into protein

# codon table
CODON_TABLE = {
    "ATA":"I","ATC":"I","ATT":"I","ATG":"M",
    "ACA":"T","ACC":"T","ACG":"T","ACT":"T",
    "AAC":"N","AAT":"N","AAA":"K","AAG":"K",
    "AGC":"S","AGT":"S","AGA":"R","AGG":"R",
    "CTA":"L","CTC":"L","CTG":"L","CTT":"L",
    "CCA":"P","CCC":"P","CCG":"P","CCT":"P",
    "CAC":"H","CAT":"H","CAA":"Q","CAG":"Q",
    "CGA":"R","CGC":"R","CGG":"R","CGT":"R",
    "GTA":"V","GTC":"V","GTG":"V","GTT":"V",
    "GCA":"A","GCC":"A","GCG":"A","GCT":"A",
    "GAC":"D","GAT":"D","GAA":"E","GAG":"E",
    "GGA":"G","GGC":"G","GGG":"G","GGT":"G",
    "TCA":"S","TCC":"S","TCG":"S","TCT":"S",
    "TTC":"F","TTT":"F","TTA":"L","TTG":"L",
    "TAC":"Y","TAT":"Y","TAA":"*","TAG":"*",
    "TGC":"C","TGT":"C","TGA":"*","TGG":"W",
}

# function to translate dna to protein
def translate_dna(seq):
    seq = seq.upper().replace("U","T")
    protein = []
    for i in range(0, len(seq)-2, 3):
        codon = seq[i:i+3]
        aa = CODON_TABLE.get(codon, "X")
        protein.append(aa)
    return "".join(protein)

# example dna test
if __name__ == "__main__":
    dna = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
    print("DNA:", dna)
    print("Protein:", translate_dna(dna))
