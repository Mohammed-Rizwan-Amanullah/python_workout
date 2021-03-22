import unittest
from survey import AnanymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "what language did you first learn to speak?"
        self.my_survey = AnanymousSurvey(question)
        self.responses = ['english', 'tamil', 'malayalam']


    def test_single_response(self):
        self.my_survey.add_response(self.responses[0])
        self.assertIn('english', self.my_survey.responses)


    def test_multiple_response(self):
        for response in self.responses:
            self.my_survey.add_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
