import json

# Read the JSON data from the cb-test.txt file
with open('cb-test.txt', 'r') as file:
    # Use a generator expression to load each line as a JSON object
    data = [json.loads(line) for line in file]

# Print the first element and format the json output
# print(json.dumps(data[0], indent=4))

item_name = data[0]['item_name']
buyer_item_description = data[0]['buyer_item_description']
buyer_price = data[0]['buyer_price']
seller_item_description = data[0]['seller_item_description']
seller_price = data[0]['seller_price']
dialog = data[0]['dialog']

# for d in dialog:
#     print(d['speaker'], d['text'])

print('sample data: ', data[0])
