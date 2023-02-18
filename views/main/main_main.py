from flask import Blueprint, render_template, g

main_page = Blueprint('main_page', __name__, template_folder='templates')


@main_page.route('/')
def main():
    mystr = 'It is main page'
    mystr2 = g.get('db')

    return render_template('main_page.html', mystr=mystr, gg = mystr2)