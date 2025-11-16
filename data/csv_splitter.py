import pandas as pd
import os

# Settings
filename = "survey_results_public.csv"  # your CSV
output_folder = "data"  # folder to save split files
num_splits = 2  # split into 2 files

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read the entire CSV
df = pd.read_csv(filename)
total_rows = len(df)
split_size = total_rows // num_splits

# Split and save
for i in range(num_splits):
    start = i * split_size
    # Make sure the last split takes any leftover rows
    end = (i + 1) * split_size if i < num_splits - 1 else total_rows
    chunk = df.iloc[start:end]
    
    output_file = os.path.join(output_folder, f"survey_results_part{i+1}.csv")
    chunk.to_csv(output_file, index=False)
    print(f"Saved {output_file} with {len(chunk)} rows")