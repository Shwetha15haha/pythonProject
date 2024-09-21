filenames = ["1.Raw Data.txt", "2.Processed data.txt", "3.Reports.txt"]

print(filenames)
new_filenames = []
for filename in filenames:
    new_filename = filename.replace('.', '-', 1)
    print(new_filename)
    new_filenames.append(new_filename)

filenames = new_filenames
print(filenames)