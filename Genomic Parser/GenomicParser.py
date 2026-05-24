rnadict = {
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "CUU": "Leucine",
    "CUC": "Leucine",
    "CUA": "Leucine",
    "CUG": "Leucine",
    "AUU": "Isoleucine",
    "AUC": "Isoleucine",
    "AUA": "Isoleucine",
    "AUG": "Methionine",
    "GUU": "Valine",
    "GUC": "Valine",
    "GUA": "Valine",
    "GUG": "Valine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "CCU": "Proline",
    "CCC": "Proline",
    "CCA": "Proline",
    "CCG": "Proline",
    "ACU": "Threonine",
    "ACC": "Threonine",
    "ACA": "Threonine",
    "ACG": "Threonine",
    "GCU": "Alanine",
    "GCC": "Alanine",
    "GCA": "Alanine",
    "GCG": "Alanine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UAA": "Ochre",
    "UAG": "Amber",
    "CAU": "Histidine",
    "CAC": "Histidine",
    "CAA": "Glutamine",
    "CAG": "Glutamine",
    "AAU": "Asparagine",
    "AAC": "Asparagine",
    "AAA": "Lysine",
    "AAG": "Lysine",
    "GAU": "Aspartic acid",
    "GAC": "Aspartic acid",
    "GAA": "Glutamic acid",
    "GAG": "Glutamic acid",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGA": "Opal",
    "UGG": "Tryptophan",
    "CGU": "Arginine",
    "CGC": "Arginine",
    "CGA": "Arginine",
    "CGG": "Arginine",
    "AGU": "Serine",
    "AGC": "Serine",
    "AGA": "Arginine",
    "AGG": "Arginine",
    "GGU": "Glycine",
    "GGC": "Glycine",
    "GGA": "Glycine",
    "GGG": "Glycine",
}

weight_dict = {
    "Glycine": 57.05132,
    "Alanine": 71.0779,
    "Serine": 87.0773,
    "Proline": 97.11518,
    "Valine": 99.13106,
    "Threonine": 101.10388,
    "Cysteine": 103.1429,
    "Leucine": 113.15764,
    "Isoleucine": 113.15764,
    "Asparagine": 114.10264,
    "Aspartic acid": 115.0874,
    "Glutamine": 128.12922,
    "Lysine": 128.17228,
    "Glutamic acid": 129.11398,
    "Methionine": 131.19606,
    "Histidine": 137.13928,
    "Phenylalanine": 147.17386,
    "Selenocysteine": 150.3079,
    "Arginine": 156.18568,
    "Tyrosine": 163.17326,
    "Tryptophan": 186.2099,
    "Pyrrolysine": 237.29816
}

with open('sequence.fasta', 'r') as file:

    raw_data = file.read()
    split_list = raw_data.split('\n')

    pure_dna = split_list[1]

    rna_sequence = pure_dna.replace('T', 'U')

    codons = []
    protein_chains = []

    total_weight = 0

    for i in range(0, len(rna_sequence), 3):

        chunk = rna_sequence[i:i+3]

        if chunk in ["UAA","UAG", "UGA"]:
            break
      
        codons.append(chunk)

    

    for chunk in codons:

        amino_acid = rnadict.get(chunk, "Unknown")

        protein_chains.append(amino_acid)
    
    for aa in protein_chains:

        total_weight += weight_dict.get(aa, 0)
            
print(codons)
print(protein_chains)
print(f'total molecular weight: {total_weight}')
