import re


pattern = r'^#[0-9a-fA-F]{6}$'

z = input(" Please Enter any hex color codes\n")


if re.match(pattern, z):
    print(z)
else:
    print("try again")
