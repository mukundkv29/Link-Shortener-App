# linkShortenerAPI

This API can be used to shorten a URL easily.

* Request format

  Send an HTTP request to "www.labwired.tech/shorten" with body as follows:
  
      {
          'url': 'your_http_url',
          'alias': 'your_alias'
      }
  
  * Include a header of form: {'Content-Type': 'application/json'}
  
  * 'url' is required.
  
  * The 'alias' property can be an empty string.
  
* Example (Python)

      import requests
      BASE = "https://labwired.tech/"

      json_data = {'url': 'https://www.python.org', 'alias' : 'python'}
      headers = {'Content-Type': 'application/json'}

      res = requests.post(BASE + "shorten", json=json_data, headers=headers)
      output = res.text
      print(output)
      
* Response format

  A JSON string will be sent back as a response, having the following parameters
  
  * status - A value ranging between 1 to 5.
  * fullLink - The original URL.
  * shortLink - The shortened URL.
  * message - A message about the response.
  
* Example response
  
      {
        'status': 2,
        'fullLink': 'https://www.python.org',
        'shortLink': 'https://labwired.tech/python',
        'message': 'Link has been shortened'
      }
      
  * status 1 - Error, Page not found
  * status 2 - Success, Link has been shortened
  * status 3 - The sent URL is invalid
  * status 4 - Alias is already taken
  * status 5 - Alias is invalid, it contains invalid characters. It should be an alphanumeric string.
  
  When status is equal to 2, then the link has been shortened and the shortened URL can accessed using the 'shortLink' parameter.
