import argparse

# Create an ArgumentParser object with a description of the program
parser = argparse.ArgumentParser(description='Testing parameters')

# Add two optional arguments to the parser
parser.add_argument("-p1", dest="param1", help="parameter1", required=True)
parser.add_argument("-p2", dest="param2", help="parameter2", required=True)

# Parse the command-line arguments and store them in a Namespace object
params = parser.parse_args()

# Print the values of the two parameters
print(params.param1)
print(params.param2)
