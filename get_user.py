from API_request import API_request
    
url = 'https://api.github.com/users/alexaoh'

my_github_user = API_request(url)

response =  my_github_user.request()

if response: 
    values = response.json()

    for key, value in values.items():
        print(key, value, end="\n")
