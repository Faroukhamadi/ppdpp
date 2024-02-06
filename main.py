import json

# Read the JSON data from the cb-test.txt file
with open('cb-test.txt', 'r') as file:
    # Use a generator expression to load each line as a JSON object
    data = [json.loads(line) for line in file]

# Print the first element and format the json output
print(json.dumps(data[0], indent=4))
