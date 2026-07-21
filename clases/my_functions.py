import pandas as pd
from constants import CANONICAL_RESIDUES

def get_aa_frequency(df_data):
    matrix_data = []

    for sequence in df_data["sequence"]:

        row = {
            "sequence" : sequence
        }

        for residue in CANONICAL_RESIDUES:
            row.update({residue: sequence.count(residue)/len(sequence)})
        
        matrix_data.append(row)

    df_frequencies = pd.DataFrame(matrix_data)
    
    return df_frequencies