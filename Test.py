import numpy as np
import pandas as pd
import glob
import os

# Define the paths to the input and output folders
input_folder = r'C:\Users\oma4008\OneDrive - med.cornell.edu\Desktop\Data Analysis\Manish\Input Python'
output_folder = r'C:\Users\oma4008\OneDrive - med.cornell.edu\Desktop\Data Analysis\Manish\Output2'

# Use the glob function to get a list of files in the input folder with the extension '.xlsx'
files = glob.glob(input_folder + '/*.xlsx')

# Loop through each file in the input folder
for file in files:
    # Read the current file into a pandas DataFrame
    T = pd.read_excel(file)
    
    # Flip the rows of the DataFrame
    T.iloc[151:281, :] = np.flipud(T.iloc[151:281, :])
    T.iloc[431:561, :] = np.flipud(T.iloc[431:561, :])
    T.iloc[711:841, :] = np.flipud(T.iloc[711:841, :])
    T.iloc[991:1121, :] = np.flipud(T.iloc[991:1121, :])
    T.iloc[1271:1401, :] = np.flipud(T.iloc[1271:1401, :])
    T.iloc[1551:1681, :] = np.flipud(T.iloc[1551:1681, :])
    
    # Replace values in the 'Concentration' column that meet the specified conditions
    T['Concentration'] = np.where(T['Concentration'] == 1.111, 1.1111, T['Concentration'])
    T['Concentration'] = np.where(T['Concentration'] == 3.333333333, 3.333, T['Concentration'])

    # Get the unique values in the 'PlateName' column
    unique_plate_names = np.unique(T['Plate Name'], return_index=True, return_inverse=True, return_counts=True)

    # Create a DataFrame to store the output data
    output_data = pd.DataFrame(index=range(len(unique_plate_names[0]) * 2 + 2), columns=range(len(T['Drug Name'].unique()) + 1))

    # Fill the first row with the headers
    output_data.iloc[0, 0] = 'Concentration'
    output_data.iloc[0, 1:] = T['Drug Name'].unique()

    # Loop through each unique plate name value
    for j in range(len(unique_plate_names[0])):
        # Get the rows of the table where the 'PlateName' column is equal to the current unique plate name
        plate_rows = T['Plate Name'] == unique_plate_names[0][j]
        # Find the rows where the Well column starts with 'N' and the Batch column is empty
        N_rows = T['Well'].apply(lambda x: str(x).startswith('N')) & T['Batch'].isnull()
        avg_Lum_values_missing = np.nanmean(T.loc[N_rows, 'Lum'])

        # Get the unique values in the 'DrugName' and 'Concentration' columns
        unique_drugs = T.loc[plate_rows, 'Drug Name'].unique()
        unique_concentrations = T.loc[plate_rows, 'Concentration'].unique()

        # Create an array to store the average Lum values
        Lum_values = np.empty((len(unique_concentrations), len(unique_drugs)))

        # Iterate over each unique concentration
        for k, concentration in enumerate(unique_concentrations):
            # Get the rows where the 'Concentration' column matches the current unique concentration
            concentration_rows = T.loc[plate_rows, 'Concentration'].fillna('').eq(concentration).values.reshape(-1, 1)

            # Iterate over each unique drug
            for l, drug in enumerate(unique_drugs):
                # Get the rows where the 'Drug Name' column matches the current unique drug
                drug_rows = T.loc[plate_rows, 'Drug Name'].fillna('').eq(drug).values.reshape(1, -1)
                num_rows_per_concentration = len(drug_rows[0]) // len(concentration_rows)
                slice_data = T[T['Concentration'].isin(concentration_rows.flatten()) & T['Drug Name'].isin(drug_rows.flatten())]['Lum']

    if not slice_data.empty:
                Lum_values[k, l] = np.nanmean(slice_data)
    else:
                Lum_values[k, l] = np.nan  # or any other appropriate value to handle the empty case

    # Fill the cells with the calculated average Lum values
    row_start = j * 2 + 2
    output_data.iloc[row_start, 0] = 'Average Background Normalization Value'
    output_data.iloc[row_start, 1:len(unique_drugs) + 1] = avg_Lum_values_missing
    output_data.loc[row_start + 1:, 'Concentration'] = np.repeat(unique_concentrations, num_rows_per_concentration)[:len(output_data)-row_start-1]
    for i, concentration in enumerate(unique_concentrations):
        for j, drug in enumerate(unique_drugs):
            output_data.at[row_start + i + 1, drug] = Lum_values[i, j]

    # Define the output file name
    plate_name = os.path.splitext(os.path.basename(file))[0]
    output_file = f"{output_folder}/{plate_name}_output.csv"
     # Replace NaN values with blanks
    output_data = output_data.fillna('')

    # Write the output data to a CSV file
    output_data.to_csv(output_file, index=False)

    # Print a message indicating that the output file has been created
    print(f"Output file '{output_file}' created")

# Print a message indicating that the script has finished running
print('Script finished running')