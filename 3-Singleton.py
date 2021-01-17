
#******************************************************************************************************************#

# 3-Singleton.py

#******************************************************************************************************************#

# 2021-01-04 05:04:20

# This is the code used in '2-Understanding_Design_Patterns.txt'

class ConfigValues:

    # When class variable is preceeded with '__', it is a private variable.
    # This means it can't be accessed from outside the class.
    __instance = None

    # The decorator '@staticmethod' means the getInstance() method can be executed
    # even before instantiated an object of this class.
    @staticmethod
    def getInstance():

        # if __instance is blank, create a new instance.
        # The __instance will be blank on the first run.
        # On the second run, the __instance variable will not be empty,
        # thus this If-statement will not be executed.
        if ConfigValues.__instance == None:
            ConfigValues()
        return  ConfigValues.__instance

    # Initialize the object.
    # Note that this constructor prevents you from instantiating a new value 
    # for the instantiated object
    def __init__(self):
        """Virtually private constructor"""

        if ConfigValues.__instance != None:
            raise Exception("This class is a singleton")
        else:
            ConfigValues.__instance = self


# Creating the object

s = ConfigValues()                          # This will create the object 
print(s)

s = ConfigValues.getInstance()              # This can run without creating the object first.
print(s)                                    # Note that this will create version 2 - but both similar

s = ConfigValues.getInstance()              # Same here, this will create version 3 of s 
print(s)

# s = ConfigValues()                        # This will raise an exception "This class is a singleton" 
# print(s)                                  #  This is because this will create a 2nd copy of s

# r = ConfigValues()                        # This will raise an exception "This class is a singleton" 
# print(r)                                  #  This is because this will create a 2nd copy of s


# Test the code by running      python 3-Singleton.py
