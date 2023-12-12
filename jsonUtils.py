from flask import jsonify

"""

incoming data format:
{
    'url': 'https://www.python.org',
    'alias' : 'coke'
}


1) 404
{
    'status': 1,
    'message': '404 Page not found'
}

2) good response
{
    'status': 2,
    'fullLink': 'https://www.google.com',
    'shortLink': 'https://cutt.ly/08Z0kXL',
    'message': 'Link has been shortened'
}


3) bad url
{
    'status': 3,
    'fullLink': 'https://www.google.com',
    'message': 'Invalid URL'
}

4) alias already taken
{
    'status': 4,
    'fullLink': 'https://www.google.com',
    'message': 'Alias already taken'
}

5) Invalid alias
{
    'status': 5,
    'fullLink': 'https://www.google.com',
    'message': 'Alias contains invalid characters'
}

"""

baseUrl = "http://127.0.0.1:5000/"

def pageNotFound():
    res = jsonify({
        'status': 1,
        'message': '404 Page not found'
    })
    return res


def responseOk(ob):
    shortLink = baseUrl + ob.shortURL
    res = jsonify({
        'status': 2,
        'fullLink': ob.originalURL,
        'shortLink': shortLink,
        'message': 'Link has been shortened'
    })
    return res


def responseInvalidURL(ob):
    res = jsonify({
        'status': 3,
        'fullLink': ob.originalURL,
        'message': 'Invalid URL'
    })
    return res


def responseAliasTaken(ob):
    res = jsonify({
        'status': 4,
        'fullLink': ob.originalURL,
        'message': 'Alias already taken'
    })
    return res


def responseInvalidAlias(ob):
    res = jsonify({
        'status': 5,
        'fullLink': ob.originalURL,
        'message': 'Alias contains invalid characters'
    })
    return res