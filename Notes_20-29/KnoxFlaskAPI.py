
#**********************************************************************************************************************#

# KnoxFlaskAPI.py

#**********************************************************************************************************************#

# 2021-01-15 17:44:10

# EDEN:
# This is the code for the flask API used in Knox Hutchinson's docker section in the CBT Nuggets - DevAsc course.
# You can check out the code here: https://github.com/DataKnox/CodeSamples/blob/master/Python/Docker/myAPI/myAPI.py

# Note that you'll have to install flask on your machine first, before you can run the code below.
# For installing flask, you can follow this tutorial: https://code.visualstudio.com/docs/python/tutorial-flask

#-------------------------------------------------START OF CODE------------------------------------------------------#

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/endpoint', methods=['GET'])
def get_data():
    return (jsonify({'message': 'received'}), 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

#---------------------------------------------------END OF CODE------------------------------------------------------#

# To test if script worked, run the following commands:

#**********************************************************************************************************************#
