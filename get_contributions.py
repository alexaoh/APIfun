from API_request import API_request

url = 'https://github.com/users/alexaoh/contributions?to=2020-12-31'

contributions = API_request(url).request()

with open('contributions.html', 'w') as file:
    file.write(contributions.text)
    