import numpy as np
import pandas as pd
import glob

# Define the paths to the input and output folders
input_folder = r'C:\Users\oma4008\OneDrive - med.cornell.edu\Desktop\Data Analysis\Manish\Input Python'
output_folder = r'C:\Users\oma4008\OneDrive - med.cornell.edu\Desktop\Data Analysis\Manish\Output2'

# Use the glob function to get a list of files in the input folder with the extension '.xlsx'
files: list[str] = glob.glob(pathname=input_folder + '/*.xlsx')

# Loop through each file in the input folder
for file in files:
    # Read the current file into a pandas DataFrame
    T: pd.DataFrame = pd.read_excel(io=file)
    
    # Flip the rows of the DataFrame
    T.iloc[151:281, :] = np.flipud(m=T.iloc[151:281, :])
    T.iloc[431:561, :] = np.flipud(m=T.iloc[431:561, :])
    T.iloc[711:841, :] = np.flipud(m=T.iloc[711:841, :])
    T.iloc[991:1121, :] = np.flipud(m=T.iloc[991:1121, :])
    T.iloc[1271:1401, :] = np.flipud(m=T.iloc[1271:1401, :])
    T.iloc[1551:1681, :] = np.flipud(m=T.iloc[1551:1681, :])
    
    # Replace values in the 'Concentration' column that meet the specified conditions
    T['Concentration'] = np.where(T['Concentration'] == 1.111, 1.1111, T['Concentration'])
    T['Concentration'] = np.where(T['Concentration'] == 3.333333333, 3.333, T['Concentration'])

print(T.columns)

    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
        if T.Concentration.iloc[n] == 1.111:
            T.Concentration[n] = 1.1111
    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
        if T.Concentration.iloc[n] == 3.333333333:
            T.Concentration[n] = 3.333
    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
       if T.Concentration.iloc[n] == 10 and (T.Concentration.iloc[n - 9] == 0.000508053 or T.Concentration.iloc[n - 9] == 0.000508052634252908 or T.Concentration.iloc[n - 9] == 0.000508 or T.Concentration.iloc[n - 9] == 0.00050805) and (T.Concentration.iloc[n - 1] == 3.333 or T.Concentration.iloc[n - 1] == 3.333333333) and not np.isnan(T.Lum.iloc[n]) and not np.isnan(T.Lum.iloc[n - 1]):
          T.loc[np.arange(n - 9, n - 1 + 1), 'Concentration'] = np.array([0.000508053, 0.001524158, 0.004572474, 0.013717421, 0.041152263, 0.1234679, 0.37037037, 1.111111111, 3.333333333])
          T.loc[n, 'Concentration'] = 10

#     # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
# for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
#         if T.Concentration.iloc[n] == 30 and (T.Concentration(n - 1) == 10 and (T.Concentration(n - 9) != 0.000508 or T.Concentration(n - 9) != 0.000508053 and T.Concentration(n - 9) != 0.000508052634252908) and not np.isnan(T.Lum[n])  and not np.isnan(T.Lum[n - 1]) :
#             T.Concentration[n - 9] = 0.00152401
#             T.Concentration[n - 8] = 0.00457201
#             T.Concentration[n - 7] = 0.01371701
#             T.Concentration[n - 6] = 0.04115201
#             T.Concentration[n - 5] = 0.1234601
#             T.Concentration[n - 4] = 0.3703701
#             T.Concentration[n - 3] = 1.111101
#             T.Concentration[n - 2] = 3.33301
#             T.Concentration[n - 1] = 10.01
#             T.Concentration[n] = 30
#     # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
# for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
#         if T.Concentration.iloc[n] == 1 and T.Concentration(n - 1) == 0.333333333 and (T.Concentration(n - 9) == 5.08053e-05 or T.Concentration(n - 9) == 5.08e-05) and T.Concentration(n - 8) == 0.000152416 and not np.isnan(T.Lum[n])  and not np.isnan(T.Lum[n - 1]) :
#             T.Concentration[n - 9] = 5.08053e-05
#             T.Concentration[n - 8] = 0.000152416
#             T.Concentration[n - 7] = 0.0004572
#             T.Concentration[n - 6] = 0.0013717
#             T.Concentration[n - 5] = 0.0041152
#             T.Concentration[n - 4] = 0.012346
#             T.Concentration[n - 3] = 0.037037
#             T.Concentration[n - 2] = 0.111
#             T.Concentration[n - 1] = 0.333
#             T.Concentration[n] = 1
#     # Check order
# # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
# for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
#         if T.Concentration.iloc[n] == 0.03 and T.Concentration(n - 1) == 0.01 and not np.isnan(T.Lum[n])  and not np.isnan(T.Lum[n - 1]) :
#             T.Concentration[n - 9] = 1.52e-06
#             T.Concentration[n - 8] = 4.57e-06
#             T.Concentration[n - 7] = 1.37e-05
#             T.Concentration[n - 6] = 4.12e-05
#             T.Concentration[n - 5] = 0.000123457
#             T.Concentration[n - 4] = 0.00037037
#             T.Concentration[n - 3] = 0.001111111
#             T.Concentration[n - 2] = 0.003333333
#             T.Concentration[n - 1] = 0.01
#             T.Concentration[n] = 0.03
#     # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
# for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
#         if T.Concentration.iloc[n] == 0.1 and (T.Concentration(n - 1) == 0.03333333 or T.Concentration(n - 1) == 0.033333333) and T.Concentration(n - 9) == 5.08053e-06 and not np.isnan(T.Lum[n])  and not np.isnan(T.Lum[n - 1]) :
#             T.Concentration[n - 9] = 5.08053e-06
#             T.Concentration[n - 8] = 1.52416e-05
#             T.Concentration[n - 7] = 4.57247e-05
#             T.Concentration[n - 6] = 0.000137174
#             T.Concentration[n - 5] = 0.000411523
#             T.Concentration[n - 4] = 0.001234568
#             T.Concentration[n - 3] = 0.003703704
#             T.Concentration[n - 2] = 0.011111111
#             T.Concentration[n - 1] = 0.03333333
#             T.Concentration[n] = 0.1
#     # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
# for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
#         if T.Concentration.iloc[n] == 6 and T.Concentration(n - 1) == 2 and T.Concentration(n - 9) == 0.000304832 and not np.isnan(T.Lum[n])  and not np.isnan(T.Lum[n - 1]) :
#             T.Concentration[n] = 6
#             T.Concentration[n - 1] = 2
#             T.Concentration[n - 2] = 0.666666667
#             T.Concentration[n - 3] = 0.222222222
#             T.Concentration[n - 4] = 0.074074074
#             T.Concentration[n - 5] = 0.024691358
#             T.Concentration[n - 6] = 0.008230453
#             T.Concentration[n - 7] = 0.002743484
#             T.Concentration[n - 8] = 0.000914495
#             T.Concentration[n - 9] = 0.000304832
#     # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
# for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
#         if T.Concentration.iloc[n] == 3 and T.Concentration(n - 1) == 1 and (T.Concentration(n - 9) == 0.000152416 or T.Concentration(n - 9) == 0.0001524) and not np.isnan(T.Lum[n])  and not np.isnan(T.Lum[n - 1])  and (T.Concentration(n - 9) != 5.08e-05):
#             T.Concentration[n - 9] = 0.00015242
#             T.Concentration[n - 8] = 0.000457247
#             T.Concentration[n - 7] = 0.001371742
#             T.Concentration[n - 6] = 0.004115226
#             T.Concentration[n - 5] = 0.012345679
#             T.Concentration[n - 4] = 0.037037037
#             T.Concentration[n - 3] = 0.111111111
#             T.Concentration[n - 2] = 0.333333333
#             T.Concentration[n - 1] = 1.01
#             T.Concentration[n] = 3
#     # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
# for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
#         if T.Concentration.iloc[n] == 3 and T.Concentration(n - 1) == 1 and T.Concentration(n - 9) == 0.000152415790275873 and not np.isnan(T.Lum[n])  and not np.isnan(T.Lum[n - 1])  and (T.Concentration(n - 9) != 5.08e-05):
#             T.Concentration[n - 9] = 0.0001524201
#             T.Concentration[n - 8] = 0.00045724701
#             T.Concentration[n - 7] = 0.00137174201
#             T.Concentration[n - 6] = 0.00411522601
#             T.Concentration[n - 5] = 0.01234567901
#             T.Concentration[n - 4] = 0.03703703701
#             T.Concentration[n - 3] = 0.11111111101
#             T.Concentration[n - 2] = 0.33333333301
#             T.Concentration[n - 1] = 1.01
#             T.Concentration[n] = 3
    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
        if T.Concentration.iloc[n] == 0.12345679:
            T.Concentration[n] = 0.1234679
 # Get the unique values in the 'PlateName' column
unique_plate_names = np.unique(T['Plate Name'], return_index=True, return_inverse=True, return_counts=True)

# Loop through each unique plate name value
for j in range(len(unique_plate_names[0])):
    # Get the rows of the table where the 'PlateName' column is equal to the current unique plate name
    plate_rows = T['Plate Name'] == unique_plate_names[0][j]
    # Find the rows where the Well column starts with 'N' and the Batch column is empty
    N_rows = T['Well'].apply(lambda x: str(x).startswith('N')) & T['Batch'].isnull()
    avg_Lum_values_missing = np.nanmean(T.loc[N_rows, 'Lum'])

    # Get the unique values in the 'DrugName' and 'Concentration' columns
    unique_drugs = T['Drug Name'].unique()
    unique_concentrations = T['Concentration'].unique()
    Lum_values = np.full((len(unique_concentrations), len(unique_drugs)), np.nan)

    # Loop through each unique concentration value and get the Lum value for each unique drug
    for k, concentration in enumerate(unique_concentrations):
        concentration_rows = T['Concentration'] == concentration
        for l, drug in enumerate(unique_drugs):
            drug_rows = T['Drug Name'] == drug
            slice_data = T.loc[np.logical_and(concentration_rows, drug_rows), 'Lum']
if not slice_data.empty:
    Lum_values[k, l] = np.nanmean(slice_data)
else:
    Lum_values[k, l] = np.nan  # or any other appropriate value to handle the empty case

# Create a DataFrame to store the output data
output_data = pd.DataFrame(index=range(len(unique_concentrations) + 2), columns=range(len(unique_drugs) + 1))

# Fill the first row with the headers
output_data.iloc[0, 0] = 'Concentration'
output_data.iloc[0, 1:] = unique_drugs

# Fill the second row with the header 'Average Background Normalization Value' and the calculated average Lum values
output_data.iloc[1, 0] = 'Average Background Normalization Value'
output_data.iloc[1, 1:] = avg_Lum_values_missing

# Fill the remaining cells with the calculated average Lum values
output_data.iloc[2:, 0] = unique_concentrations
output_data.iloc[2:, 1:] = Lum_values

# Add an empty row after every 10 rows of data
for f in range(2, min(output_data.shape[0], 200), 12):
   output_data = pd.concat([output_data, pd.Series()], ignore_index=True)

# Define the output file name
output_file = 'output_file.csv'

# Replace NaN values with blanks
output_data = output_data.fillna('')

# Write the output data to a CSV file
output_data.to_csv(output_file, index=False)

# Print a message indicating that the output file has been created
print(f"Output file '{output_file}' created")

# Print a message indicating that the script has finished running
print('Script finished running')
