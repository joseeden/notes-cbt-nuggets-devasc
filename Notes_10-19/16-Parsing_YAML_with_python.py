
#******************************************************************************************************************#

# 16-Parsing_YAML_with_python

#******************************************************************************************************************#

# 2021-01-08 03:51:56

# By specifications, YAML is considered a superset of JSON.
# Here we\ll use '10-Sample.yaml' which is in the same directory.
# Recall hat you have to install YAML first before using it - it's not built-in with Python.
# To install yaml:      python -m pip install pyyaml

#------------------------------------------------START OF CODE----------------------------------------------------#

import yaml
from yaml import load, load_all

# load      - If we ahve a single YAML odcument in a single file, we can use 'load'
# loadall   - if there are multiple YAML documents in a single file, we can use 'loadall'
# Note that if there are multiple documents and we use 'load', it'll just load the first document.
stream = open('10-Sample.yaml', 'r')
documents = load_all(stream, Loader=yaml.FullLoader)

# this will return a type=generator
print(type(documents))
print("")

# to dig in to the actual code, we can iterate.
# the prnit statement below will return a type=dictionary
# This is because each root is a dictionary. TO understand this, you can check out the yaml file
# that we're parsing - '10-Sample.yaml'
# In that file, the root is 'People' for the first document.
for doc in documents:
    print(type(doc))
#-------------------------------------------------END OF CODE----------------------------------------------------#
