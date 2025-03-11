import csv

# Input / Output file 
input_file = 'security_incidents.csv'
output_file = 'security_incidents_modified.csv'

# Read the csv
with open(input_file, mode='r') as infile:
    reader = csv.reader(infile)
    data = list(reader)

# Create new column and a default value 
new_column_name = 'status'
default_value = 'pending'

# Adding new column to the header
header = data[0] + [new_column_name]

# Adding the new column to each row 
rows = [row + [default_value] for row in data[1:]]

# Writing the data to a new csv
with open(output_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Modified data saved to '{output_file}'")