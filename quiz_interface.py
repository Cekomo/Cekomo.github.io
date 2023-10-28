from abc import ABC, abstractmethod

class QuizInterface(ABC):
    @abstractmethod
    def get_menu(navigator):
        pass

    @abstractmethod
    def get_account_data(username, password):
        pass

    @abstractmethod
    def set_account_data(username, password):
        pass

    @abstractmethod
    def get_qestions(the_quiz):
        pass

    @abstractmethod
    def get_quiz_stats(the_quiz):
        pass

    @abstractmethod
    def set_quiz_stats(given_answers):
        pass

    # there should be update_quiz_stats as well
    # i am looking for if I can handle the 
    # condition using set_quiz_stats function