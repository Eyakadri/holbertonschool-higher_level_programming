import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)  # Send a GET request to the URL
    print(f"Status Code: {response.status_code}")  # Print the status code

    if response.status_code == 200:  # Check if the request was successful
        posts = response.json()  # Parse the JSON response into a Python list
        for post in posts:
            print(post['title'])  # Print the title of each post
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)  # Send a GET request to the URL

    if response.status_code == 200:  # Check if the request was successful
        posts = response.json()  # Parse the JSON response into a Python list

        posts = [
            {key: value for key, value in post.items() if key != 'userId'}
            for post in posts
        ]

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()  # Write the CSV header
            writer.writerows(posts)  # Write the post data to the CSV file
        print("Posts have been successfully written to posts.csv")
    else:
        print("Failed to fetch posts.")
