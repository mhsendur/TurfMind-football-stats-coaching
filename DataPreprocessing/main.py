import os
import pandas as pd


# Define the path to the folder containing club data
data_folder = './DataPreprocessing-TurfMind/club_data'

# Create a folder to store the cleaned club data
cleaned_data_folder = './DataPreprocessing-TurfMind/cleaned_club_data'
os.makedirs(cleaned_data_folder, exist_ok=True)


# Function to preprocess a CSV file and detect changes
def preprocess_csv(file_path):
    # Load the CSV file into a Pandas DataFrame
    original_df = pd.read_csv(file_path)

    # Create a copy of the original DataFrame for comparison
    original_copy = original_df.copy()

    # Standardise column names (convert to lowercase and remove spaces)
    original_df.columns = original_df.columns.str.lower().str.replace(' ', '_')

    # Convert date column to datetime data type
    original_df['date'] = pd.to_datetime(original_df['date'])

    # Round numeric columns to three decimal places
    numeric_columns = original_df.select_dtypes(include=['number'])
    original_df[numeric_columns.columns] = numeric_columns.round(3)

    # Additional preprocessing steps

    # Check if anything was changed
    if not original_df.equals(original_copy):
        print(f"Changes detected in: {file_path}")

    return original_df


# Process each CSV file in the data folder
for file_name in os.listdir(data_folder):
    file_path = os.path.join(data_folder, file_name)

    if file_path.lower().endswith('.csv'):
        print(f"Processing CSV file: {file_name}")
        cleaned_df = preprocess_csv(file_path)

        cleaned_file_path = os.path.join(cleaned_data_folder, file_name)
        cleaned_df.to_csv(cleaned_file_path, index=False)

print("Data preprocessing and cleaning completed.")

# Define the input and output folder paths
input_folder = "./DataPreprocessing-TurfMind/player_data"
output_folder = "./DataPreprocessing-TurfMind/cleaned_player_data"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)


# Function to preprocess a CSV file
def preprocess_csv_file(input_path, output_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_path)

    # Handling missing data
    df.fillna(0, inplace=True)  # Fill missing values with 0 for numerical columns

    # Standardise column names (convert to lowercase, remove spaces and special characters)
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('.', '')

    # Rename specified columns
    column_renames = {
        'unnamed:_0_level_0_player': 'player',
        'unnamed:_1_level_0_nation': 'player_nation',
        'unnamed:_2_level_0_pos': 'player_position',
        'unnamed:_3_level_0_age': 'player_age',
        'unnamed:_4_level_0_mp': 'mp',
        'unnamed:_24_level_0_matches': 'matches'
    }
    df.rename(columns=column_renames, inplace=True)


    # Convert data types

    # Remove columns starting from "expected_xg" to the last column with only 0.0 values
    last_non_zero_column = df.columns.get_loc('expected_xg') - 1
    df = df.iloc[:, :last_non_zero_column + 1]

    # Save the cleaned data to the output folder
    df.to_csv(output_path, index=False)


# Traverse through season and league folders
for season_folder in os.listdir(input_folder):
    season_path = os.path.join(input_folder, season_folder)
    if not os.path.isdir(season_path):
        continue

    for league_folder in os.listdir(season_path):
        league_path = os.path.join(season_path, league_folder)
        if not os.path.isdir(league_path):
            continue

        # Process all "standard_stats" CSV files in the league folder
        for filename in os.listdir(league_path):
            if filename.startswith("standard_stats") and filename.endswith(".csv"):
                input_file = os.path.join(league_path, filename)
                output_file = os.path.join(output_folder, season_folder, league_folder, filename)
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                preprocess_csv_file(input_file, output_file)

print("Data preprocessing completed.")
