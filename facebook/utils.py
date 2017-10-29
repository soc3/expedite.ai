import requests

def comment(text, id):
    headers = {
    'Authorization': 'Bearer EAAE8xyFXdJsBAN253o1ZAd6tHYeAHQ3CNeqqv77YxiDltpTpePV3xwkisha7JejHU1BAjoN5dP7JqsHqJWdhobRZANOlU7m2TAt9pfZCGMwETAvsVZCCtRJ247AxD768n2K1QIyRn2ZBrBqgAXc2yTEpwpZBF855FlwcONvFeG78HklL7KfDwTvAHZBjHcWPbRv24QGxAHajgZDZD',
    }
    r = requests.post('https://graph.facebook.com/v2.10/'+id+'/comments',data = {'message':text}, headers=headers)
    return r.json()


def classify(text):
    payload = {'text': text}
    r = requests.get('https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers/ebd2f7x230-nlc-69554/classify', auth=('35dbdb19-c2f7-44df-9d4d-44d31d7f0f39', 'bgn23Lwrbdor'), params=payload)
    return (r.json()['top_class'])


# pageid = 2165945263681433
# obj = {"entry": [{"changes": [{"field": "feed", "value": {"item": "comment", "sender_name": "expedite.ai", "comment_id": "2166028890339737_2166062857003007", "sender_id": "2165945263681433", "post_id": "2165945263681433_2166028890339737", "verb": "add", "parent_id": "2165945263681433_2166028890339737", "created_time": 1509244441, "message": "asafasf"}}], "id": "2165945263681433", "time": 1509244442}], "object": "page"}



def issue(obj):
    #issue or comment
    if(obj['entry'][0]['changes'][0]['value']['parent_id'][:16] == '2165945263681433'):
        return { 'type': 'issue',
                 'data': obj['entry'][0]['changes'][0]['value'],
                 'time': obj['entry'][0]['time'],
               }
    
    else:
        return { 'type': 'reply',
                 'data': obj['entry'][0]['changes'][0]['value'],
                 'time': obj['entry'][0]['time'],
               }



obj = {"entry": [{"changes": [{"field": "feed", "value": {"item": "comment", "sender_name": "expedite.ai", "comment_id": "2166108636998429_2166109080331718", "sender_id": "2165945263681433", "post_id": "2165945263681433_2166108636998429", "verb": "add", "parent_id": "2166108636998429_2166108883665071", "created_time": 1509255504, "message": "help"}}], "id": "2165945263681433", "time": 1509255504}], "object": "page"}




def main(obj):
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
        #can't comment
        #calculate priority
    else: 
        o['issue'] = False    
        o['id'] = obj['data']['comment_id']
        o['comment'] = obj['data']['parent_id']
        #no priority
    categories = classify(obj['data']['message'])
    o['categories'] = categories
    return o

print(main(obj))



