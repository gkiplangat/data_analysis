# This file splits the larger excel file into small chanks
# For Example i have a file which if 500,000 rows, 
# Loading it may be a problem, so i nead to split
# using this code

import pandas as pd

def split_excel_file(input_file, output_prefix, chunk_size):

    # Read the Excel file to be splited
    df = pd.read_excel(input_file)

    # Get the number of rows in the dataframe
    total_rows = len(df)

    # Calculate the number of chunks needed
    num_chunks = total_rows // chunk_size + 1

    # Split the dataframe into chunks and save each chunk as a separate Excel file
    for i in range(num_chunks):
        start_row = i * chunk_size
        end_row = min((i + 1) * chunk_size, total_rows)

        chunk_df = df[start_row:end_row]

        output_file = f"{output_prefix}_{i+1}.xlsx"
        chunk_df.to_excel(output_file, index=False)

        print(f"Chunk {i+1} saved to {output_file}")

    print("Splitting completed successfully.")

# Example usage
# You only need to change here to the name of your file
split_excel_file("excel_file.xlsx", "split", 50000)