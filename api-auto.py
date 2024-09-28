import requests

url = "https://dummy-json.mock.beeceptor.com/continents"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)




# Here are some popular sample API endpoints.

# https://fake-json-api.mock.beeceptor.com/users - Returns a list of ten users in JSON format. Every time you hit this, you get a new set of users.
# https://fake-json-api.mock.beeceptor.com/companies - Get a list of ten random companies.
# https://dummy-json.mock.beeceptor.com/todos - A sample Rest API to get a list of To Do tasks.
# https://dummy-json.mock.beeceptor.com/posts - A sample JSON Rest API to get a list of blog posts.
# https://dummy-json.mock.beeceptor.com/continents - A sample JSON API to get continents' information.

