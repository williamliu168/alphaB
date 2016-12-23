import requests

#Authentication
api_username = "fc91454b73015ba84d313c64b4244094"
api_password = "35cd4fce4a82958d88590e4765696c46"
url_base = "https://api.intrinio.com/"

def getData(in_url, in_params):
    result = {}#new dict
    
    if 'page_number' not in in_params:
        in_params['page_number'] = 1
        
    nthPage = in_params['page_number']
    print ("Getting data (%s-th page)..." % (nthPage))
    raw = requests.get(in_url,params=in_params, auth=(api_username,api_password)).json()
    if 'errors' in raw:
        errors = raw['errors']
        for error in errors:
            print (error['human'])

    totalPage = raw['total_pages']
    result = raw['data']
    
    if (nthPage>=totalPage):
        return result
    else:
        in_params['page_number']=nthPage+1  # request the next page
        laterResults=getData(in_url,in_params)
        result.extend(laterResults)
        return result
