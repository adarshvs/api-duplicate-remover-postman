import json

# Load the collection from a JSON file
with open("collection.json") as f:
    collection = json.load(f)

# Create an empty list to store unique URLs
unique_urls = []

# Get the count of requests in the original collection
original_count = len(collection["item"])

# Iterate over each request in the collection
for item in collection["item"]:
    # Get the URL of the request
    url = item["request"]["url"]

    # Check if the URL is already in the unique_urls list
    if url not in unique_urls:
        # If it is not, add it to the list
        unique_urls.append(url)
    else:
        collection["item"].remove(item)

# Get the count of requests in the updated collection
updated_count = len(collection["item"])

# Calculate the number of duplicates removed
duplicates_removed = original_count - updated_count

# Print the number of duplicates removed
print(f"{duplicates_removed} duplicate(s) removed from the collection.")


with open("new.json", "w") as f:
    json.dump(collection, f, indent=4)
