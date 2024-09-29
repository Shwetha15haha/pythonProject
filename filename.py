# Initialize a list of filenames
filenames = ["1.Raw Data.txt", "2.Processed data.txt", "3.Reports.txt"]

# Print the original list of filenames
print(filenames)

# Initialize an empty list to store the new filenames
new_filenames = []

# Iterate over each filename in the original list
for filename in filenames:
    # Replace the first occurrence of '.' with '-' in the filename
    new_filename = filename.replace('.', '-', 1)
    # Print the modified filename
    print(new_filename)
    # Append the modified filename to the new_filenames list
    new_filenames.append(new_filename)

# Update the original filenames list with the new filenames
filenames = new_filenames

# Print the updated list of filenames
print(filenames)

# output :
# ['1.Raw Data.txt', '2.Processed data.txt', '3.Reports.txt']
# 1-Raw Data.txt
# 2-Processed data.txt
# 3-Reports.txt
# ['1-Raw Data.txt', '2-Processed data.txt', '3-Reports.txt']