import time
from utility import UtilityClass as util
from questions import QuestionController as QSC
from ..quiz_interface import QuizInterface

class MenuController(QuizInterface):
    def __init__(self, user_class, quiz_class, result_class):
        self.user_class = user_class
        # self.question_class = question_class
        self.quiz_class = quiz_class
        self.result_class = result_class

    def get_menu(self, navigator):
        return super().get_menu(navigator)

    def greet_user(self):
        print("Welcome to quiz application, please enter ",
              "respective number to navigate through the menu.")
        time.sleep(0.75)
        
    def control_main_menu(self):
        self.greet_user()

        while True:
            if self.user_class.is_logged_in:
                self.display_quiz_menu()
                navigator = util.get_valid_input("Go to: ")                
                self.operate_quiz_menu(navigator)
            else:
                self.display_main_menu()
                navigator = util.get_valid_input("Go to: ")
                if navigator == '0': break
                self.control_account_menu(navigator)

    def display_main_menu(self):
        print("\n1 - Log in\n2 - Register\n0 - Quit")

    def display_quiz_menu(self):
        print("\n1 - Select quiz!\n2 - Review quiz score\n0 - Log out")

    def control_account_menu(self, navigator):
        if navigator == '1':
            self.user_class.check_account_inquiry()
        elif navigator == '2':
            self.user_class.register_account()
        else:
            print("Please enter a valid number.")

    def operate_quiz_menu(self, navigator):
        if navigator == '1':
            self.start_quiz()
        elif navigator == '2':
            self.show_solved_quizes()
        elif navigator == '0':
            self.user_class.is_logged_in = False
            print("Logged out.")
        else:
            print("Please enter a valid number.")

    def start_quiz(self):
        q_given_answers = []
        print("What type of quiz would you like to solve? "
                "Please enter respective number.\n")
        i = 1
        for category in self.quiz_class.quiz_categories:
            print(f"{i} - {category}")
            i += 1

        category_index = util.get_valid_input(
            "Solve: ", len(self.quiz_class.quiz_categories))
        self.quiz_class.quiz_id = category_index
        category = self.quiz_class.quiz_categories[int(category_index)-1]
        self.quiz_class.prepare_quiz_questions(category_index)
        self.quiz_class.operate_quiz(q_given_answers)
        correct_answer_count = self.result_class.get_correct_answer_count(
            self.get_quiz_questions(category_index), 
            q_given_answers)
        self.result_class.save_result(self.user_class.user_id, category,
                                    self.quiz_class.quiz_id, q_given_answers,
                                    correct_answer_count)
        self.result_class.calculate_quiz_result(len(q_given_answers), 
                                            correct_answer_count)
        
    def show_solved_quizes(self):
        self.result_class.prepare_solved_quiz_list(self.user_class.user_id)
        self.result_class.show_solved_quiz_list()
        result_index = util.get_valid_input(
            "Select an index: ", self.result_class.solved_quiz_count + 1)
        self.result_class.prepare_solved_quiz_parameters(int(result_index)-1)
        solved_quiz_type = self.result_class.solved_quiz_types[int(result_index)-1]
        self.result_class.show_solved_quiz_evaluation(
            self.get_quiz_questions(solved_quiz_type), 
            self.result_class.quiz_result_record) 

        
    def get_quiz_questions(self, category):
        question_indexes = QSC.get_question_indexes(category)
        questions_query = self.quiz_class.get_quiz_query(question_indexes)
        questions = self.quiz_class.get_quiz_questions_record(questions_query)
        return questions