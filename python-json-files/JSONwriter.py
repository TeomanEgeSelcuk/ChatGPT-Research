import json
import os

# Variables
DB = "Openstax Calculus Volume 2"
collections = "Section 5.2 Infinite Series"

# Check if DB.json file exists
if os.path.isfile(f"{DB}.json"):
    # Read existing data from DB.json
    with open(f"{DB}.json", "r") as file:
        existing_data = json.load(file)

    # Check if data.json file exists
    if os.path.isfile("data.json"):
        # Read sequences from data.json
        with open("data.json", "r") as file:
            data = json.load(file)

        # Get the existing sequences or an empty list
        existing_sequences = existing_data.get(collections, [])

        # Extract the sequences from data.json
        new_sequences = data.get("sequences", [])

        # Create a set of existing questions
        existing_questions = {seq.get("question", "") for seq in existing_sequences}

        # Filter out duplicate sequences from new_sequences
        unique_sequences = [seq for seq in new_sequences if seq.get("question", "") not in existing_questions]

        # Update collections with unique sequences
        existing_data[collections] += unique_sequences

        # Write updated data to DB.json
        with open(f"{DB}.json", "w") as file:
            json.dump(existing_data, file, indent=4)
    else:
        print("Error: data.json file not found.")
else:
    print(f"Error: {DB}.json file not found.")
