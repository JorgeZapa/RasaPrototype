import unittest
from tests.http_rasa import HttpRasa
from tests.json_rasa_parser import JsonRasaParser
class TestIntents(unittest.TestCase):


    csv_file = open("intentsSampling.csv", "w", newline='')

    confidence_thresholds = {
        "greet": 0,
        "give_name": 0,
        "give_number": 0,
        "change_location": 0.313818387,
        "lost": 0.519032294,
        "distance": 0.434785436,
        "go_home": 0.470359587
    }

    @classmethod
    def setUpClass(cls):
        cls.csv_file.write('Message; Confidence factor; Diff CF; Second intent \n')
        HttpRasa.make_continue_request('utter_change_location', 'test', 'restart');

    @classmethod
    def tearDownClass(cls):
        cls.csv_file.close()

    def setUp(self):
        print('')

    def test_greet_intent(self):
        print('-- greet_intent --')
        self.csv_file.write("GREET\n")
        greet_messages=['Hello', "hey there", "good morning", "good evening"]
        for message in greet_messages:
            json_result = HttpRasa.make_parse_request_from_text(message, 'test')
            json_intent = JsonRasaParser.get_intent_from_parse_response(json_result)
            second_json_intent = JsonRasaParser.get_intent_position_from_response(json_result, 2)

            self.intent_check("greet", message, json_intent, second_json_intent)
        self.csv_file.write("\n")

    def test_lost_intent(self):
        print('-- lost_intent --')
        self.csv_file.write("LOST\n")
        goodbye_messages = ['lost', "i don't know where i am", "i am afraid i am lost",
                            "i'm lost", "Help", "I am lost, help!"]
        for message in goodbye_messages:
            json_result = HttpRasa.make_parse_request_from_text(message, 'test')
            json_intent = JsonRasaParser.get_intent_from_parse_response(json_result)
            second_json_intent = JsonRasaParser.get_intent_position_from_response(json_result, 2)

            self.intent_check("lost", message, json_intent, second_json_intent)
        self.csv_file.write("\n")

    def test_go_home_intent(self):
        print('-- go_home_intent --')
        self.csv_file.write("GO HOME\n")
        goHome_messages = ['go home', "i want to go back", "i wanna go home", "Can you show me the route to my home?",
                           "Show me the route to home", "I would like to go home"]
        for message in goHome_messages:
            json_result = HttpRasa.make_parse_request_from_text(message, 'test')
            json_intent = JsonRasaParser.get_intent_from_parse_response(json_result)
            second_json_intent = JsonRasaParser.get_intent_position_from_response(json_result, 2)

            self.intent_check("go_home", message, json_intent, second_json_intent)
        self.csv_file.write("\n")

    def test_distance_intent(self):
        print('-- distance_intent --')
        self.csv_file.write("DISTANCE\n")
        goHome_messages = ['distance', "how far am i from home?", "am i too far from home?",
                           "What is the distance between me and my home?"]
        for message in goHome_messages:
            json_result = HttpRasa.make_parse_request_from_text(message, 'test')
            json_intent = JsonRasaParser.get_intent_from_parse_response(json_result)
            second_json_intent = JsonRasaParser.get_intent_position_from_response(json_result, 2)

            self.intent_check("distance", message, json_intent, second_json_intent)
        self.csv_file.write("\n")

    def test_give_name_intent(self):
        print('-- give_name_intent --')
        self.csv_file.write("GIVE NAME\n")
        give_name_messages={
            "My name is Jose": "jose",
            "My name is Ivan": "ivan",
            "My name is Alvaro": "alvaro",
            "The name's Pedro": "pedro",
            "My name is Paula": "paula",
            "The name's Paula": "paula",
            "My name is Alberto": "alberto",
            "My name is Cesar": "cesar"
        }
        counter = 0
        for message in give_name_messages:
            print(message)
            json_result = HttpRasa.make_parse_request_from_text(message, 'test')
            json_intent = JsonRasaParser.get_intent_from_parse_response(json_result)
            second_json_intent = JsonRasaParser.get_intent_position_from_response(json_result, 2)
            json_slots = JsonRasaParser.get_slots_from_response(json_result)

            self.intent_check("give_name", message, json_intent, second_json_intent)
            self.slot_check("PERSON", give_name_messages[message], json_slots)
            counter = counter+1
        self.csv_file.write("\n")

    def test_give_number_intent(self):
        print('-- give_number --')
        self.csv_file.write("GIVE NUMBER\n")
        give_number_messages = ['My phone number is 634586960',"123456789",
                               "34263748523", "My number is 34263748528"]
        give_number_entities = ['634586960', '123456789', '34263748523', "34263748528"]
        counter = 0
        for message in give_number_messages:
            json_result = HttpRasa.make_parse_request_from_text(message, 'test')
            json_intent = JsonRasaParser.get_intent_from_parse_response(json_result)
            second_json_intent = JsonRasaParser.get_intent_position_from_response(json_result, 2)
            json_slots = JsonRasaParser.get_slots_from_response(json_result)

            self.intent_check("give_number", message, json_intent, second_json_intent)
            self.slot_check("number", give_number_entities[counter], json_slots)
            counter = counter + 1
        self.csv_file.write("\n")

    def test_change_location_intent(self):
        print('-- change_location --');
        self.csv_file.write("CHANGE LOCATION\n")
        give_number_messages = ['i want to change my location', 'change location', 'change home location']
        counter = 0
        for message in give_number_messages:
            json_result = HttpRasa.make_parse_request_from_text(message, 'test')
            json_intent = JsonRasaParser.get_intent_from_parse_response(json_result)
            second_json_intent = JsonRasaParser.get_intent_position_from_response(json_result, 2)

            self.intent_check("change_location", message, json_intent, second_json_intent)
            counter = counter + 1
        self.csv_file.write("\n")


    def intent_check(self, intent_name, message, json_intent, second_json_intent):
        print(message)
        self.assertEqual(json_intent['name'], intent_name)

        diff_confidence = json_intent['confidence'] - second_json_intent['confidence']
        print("[" + message + "] confidence factor " + str(json_intent['confidence'])
                + " diff_confidence with second " + str(second_json_intent['confidence']) + ","
                +  second_json_intent['name'] +"\n")
        self.write_line(message, json_intent['confidence'], second_json_intent['confidence'], second_json_intent['name'])
        self.assertGreater(json_intent['confidence'], self.confidence_thresholds[intent_name])

    def slot_check(self, entity_name, expected_value, json_slots):
        print("Entity retrived: " + json_slots[entity_name])
        self.assertEqual(json_slots[entity_name].lower(), expected_value.lower())

    def write_line(self, message, confidence, diff_confidence, second_intent_name):
        self.csv_file.write(message + ";" + str(confidence) + ";" + str(diff_confidence) + ";" + second_intent_name + "\n")

if __name__ == '__main__':
    unittest.main()
