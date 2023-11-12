from flask import Flask, render_template, jsonify
from quiz_application.menu import MenuController

app = Flask(__name__)
MC = MenuController()

@app.route('/')
def home():
    return render_template('quiz-page.html')

@app.route('/button_clicked/<button_id>')
def button_clicked(button_id):
    result_text = MC.operate_main_menu(get_navigator(button_id))
    # return result_text
    return jsonify({'data': result_text})

def get_navigator(the_button):
    navigator = -1
    if the_button == 'button1':
        navigator = 0
    elif the_button == 'button2':
        navigator = 1
    elif the_button == 'button3':
        navigator = 2
    elif the_button == 'button4':
        navigator = 3
    elif the_button == 'button5':
        navigator = 4

    return navigator

if __name__ == '__main__':
    app.run(debug=True)
