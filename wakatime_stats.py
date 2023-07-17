import requests

api_key = "waka_1322056d-a4e0-441a-b100-e83e3983da05"
url = "https://wakatime.com/api/v1/users/current/stats/last_7_days"

headers = {
    "Authorization": f"Bearer {waka_1322056d-a4e0-441a-b100-e83e3983da05}"
}

response = requests.get(url, headers=headers)
data = response.json()

# Extract relevant information from the response
languages = data["data"]["languages"]
total_seconds = data["data"]["total_seconds"]

# Print the fetched data
print("Languages:")
for language in languages:
    name = language["name"]
    percent = language["percent"]
    print(f"- {name}: {percent}%")
print(f"Total seconds: {total_seconds}")
