import sys
import pandas as pd

# Fazer a base de 2013 a 2021

def concatenate_csv(file1, file2, output_file, match_columns, merge_type):
    # Read CSV files
    df1 = pd.read_csv(file1, delimiter=';')
    df2 = pd.read_csv(file2, delimiter=';')

    merged_df = pd.merge(df1, df2, on=match_columns, how=merge_type, suffixes=('_x', ''))
    
    # merged
    # merged_df[(merged_df['NO_CATEGORIA'] == 'Total') & (merged_df['NO_DEPENDENCIA'] == 'Total')]
    
    columns_to_drop = [col for col in merged_df.columns if col.endswith('_x')]

    merged_df.drop(columns_to_drop, axis=1, inplace=True)
    
    merged_df = merged_df[(merged_df['NO_CATEGORIA'] == 'Total') & (merged_df['NO_DEPENDENCIA'] == 'Total')]
    
    merged_df.replace(regex=r',(\d+)', value=r'.\1', inplace=True)
    
    merged_df.to_csv(output_file, index=False, sep=';')
    print("Concatenation completed. Merged data saved to", output_file)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python concatenate.py <arquivo_resposta.csv> <arquivo_entrada.csv>")
    else:
        # Specify input CSV files
        csv_file1 = sys.argv[1]
        csv_file2 = sys.argv[2]
        match_columns = sys.argv[3]
        merge_type = sys.argv[4]

        # Specify output file
        output_csv = sys.argv[1]

        # Call the function to concatenate CSV files
        concatenate_csv(csv_file1, csv_file2, output_csv, match_columns.split(';'), merge_type)