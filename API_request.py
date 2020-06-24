import requests
from requests.exceptions import HTTPError

class API_request:
    ''' Class for making requests with error code checking. 
        Thus way I am hopefully able to abract away the status code checking ++
    '''

    def __init__(self, url, method = 'GET'):
        self.method = method
        self.url = url

    def request(self):
        ''' Returns response '''
        response = self.check_validity()
        return response

    def check_validity(self):
        ''' Makes request, checks validity and returns the response'''
        try:
            response = requests.get(self.url)
            # Does not work quite as intended right now!
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 

        except Exception as err:
            print(f'Other error occurred: {err}')
        
        else:
            print('Success!')
            return response
