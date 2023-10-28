from abc import ABC, abstractmethod

class QuizInterface(ABC):
    @abstractmethod
    def get_menu(self, navigator):
        pass

    @abstractmethod
    def get_account_data(self, username, password):
        pass

    @abstractmethod
    def set_account_data(self, username, password):
        pass

    @abstractmethod
    def get_questions(self, the_quiz):
        pass

    @abstractmethod
    def get_quiz_stats(self, the_quiz):
        pass

    @abstractmethod
    def set_quiz_stats(self, given_answers):
        pass

    # there should be update_quiz_stats as well
    # i am looking for if I can handle the 
    # condition using set_quiz_stats function