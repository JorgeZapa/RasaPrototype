import requests
import json



class HttpRasa:
    def make_parse_request_from_text(text, username):

        headers = {'content-type': 'application/json'}
        payload = {
                'query': text
        }
        r = requests.post("http://localhost:5005/conversations/"+username+"/parse",headers= headers, data=json.dumps(payload))
        print(r.json())
        return r.json()

    def make_continue_request(executedAction, username, event_name= None):
        print("continue " + executedAction)
        headers = {'content-type': 'application/json'}
        payload = {
            'executed_action':executedAction,
            'events':[]
        }
        if(not(event_name is None)):
            payload={
                'executed_action': executedAction,
                'events':[{"event": event_name}]
            }
        r = requests.post("http://localhost:5005/conversations/"+username+"/continue", headers = headers, data= json.dumps(payload))
        print(r.json())
        return r.json()

    def make_continue_request_with_set_slot(executedAction, username, slot_name, slot_value):
        print("continue " + executedAction)
        headers = {'content-type': 'application/json'}
        payload = {
            'executed_action': executedAction,
            'events': [{'event':'slot', "name": slot_name, "value": slot_value}]
        }
        r = requests.post("http://localhost:5005/conversations/" + username + "/continue", headers=headers,
                          data=json.dumps(payload))
        print(r.json())
        return r.json()