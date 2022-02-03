import sys
with open(sys.argv[1], "r") as f:
	content_1 = f.read()

with open(sys.argv[2], "r") as f:
	content_2 = f.read()

# Content of a .csv file ends with a "\n" so a trailing empty string is produced by split()
# The header and the trailing empty string should not be included
content_1 = content_1.split("\n")[1:-1]
content_2 = content_2.split("\n")[1:-1]

# Only the file name should be included
file_1_name = sys.argv[1].split("/")[-1]
file_2_name = sys.argv[2].split("/")[-1]

# stdout of the header
print("email_hash,category,filename") 

# Create an empty string to collect each line of input csv files
output = ""
# Concatenate the file names to the end of each line with a new line
for c1 in content_1:
	output += c1 + "," + file_1_name + "\n"
# stdout of the first csv file
print(output, end="")

# Repeat the same process for the second csv file
output = ""
for c2 in content_2:
	output += c2 + "," + file_2_name + "\n"

print(output, end="")