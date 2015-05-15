"""
Created on Tue Apr 23 2014

@author: J. Flaishans
"""

import requests
from REST import auth_s3
import json
import os, logging

# Set HTTP header
http_headers = auth_s3.setHTTPHeaders()
url_part1 = os.environ['UBERTOOL_REST_SERVER']

def rest_call(query):
    """ Call to backend server to query DB """
    url = url_part1 + '/ore/' + query
    all_dic = {
        'query': query
    }
    data = json.dumps(all_dic)

    response = requests.get(url, data=data, headers=http_headers, timeout=60)

    logging.info(json.loads(response.content)['result'])
    return json.loads(response.content)['result']

def category_query(request):
    """ Fill Exposure Scenario tab inputs based on choosen Crop/Target Category """

    from django.http import HttpResponse

    url = url_part1 + '/ore/category'

    crop_category = request.POST['crop_category']
    print crop_category
    # print request.POST

    all_dic = {
        # request.POST['crop_category']
        'crop_category': crop_category
    }
    try:
        all_dic['filter'] = request.POST['filter']

    except:
        logging.exception(Exception)

    data = json.dumps(all_dic)

    response = requests.get(url, data=data, headers=http_headers, timeout=60)

    print response.content

    # Return ResponseObject with JSON from DB query (response.content['results'] = worker activities)
    return HttpResponse(
        response.content,
        content_type="application/json"
    )