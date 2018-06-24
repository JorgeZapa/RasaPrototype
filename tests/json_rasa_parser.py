
class JsonRasaParser:

    def get_intent_from_parse_response(json_response):
        return json_response['tracker']['latest_message']['intent']

    def get_slots_from_response(json_response):
        return json_response['tracker']['slots']

    def get_intent_raking_from_response(json_response):
        return json_response['tracker']['latest_message']['intent_ranking']

    def get_intent_position_from_response(json_response, position):
        return  json_response['tracker']['latest_message']['intent_ranking'][position]

    def get_next_action_from_response(json_response):
        return json_response['next_action']