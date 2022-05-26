# File content before editing
# 4707025628 Par Ernst Jeffery 307 Delores St Colquitt, Georgia(GA)
# 5453303457 Robert Xulio David 626 Anderson Rd Duluth, Minnesota(MN)
# 9232815509 Gani Frigyes Ovidiu 205 Chappin St Chadbourn, North Carolina(NC)
# 6755990433 Frens Pierpaolo Goemon 46934 Blue Spruce St Tea, South Dakota(SD)
# 4322680564 Afon Kire Micaiah 1101 Twin Laurel Blvd Nokomis, Florida(FL)
# 5546157441 Stojan Aldo Adao 700 N Alanthus Ave Stanberry, Missouri(MO)
# 9576357908 Nasim Hjortur Juraj 1978 County 381 Rd Wewahitchka, Florida(FL)
# 5683979587 Jimeno Raphael Wulfric 405 N Apsco Ln Cottonwood, Arizona(AZ)

cfile = open("file_edit.txt", "r+")
cfile.seek(0)
x = cfile.readlines()
cfile.seek(0)
print(x)

phone_numbers = []
for i in x:
    phone_numbers.append(i.split()[0]) # getting phone numbers in a list
print(phone_numbers)

# Eliminating bug creating situation by adding \n to last line if it doesn't have one
if "\n" not in x[len(x)-1]:
    x[len(x) - 1] = x[len(x)-1] + "\n"

# Sorting
while True:
    counter = 0
    for i in range(len(phone_numbers)-1):
        if phone_numbers[i] > phone_numbers[i+1]:
            phone_numbers[i], phone_numbers[i+1] = phone_numbers[i+1], phone_numbers[i]
            x[i], x[i+1] = x[i+1], x[i]
            counter = 1
    if counter == 0:
        break
x = "".join(x) # Gluing the list into 1 string
cfile.write(x) # Rewriting the file in sorted order

cfile.seek(0)
print(cfile.read())

# File content after editing
# 4322680564 Afon Kire Micaiah 1101 Twin Laurel Blvd Nokomis, Florida(FL)
# 4707025628 Par Ernst Jeffery 307 Delores St Colquitt, Georgia(GA)
# 5453303457 Robert Xulio David 626 Anderson Rd Duluth, Minnesota(MN)
# 5546157441 Stojan Aldo Adao 700 N Alanthus Ave Stanberry, Missouri(MO)
# 5683979587 Jimeno Raphael Wulfric 405 N Apsco Ln Cottonwood, Arizona(AZ)
# 6755990433 Frens Pierpaolo Goemon 46934 Blue Spruce St Tea, South Dakota(SD)
# 9232815509 Gani Frigyes Ovidiu 205 Chappin St Chadbourn, North Carolina(NC)
# 9576357908 Nasim Hjortur Juraj 1978 County 381 Rd Wewahitchka, Florida(FL)