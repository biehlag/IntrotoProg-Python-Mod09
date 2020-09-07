# -----------------------------------------------------------#
# Title: TestHarness.py
# Description: A script to run and test the other modules to make sure the are working
# ChangeLog:
#   Austin Biehl, 09.03.2020, Import Person, Processing, Data, and IO classes
# ---------------------------------------------------------- #
# Harness script begins
#
if __name__ == "__main__":
    from DataClasses import Person as P
    from DataClasses import Employee as EMP
    from ProcessingClasses import FileProcessor as FP
    from IOClasses import EmployeeIO as EIO
else:
    raise Exception("This file was not created to be imported")

# Test reading PersonData.txt
lstFileData = FP.read_data_from_file("PersonData.txt")
lstTable = []
for line in lstFileData:
    lstTable.append(P(line[0], line[1].strip()))
for row in lstTable:
    print(row.to_string())

# Test writing to PersonData.txt
FP.save_data_to_file("PersonData.txt", lstTable)
lstFileData = FP.read_data_from_file("PersonData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(P(line[0], line[1].strip()))
for row in lstTable:
    print(row.to_string())
#
# Test Employee class

lstFileData = FP.read_data_from_file("EmployeeData.txt")
lstTable = []
for line in lstFileData:
    lstTable.append(EMP(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

# Test writing to PersonData.txt
FP.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = FP.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(EMP(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string())

# Test IO class
cont = True
while cont == True:
    EIO.print_menu_items()
    strChoice = EIO.input_menu_options()
    if strChoice == "1":
        for row in lstTable:
            print(row.to_string())
    elif strChoice == "2":
        EmpInput = []
        EmpInput = EIO.input_employee_data()
        lstTable.append(EmpInput)
        for row in lstTable:
            print(row.to_string())
    elif strChoice == "3":
        FP.save_data_to_file("EmployeeData.txt",lstTable)
        print("Data was saved to file")
    elif strChoice == "4":
        cont = False
        print("Goodbye")
exit()
