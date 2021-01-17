
#******************************************************************************************************************#

# 15-Parsing_JSON_with_python

#******************************************************************************************************************#

# 2021-01-08 03:17:38

# Note that JSON is a  builtin library - no need to install it.
# If you have  python installed, JSON comes with it.

#------------------------------------------------START OF CODE----------------------------------------------------#

import json

# This is the smae with the the file '9-Sample_valid.json' that is in the same directory.
# But here is is a type=string
jsonstr = """
          {"people":[
          {"id":"1", "FirstName":"John", "LastName":"Smith", "Email":"john.smith@yahoo.com"},
          {"id":"2", "FirstName":"Jane", "LastName":"Doe", "Email":"jane.doe@yahoo.com"},
          {"id":"3", "FirstName":"Jeff", "LastName":"Park", "Email":"jeff.park@yahoo.com"}
          ]}
          """

jsonobj = json.loads(jsonstr)
print(jsonobj)
print("")

# JSON detects that the first character is a '{' so this returns a type=dictionary
print(type(jsonobj))
print("")

# JSON detects the character after 'people' which is a'[' so this returns a type=list
print(type(jsonobj["people"]))
print("")

# Returns the index=1 of the list. Recall that the index numbering is 0,1,2....
print(jsonobj['people'][1])
print("")
print(jsonobj['people'][2])
print("")

#--------------------------------------------------------------------------------------

# We can also read froma  file. Note here that we're using 'load'
# We'll read from '9-Sample_valid.json' which is in the same directory.
samplefile = open('9-Sample_valid.json')
jsonobj2 = json.load(samplefile)

print(jsonobj2['People'])

#-------------------------------------------------END OF CODE----------------------------------------------------#

