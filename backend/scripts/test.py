import json

# Specify the path to your JSON file
json_file_path = "data/medicines.json"

# Load the JSON file
with open(json_file_path, "r") as file:
    datas = json.load(file)

datas = [
    {**data, "price": float(data["price"].replace("Rs.", "").replace(",", ""))}
    for data in datas
]

# Save the modified JSON back to the file
with open(json_file_path, "w") as file:
    json.dump(datas, file)
