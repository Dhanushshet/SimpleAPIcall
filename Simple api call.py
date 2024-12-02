import requests  # This is like a phone to call the API.

# Step 1: Make the API call to fetch data.
def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"  # API that gives us some fake posts.
    response = requests.get(url)  # "Hello API, can you give me the posts?"

    if response.status_code == 200:  # 200 means the API answered, "Sure, here you go!"
        print("Data fetched successfully!")
        return response.json()  # API gives us the data in JSON format (like a dictionary).
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []

# Step 2: Filter posts based on a condition (e.g., title length greater than 20 characters).
def filter_posts(posts):
    print("\nFiltering posts with titles longer than 20 characters...\n")
    filtered_posts = [post for post in posts if len(post['title']) > 20]
    return filtered_posts

# Step 3: Save filtered posts to a file (useful for data engineering to keep records).
def save_to_file(data, filename="filtered_posts.json"):
    import json
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Filtered posts saved to {filename}")

# Main function to tie everything together.
if __name__ == "__main__":
    print("Starting the process...\n")

    # Fetch data
    posts = fetch_data()

    if posts:
        # Filter the data
        filtered = filter_posts(posts)

        # Show a summary of filtered data
        print(f"Found {len(filtered)} posts with long titles.")

        # Save the filtered data
        save_to_file(filtered)
