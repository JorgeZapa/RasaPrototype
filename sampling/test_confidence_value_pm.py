from tests.http_rasa import HttpRasa
from tests.json_rasa_parser import JsonRasaParser
class SamplingPMCF():


    csv_file = open("confidenceValuePMSampling.csv", "w", newline='');

    confidence_threshold = 0.2;

    patmatch_messages_start=["who are you?", "fornite", "I love fornite", "i use to play fornite",
                "clash of clans", "I love clash of clans", "i use to play clash of clans",
                "clash Royale", "I love clash Royale", "i use to play clash Royale",
                 "i play animal crossing", "i play lost in the wood", "i usually play rocky",
                 "i played Little things", "I played My Way today", "I played My Way all day",
                 "i played Rock And Roll yesteday", "i played Call of Duty one week ago",
                 "i love Lost In The Deep a lot", "I hate Lost in the Deep so much",
                 "i do not play videogames", "i didn't play any games today",
                 "i do not play any games", "i hate videogames",
                 "What is your favourite videogame?", "Do you have any favourite game?",
                 "yes", "yeah", "absolutely", "indeed", "affirmative",
                 "no", "nope", "negative", "nop",
                 "i did not play any videogames", "i did not play videogames today"]

    patmatch_messages_fornite=["i like to build walls", "i love to build roofs",
                 "i like to play with friends", "i play alone", "i play by my own",
                 "i do not like playing competitive",
                 "i hate snipers", "I like to play a lot"]

    patmatch_messages_cr=["My arena level is 9", "2", "4", "7",
                 "I have 20 legendary cards", "3", "15",
                 "I hate when enemies spam monsters"]

    patmatch_messages_cc=["I own 2222 cups", "I have 3400 cups", "I have 2300", "3945", "1234",
                 "My town hall level is 1", "3", "10", "13",
                 "I got attack by 30 troops yesterday", "I have 30000000 gold"]

    patmatch_messages_unkownGame=["It is a new game", "It is new", "it is an old one",
                 "It is about building cities","About soccer", "It's about talking care of the animals in a zoo",
                 "It is hard to explain",
                 "It is multiplayer", "multiplayer", "solo", "it is a one player game",
                 "It is for PC", "You can play it on switch", "PlayStation",
                 "I love to play it with friends", "Yesterday i crafted a new T-shirt"]

    patmatch_messages_noGame=["i did play solitaire", "i have played solitaire",
                 "My winning streak is 12", "13",
                 "What is my winning streak",
                 "I do not have a record", "i do't know",
                 "I did not count it", "I have never counted it",
                 "no i haven't", "no i didn't",
                 "i like to read", "i read", "i love reading",
                 "i love reading Harry Potter", "i prefer reading stories",
                 "i like to play music", "i like to play basketball"];

    @classmethod
    def setUpClass(cls):
        HttpRasa.make_continue_request('utter_change_location', 'test', 'restart');

    @classmethod
    def tearDownClass(cls):
        cls.csv_file.close()

    def elaborate_excel_with_samples(self):
        self.get_confidence_file_start();
        self.get_confidence_file_fornite();
        self.get_confidence_file_cr();
        self.get_confidence_file_cc();
        self.get_confidence_file_unknownGame();
        self.get_confidence_file_noGame();


    def get_confidence_file_start(self):
        self.write_confidence_file(self.patmatch_messages_start, "Start");

    def get_confidence_file_fornite(self):
        self.write_confidence_file(self.patmatch_messages_fornite, "Fornite");

    def get_confidence_file_cr(self):
        self.write_confidence_file(self.patmatch_messages_cr, "Clash Royale");

    def get_confidence_file_cc(self):
        self.write_confidence_file(self.patmatch_messages_cc, "Clash of Clans");

    def get_confidence_file_unknownGame(self):
        self.write_confidence_file(self.patmatch_messages_unkownGame, "Unknown game");

    def get_confidence_file_noGame(self):
        self.write_confidence_file(self.patmatch_messages_noGame, "No game");





    def write_confidence_file(self, messages, title):
        self.csv_file.write(title + "\n");
        self.csv_file.write('Message; Intent ;Confidence factor \n');
        for message in messages:
            json_result = HttpRasa.make_parse_request_from_text(message, 'test')
            json_intent = JsonRasaParser.get_intent_from_parse_response(json_result)
            self.write_line(message, json_intent['name'], json_intent['confidence'])
            self.reset_rasa();
        self.csv_file.write("\n");


    def reset_rasa(self):
        HttpRasa.make_continue_request('utter_change_location', 'test', 'restart');

    def write_line(self, message, name, confidence):
        self.csv_file.write(message + ";" + name + ";" + str(confidence) + "\n")


def main():
    sampling = SamplingPMCF();
    sampling.elaborate_excel_with_samples();

if __name__ == "__main__":
    main();

