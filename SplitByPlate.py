import numpy as np
import pandas as pd
import glob

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

    unique_concentrations = np.unique(T['Concentration'])

    # Get the unique values in the 'PlateName' column
    unique_plate_names = np.unique(T['Plate Name'])

    # Loop through each unique plate name value
    for plate_name in unique_plate_names:
        num_rows_per_concentration = len(T[T['Plate Name'] == unique_plate_names[0][0]])
        output_data = pd.DataFrame(index=range(len(unique_concentrations) * num_rows_per_concentration + 2), columns=['Concentration'] + list(T['Drug Name'].unique()))

# Fill the first row with the headers
        output_data.iloc[0, 0] = 'Concentration'
        output_data.iloc[0, 1:] = T['Drug Name'].unique()


        # Get the rows of the table where the 'PlateName' column is equal to the current unique plate name
        plate_rows = T['Plate Name'] == plate_name

        # Find the rows where the Well column starts with 'N' and the Batch column is empty
        N_rows = T['Well'].apply(lambda x: str(x).startswith('N')) & T['Batch'].isnull()
        avg_Lum_values_missing = np.nanmean(T.loc[plate_rows & N_rows, 'Lum'])

        # Get the unique values in the 'DrugName' and 'Concentration' columns
        unique_drugs = T.loc[plate_rows, 'Drug Name'].unique()
        unique_concentrations = T.loc[plate_rows, 'Concentration'].unique()

        # Create an array to store the average Lum values
        Lum_values = np.empty((len(unique_concentrations), len(unique_drugs)))

        # Iterate over each unique concentration
        for i, concentration in enumerate(unique_concentrations):
        for j, drug in enumerate(unique_drugs):
        Lum_values[i, j] = lum_dict[(concentration, drug)]



                # Get the rows where the 'Drug Name' column matches the current unique drug
        drug_rows = T.loc[plate_rows, 'Drug Name'] == drug

                # Get the Lum values for the current drug and concentration
        slice_data = T.loc[plate_rows & concentration_rows & drug_rows, 'Lum']

        if not slice_data.empty:
                    Lum_values[i, j] = np.nanmean(slice_data)
        else:
                    Lum_values[i, j] = np.nan  # or any other appropriate value to handle the empty case

        # Fill the cells with the calculated average Lum values
        output_data.iloc[1:, 1:] = Lum_values


        for i, concentration in enumerate(unique_concentrations):
            for j, drug in enumerate(unique_drugs):
                output_data.at[1, drug] = avg_Lum_values_missing
                output_data.at[i + 2, drug] = Lum_values[i, j]

        # Define the output file name
        output_file = f"{output_folder}/{plate_name}_output.csv"

        # Replace NaN values with blanks
        output_data = output_data.fillna('')

        # Write the output data to a CSV file
        output_data.to_csv(output_file, index=False)

        # Print a message indicating that the output file has been created
        print(f"Output file '{output_file}' created")

# Print a message indicating that the script has finished running
print('Script finished running')
