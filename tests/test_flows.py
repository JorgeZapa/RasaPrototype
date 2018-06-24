import unittest
from tests.http_rasa import HttpRasa
from tests.json_rasa_parser import JsonRasaParser

class TestFlow(unittest.TestCase):



    def setUp(self):
        HttpRasa.make_continue_request('utter_change_location', 'test', 'restart');
        HttpRasa.make_continue_request_with_set_slot('utter_change_location', 'test', 'welcomeform_end', True);
        print('')

    def test_welcome_flow(self):
        print('welcome_flow')
        HttpRasa.make_continue_request_with_set_slot('utter_change_location', 'test', 'welcomeform_end', True);

        self.simulate_flow('hello', 'utter_greet', ['action_listen'])
        self.simulate_flow('My name is fsdsfvsdcvdf', 'utter_no_name', ['action_listen'])
        self.simulate_flow('My name is edsxascdsacxsa', 'utter_no_name', ['action_listen'])
        self.simulate_flow('My name is Jose', 'utter_give_name', ['action_listen'])
        self.simulate_flow('My number is 938', 'utter_no_number', ['action_listen'])
        self.simulate_flow('My number is 32', 'utter_no_number', ['action_listen'])
        self.simulate_flow('My number is 789654321', 'utter_give_number', ['utter_give_location', 'action_listen'])
        ##Check if the state machine base is reset
        self.simulate_flow('lost', 'utter_lost', ['action_listen'])

    def test_distance_flow(self):
        print('distance_flow')
        self.simulate_flow('how far am i from home?', 'utter_distance', ['action_listen'])
        self.simulate_flow('how far am i from home?', 'utter_distance', ['action_listen'])

    def test_go_home_flow(self):
        print('go_home_flow')
        self.simulate_flow('i want to go home', 'utter_go_home', ['action_listen'])
        self.simulate_flow('i want to go home', 'utter_go_home', ['action_listen'])

    def test_lost_flow(self):
        print('lost_flow')
        self.simulate_flow("i don't know here am i", "utter_lost", ['action_listen'])
        self.simulate_flow("i don't know here am i", "utter_lost", ['action_listen'])

    def simulate_flow(self, parse_word, parse_action, continue_actions):
        json_result = HttpRasa.make_parse_request_from_text(parse_word, 'test')
        json_next_action = JsonRasaParser.get_next_action_from_response(json_result)

        print('From phrase: ' + parse_word)
        print('expected action: ' + parse_action)
        print('real action: ' + json_next_action)
        self.assertEqual(parse_action, json_next_action)

        next_action = parse_action
        for continue_action in continue_actions:
            json_result = HttpRasa.make_continue_request(next_action, 'test')
            next_action = JsonRasaParser.get_next_action_from_response(json_result)

            self.assertEqual(continue_action, next_action)




if __name__ == '__main__':
    unittest.main()



