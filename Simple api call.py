{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Fr-FGqc0OrDa",
        "outputId": "65234ffc-7066-4dc9-bd47-d0df2ccf54da",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Starting the process...\n",
            "\n",
            "Data fetched successfully!\n",
            "\n",
            "Filtering posts with titles longer than 20 characters...\n",
            "\n",
            "Found 90 posts with long titles.\n",
            "Filtered posts saved to filtered_posts.json\n"
          ]
        }
      ],
      "source": [
        "import requests  # This is like a phone to call the API.\n",
        "\n",
        "# Step 1: Make the API call to fetch data.\n",
        "def fetch_data():\n",
        "    url = \"https://jsonplaceholder.typicode.com/posts\"  # API that gives us some fake posts.\n",
        "    response = requests.get(url)  # \"Hello API, can you give me the posts?\"\n",
        "\n",
        "    if response.status_code == 200:  # 200 means the API answered, \"Sure, here you go!\"\n",
        "        print(\"Data fetched successfully!\")\n",
        "        return response.json()  # API gives us the data in JSON format (like a dictionary).\n",
        "    else:\n",
        "        print(f\"Failed to fetch data. Status code: {response.status_code}\")\n",
        "        return []\n",
        "\n",
        "# Step 2: Filter posts based on a condition (e.g., title length greater than 20 characters).\n",
        "def filter_posts(posts):\n",
        "    print(\"\\nFiltering posts with titles longer than 20 characters...\\n\")\n",
        "    filtered_posts = [post for post in posts if len(post['title']) > 20]\n",
        "    return filtered_posts\n",
        "\n",
        "# Step 3: Save filtered posts to a file (useful for data engineering to keep records).\n",
        "def save_to_file(data, filename=\"filtered_posts.json\"):\n",
        "    import json\n",
        "    with open(filename, 'w') as file:\n",
        "        json.dump(data, file, indent=4)\n",
        "    print(f\"Filtered posts saved to {filename}\")\n",
        "\n",
        "# Main function to tie everything together.\n",
        "if __name__ == \"__main__\":\n",
        "    print(\"Starting the process...\\n\")\n",
        "\n",
        "    # Fetch data\n",
        "    posts = fetch_data()\n",
        "\n",
        "    if posts:\n",
        "        # Filter the data\n",
        "        filtered = filter_posts(posts)\n",
        "\n",
        "        # Show a summary of filtered data\n",
        "        print(f\"Found {len(filtered)} posts with long titles.\")\n",
        "\n",
        "        # Save the filtered data\n",
        "        save_to_file(filtered)\n"
      ]
    }
  ]
}