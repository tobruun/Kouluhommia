import pandas as pd

def salasanojen_filtterointi(input_file, output_file):

    df = pd.read_csv(input_file, delimiter='\t', encoding='utf-8')

    filtered_df = df[(df['Hakusana'].str.len() >= 5) & (df['Hakusana'].str.len() <= 12)]

    if not filtered_df.empty:

        filtered_df.to_csv(output_file, index=False, sep='\t', encoding='utf-8')
        print(f"words saved to {output_file}.")
    else:
        print("not ofund")


if __name__ == "__main__":
    input_file = ''  
    output_file = ''   
    salasanojen_filtterointi(input_file, output_file)
