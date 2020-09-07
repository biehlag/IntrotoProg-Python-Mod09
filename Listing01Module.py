# ---------------------------------------------------------- #
# Title: Listing01Module
# Description: Components of a typical module
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #

def standalone_function():
    print("Called standalone_function")

class MyData:
    def __init__(self):
        print("Created MyData object")

class FileProcessor:

    @staticmethod
    def process_data():
        print("Called process_data")

class IO:

    @staticmethod
    def print_data():
        print("Called print_data")

