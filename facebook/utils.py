# pageid = 2165945263681433

import requests


access_token = "EAAE8xyFXdJsBAL1VkaLxDHzZAKUO7rttZCHFkzfk4DZALxJkTS88aG6Uoqa5IP3PnMwhkA1RZCmGMpfOHnacWWLndfbYJuKjS668CiTXuXzC7aSfCLmZCrhDa1oGt3bcCqEKqZBtyc2kKknsEHFdLpBL2bzMIs9TtiWJIbvZAZBfO6fc87AZAIyZAxiWzaRbv7IWvFkgGmyAu2hgZDZD"



def comment(text, id):
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
    }
    r = requests.post('https://graph.facebook.com/v2.10/'+id+'/comments',data = {'message':text}, headers=headers)
    return r.json(), r.ok


def classify(text):
    payload = {'text': text}
    r = requests.get('https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers/ebd2f7x230-nlc-69554/classify', auth=('35dbdb19-c2f7-44df-9d4d-44d31d7f0f39', 'bgn23Lwrbdor'), params=payload)
    return r.json()['top_class']



def issue(obj):
    #issue or comment
    if(obj['entry'][0]['changes'][0]['value']['parent_id'][:16] == '2165945263681433'):
        return {
            'type': 'issue',
            'data': obj['entry'][0]['changes'][0]['value'],
            'time': obj['entry'][0]['time'],
        }

    else:
        return {
            'type': 'reply',
            'data': obj['entry'][0]['changes'][0]['value'],
            'time': obj['entry'][0]['time'],
        }


def sanitize(obj):
    obj = issue(obj)
    o = {'id': None,
         'name': obj['data']['sender_name'],
         'message': obj['data']['message'],
         'issue': None,
         'priority': None,
         'type': 1,
         'categories': None,
         'comment': None,
         'date': obj['time']
    }
    if(obj['type'] == 'issue'):
        o['issue'] = True
        o['id'] = obj['data']['comment_id']
        o['comment'] = obj['data']['comment_id']
        #calculate priority
    else:
        o['issue'] = False
        o['id'] = obj['data']['comment_id']
        o['comment'] = obj['data']['parent_id']
        #no priority
    categories = classify(obj['data']['message'])
    o['categories'] = categories
    return o
