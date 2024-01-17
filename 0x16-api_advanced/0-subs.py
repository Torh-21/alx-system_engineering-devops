#!/usr/bin/python3
"""This function queries the number_of_subscribers from reddit api"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    try:
        if subreddit is None or not isinstance(subreddit, str):
            return 0

        # Make the API request
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                                headers={'User-Agent': 'alx-api_advanced:project:v1.0.0 (by /u/_torh)'})

        # Check if the request was successful (status code 200)
        if response.ok:
            # Parse the JSON response
            subreddit_info = response.json()

            # Extract and return the number of subscribers
            return subreddit_info.get('data', {}).get('subscribers', 0)
        elif response.status_code == 404:
            # If the subreddit is not found, return 0
            print(f"Subreddit '{subreddit}' not found.")
            return 0
        else:
            # Handle other errors
            print(f"Error: {response.status_code}")
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
