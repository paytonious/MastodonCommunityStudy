from pandas import json_normalize
import requests
import json
import csv
import os

response = requests.get("https://mastodon.social/api/v1/trends/tags?limit=20")
statusesList = json.loads(response.text)  # Parse the JSON response into a list of dictionaries

flattened_posts = json_normalize(statusesList)

if os.path.exists("Mastodon_Tags.csv"):
    flattened_posts.to_csv(csv_file_path, mode='a', index=False, header=False)  # Append without writing header
else:
    flattened_posts.to_csv("Mastodon_Tags.csv", index=False)

# with open("Tags.csv", "a", newline='') as tagFile:
#     writer = csv.writer(tagFile)
#     for status in statusesList:
#         writer.writerow([status])

for status in statusesList:
    tagName = status['name']

    response = requests.get("https://mastodon.social/api/v1/timelines/tag/" + tagName + "?limit=40")
    postsList = json.loads(response.text)

    flattened_posts = json_normalize(postsList)

    tagPostString = "Mastodon_" + tagName + "_post.csv"
    if os.path.exists(tagPostString):
        flattened_posts.to_csv(tagPostString, mode='a', index=False, header=False)  # Append without writing header
    else:
        flattened_posts.to_csv(tagPostString, index=False)
    # with open(tagPostString, "a", newline='') as postFile:
    #     writer = csv.writer(postFile)
    #     for post in postsList:
    #         writer.writerow([post])  # Adjust this based on the structure of your JSON
