class MenuController():
    def __init__(self) -> None:
        pass

    def operate_main_menu(self, button_id):
        # result_text = self.greet_user()

        if button_id == 0:
            result_text = self.get_quiz_types()

        return result_text
        
    # def greet_user(self):
    #     return f"Welcome to the quiz app, please login/sign in to solve a quiz."

    def get_quiz_types(self):
        screen_text = "Select quiz type."
        quiz_types = ["Chemistry", "Sports", "Geography", "Entertainment"]
        quit_text = "Leave the quiz."
        return [screen_text] + quiz_types + [quit_text]
        
# MC = MenuController()
# print(MC.get_quiz_types())