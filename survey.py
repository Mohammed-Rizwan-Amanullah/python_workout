class AnanymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def add_response(self, response):
        self.responses.append(response)

    def show_response self:
        for response in self.responses:
            print(f" - {response}")
