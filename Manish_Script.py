import numpy as np
from numpy.lib.twodim_base import flipud
clear
# Define the paths to the input and output folders
input_folder = 'C:\Users\oma4008\OneDrive - med.cornell.edu\Desktop\Data Analysis\Manish\Input Python'
output_folder = 'C:\Users\oma4008\OneDrive - med.cornell.edu\Desktop\Data Analysis\Manish\Output'
# Use the dir function to get a list of files in the input folder with the extension '.csv'.
files = dir(fullfile(input_folder,'*.xlsx'))
# Set the format specifier for displaying numerical values
#format_specifier = '#0.3f';

# Loop through each file in the input folder.
for i in np.arange(1,len(files)+1).reshape(-1):
    # Read the current file into a table using readtable function
    T = readtable(fullfile(input_folder,files(i).name))
# Flip the rows of the table from row to row
T[np.arange(151, 280+1), :] = np.flipud(T[np.arange(151, 280+1), :])
T[np.arange(431, 560+1), :] = np.flipud(T[np.arange(431, 560+1), :])
T[np.arange(711, 840+1), :] = np.flipud(T[np.arange(711, 840+1), :])
T[np.arange(991, 1120+1), :] = np.flipud(T[np.arange(991, 1120+1), :])
T[np.arange(1271, 1400+1), :] = np.flipud(T[np.arange(1271, 1400+1), :])
T[np.arange(1551, 1680+1), :] = np.flipud(T[np.arange(1551, 1680+1), :])

    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
        if T.Concentration(n) == 1.111:
            T.Concentration[n] = 1.1111
    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
        if T.Concentration(n) == 3.333333333:
            T.Concentration[n] = 3.333
    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
        if T.Concentration(n) == 10 and (T.Concentration(n - 9) == 0.000508053 or T.Concentration(n - 9) == 0.000508052634252908 or T.Concentration(n - 9) == 0.000508 or T.Concentration(n - 9) == 0.00050805) and (T.Concentration(n - 1) == 3.333 or T.Concentration(n - 1) == 3.333333333) and not np.isnan(T.Lum(n))  and not np.isnan(T.Lum(n - 1)) :
            T.Concentration[np.arange[n - 9,n - 1+1]] = np.array([0.000508053,0.001524158,0.004572474,0.013717421,0.041152263,0.1234679,0.37037037,1.111111111,3.333333333])
            T.Concentration[n] = 10
    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
        if T.Concentration(n) == 30 and T.Concentration(n - 1) == 10 and (T.Concentration(n - 9) != 0.000508 or T.Concentration(n - 9) != 0.000508053 and T.Concentration(n - 9) != 0.000508052634252908) and not np.isnan(T.Lum(n))  and not np.isnan(T.Lum(n - 1)) :
            T.Concentration[n - 9] = 0.00152401
            T.Concentration[n - 8] = 0.00457201
            T.Concentration[n - 7] = 0.01371701
            T.Concentration[n - 6] = 0.04115201
            T.Concentration[n - 5] = 0.1234601
            T.Concentration[n - 4] = 0.3703701
            T.Concentration[n - 3] = 1.111101
            T.Concentration[n - 2] = 3.33301
            T.Concentration[n - 1] = 10.01
            T.Concentration[n] = 30
    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
        if T.Concentration(n) == 1 and T.Concentration(n - 1) == 0.333333333 and (T.Concentration(n - 9) == 5.08053e-05 or T.Concentration(n - 9) == 5.08e-05) and T.Concentration(n - 8) == 0.000152416 and not np.isnan(T.Lum(n))  and not np.isnan(T.Lum(n - 1)) :
            T.Concentration[n - 9] = 5.08053e-05
            T.Concentration[n - 8] = 0.000152416
            T.Concentration[n - 7] = 0.0004572
            T.Concentration[n - 6] = 0.0013717
            T.Concentration[n - 5] = 0.0041152
            T.Concentration[n - 4] = 0.012346
            T.Concentration[n - 3] = 0.037037
            T.Concentration[n - 2] = 0.111
            T.Concentration[n - 1] = 0.333
            T.Concentration[n] = 1
    # Check order
# Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
        if T.Concentration(n) == 0.03 and T.Concentration(n - 1) == 0.01 and not np.isnan(T.Lum(n))  and not np.isnan(T.Lum(n - 1)) :
            T.Concentration[n - 9] = 1.52e-06
            T.Concentration[n - 8] = 4.57e-06
            T.Concentration[n - 7] = 1.37e-05
            T.Concentration[n - 6] = 4.12e-05
            T.Concentration[n - 5] = 0.000123457
            T.Concentration[n - 4] = 0.00037037
            T.Concentration[n - 3] = 0.001111111
            T.Concentration[n - 2] = 0.003333333
            T.Concentration[n - 1] = 0.01
            T.Concentration[n] = 0.03
    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
        if T.Concentration(n) == 0.1 and (T.Concentration(n - 1) == 0.03333333 or T.Concentration(n - 1) == 0.033333333) and T.Concentration(n - 9) == 5.08053e-06 and not np.isnan(T.Lum(n))  and not np.isnan(T.Lum(n - 1)) :
            T.Concentration[n - 9] = 5.08053e-06
            T.Concentration[n - 8] = 1.52416e-05
            T.Concentration[n - 7] = 4.57247e-05
            T.Concentration[n - 6] = 0.000137174
            T.Concentration[n - 5] = 0.000411523
            T.Concentration[n - 4] = 0.001234568
            T.Concentration[n - 3] = 0.003703704
            T.Concentration[n - 2] = 0.011111111
            T.Concentration[n - 1] = 0.03333333
            T.Concentration[n] = 0.1
    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
        if T.Concentration(n) == 6 and T.Concentration(n - 1) == 2 and T.Concentration(n - 9) == 0.000304832 and not np.isnan(T.Lum(n))  and not np.isnan(T.Lum(n - 1)) :
            T.Concentration[n] = 6
            T.Concentration[n - 1] = 2
            T.Concentration[n - 2] = 0.666666667
            T.Concentration[n - 3] = 0.222222222
            T.Concentration[n - 4] = 0.074074074
            T.Concentration[n - 5] = 0.024691358
            T.Concentration[n - 6] = 0.008230453
            T.Concentration[n - 7] = 0.002743484
            T.Concentration[n - 8] = 0.000914495
            T.Concentration[n - 9] = 0.000304832
    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
        if T.Concentration(n) == 3 and T.Concentration(n - 1) == 1 and (T.Concentration(n - 9) == 0.000152416 or T.Concentration(n - 9) == 0.0001524) and not np.isnan(T.Lum(n))  and not np.isnan(T.Lum(n - 1))  and (T.Concentration(n - 9) != 5.08e-05):
            T.Concentration[n - 9] = 0.00015242
            T.Concentration[n - 8] = 0.000457247
            T.Concentration[n - 7] = 0.001371742
            T.Concentration[n - 6] = 0.004115226
            T.Concentration[n - 5] = 0.012345679
            T.Concentration[n - 4] = 0.037037037
            T.Concentration[n - 3] = 0.111111111
            T.Concentration[n - 2] = 0.333333333
            T.Concentration[n - 1] = 1.01
            T.Concentration[n] = 3
    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
        if T.Concentration(n) == 3 and T.Concentration(n - 1) == 1 and T.Concentration(n - 9) == 0.000152415790275873 and not np.isnan(T.Lum(n))  and not np.isnan(T.Lum(n - 1))  and (T.Concentration(n - 9) != 5.08e-05):
            T.Concentration[n - 9] = 0.0001524201
            T.Concentration[n - 8] = 0.00045724701
            T.Concentration[n - 7] = 0.00137174201
            T.Concentration[n - 6] = 0.00411522601
            T.Concentration[n - 5] = 0.01234567901
            T.Concentration[n - 4] = 0.03703703701
            T.Concentration[n - 3] = 0.11111111101
            T.Concentration[n - 2] = 0.33333333301
            T.Concentration[n - 1] = 1.01
            T.Concentration[n] = 3
    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n in np.arange(1,np.asarray(T.Concentration).size - 1+1).reshape(-1):
        if T.Concentration(n) == 0.12345679:
            T.Concentration[n] = 0.1234679
    # Get the unique values in the 'PlateName' column using the unique function.
unique_plate_names = unique(T.PlateName,'stable')
    # Loop through each unique plate name value
for j in np.arange(1,len(unique_plate_names)+1).reshape(-1):
        # Get the rows of the table where the 'PlateName' column is equal to the current unique plate name
        plate_rows = str(T.PlateName) == str(unique_plate_names[j])
        # Find the rows where the Well column starts with 'N' and the Batch column is empty
        N_rows = np.logical_and(np.logical_and(startsWith(strtrim(T.Well),'N'),plate_rows),np.isnan(T.Batch))
        avg_Lum_values_missing = nanmean(T.Lum(N_rows))
        # Get the unique values in the 'DrugName' and 'Concentration' columns using the unique function.
        unique_drugs = unique(T.DrugName(plate_rows),'stable')
        unique_concentrations = unique(T.Concentration(plate_rows),'stable')
        Lum_values = np.full([len(unique_concentrations),len(unique_drugs)],np.nan)
        # Loop through each unique concentration value and get the Lum value for each unique drug.
        for k in np.arange(1,len(unique_concentrations)+1).reshape(-1):
            concentration_rows = np.logical_and((T.Concentration == unique_concentrations(k)),plate_rows)
            for l in np.arange(1,len(unique_drugs)+1).reshape(-1):
                drug_rows = np.logical_and(str(T.DrugName) == str(unique_drugs[l]),plate_rows)
                Lum_values[k,l] = mean(T.Lum(np.logical_and(concentration_rows,drug_rows)))
        # Create a cell array to store the output data
        output_data = cell(len(unique_concentrations) + 2,len(unique_drugs) + 1)
        # Fill the first row with the headers
        output_data[1,1] = np.array(['Concentration'])
        output_data[1,np.arange[2,end()+1]] = unique_drugs
        # Fill the second row with the header 'Average Lum Value' and the calculated average Lum values.
        output_data[2,np.arange[2,end()+1]] = num2cell(avg_Lum_values_missing)
        # Fill the second row with the header 'Average Lum Value'
        output_data[2,1] = np.array(['Average Background Normalization Value'])
        # Fill the remaining cells with the calculated average Lum values.
        output_data[np.arange[3,end()+1],1] = num2cell(unique_concentrations)
        output_data[np.arange[3,end()+1],np.arange[2,end()+1]] = num2cell(Lum_values)

# Add an empty row after every 10 rows of data
for f in np.arange(3, min(output_data.shape[1], 200) + 1).reshape(-1):
    if (f - 3) % 12 == 0 and f > 2:
        new_row = np.empty((1, output_data.shape[2]))
        output_data = np.vstack([
            output_data[np.arange(1, f), :],
            new_row,
            output_data[np.arange(f, output_data.shape[0]), :]
        ])

                #f = f + 2; # increase the index by 2 to take into account the newly added empty rows
        # Define the output file name based on the current plate name.
        output_file = fullfile(output_folder,strcat(unique_plate_names[j],'.csv'))
        # Replace NaN values with blanks
        nan_values = cellfun(isnan,output_data,'UniformOutput',False)
        nan_indices = cellfun(any,nan_values)
        output_data[nan_indices] = np.array([''])
        # Write the output data to a CSV file using the writematrix function.
        writecell(output_data,output_file)
        # Print a message indicating that the output file has been created.
        print('Output file %s created\n' % (output_file))

# Print a message indicating that the script has finished running.
print('Script finished running\n' % ())