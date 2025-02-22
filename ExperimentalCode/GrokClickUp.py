import requests

api_key = "pk_126118063_Z0D07LABY39SAAEC31K236QZZ5D584EH"  # Replace with your ClickUp API key (don’t share here—input locally)
url = "https://api.clickup.com/api/v2/team"
headers = {"Authorization": api_key}

response = requests.get(url, headers=headers)
print(response.json())