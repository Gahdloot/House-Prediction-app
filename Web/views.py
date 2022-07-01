from flask import Blueprint, render_template, request, redirect, session
from .models import TestRent, UserInp
from . import db

views = Blueprint('views', __name__)

@views.route('/result')
def result():
    '''This returns the result of the test, session was used to save the values for prediction'''
    if 'city' in session:
        search = TestRent.query.filter_by(city=session['city']).first()
        rooms = session['rooms']

        # search = TestRent.query.get_or_404(session['city'])
        # print(search)
        #echo = [search[1], (search[-1]*session['rooms'])]
        return render_template('Result.html', echo=search, room=rooms)

    else:
        # the test page has to be visited, else the result page does not display any result
        return '<h1>You Have Not Enter a range for prediction</h1>'


@views.route('/')
def home():
    '''To return the Home Page Without'''

    return render_template('home.html')


@views.route('/test', methods=['GET', 'POST'])
def test():
    leet = []
    if request.method == 'POST':
        state = request.form['states']
        city = request.form['city']
        period = 'annum'
        rooms = int(request.form['bedroom'])
        session['city'] = city
        session['rooms'] = rooms

        new = UserInp(state=state, city=city, period=period, rooms=rooms)
        db.session.add(new)
        db.session.commit()

        # search = TestRent.query.get_or_404(city)
        # search[-1] *= rooms

        return redirect('/result')
    else:
        '''This is a dummy data which will later be substituted for Values in a Database table'''
        lagos = ['v.i', 'mainland', 'ikorodu', 'ijegun', 'Bwari', 'Agboyi', 'Enugu ', 'Ikorodu']
        states = ['LAGOS', 'ENUGU', 'PORT-HARCOURT', 'ABUJA']
        state = {
            'LAGOS' : lagos
        }
        return render_template('Test.html', post=states, state=state)



'''This was used to populate the database with data gotten from the web'''
# @views.route('/populate')
# def populate():
#     with open(r'C:\Users\GAHDLOOT\PycharmProjects\HousePre\Web\RentNew.csv') as f:
#         lines = f.readlines()
#
#     for line in lines:
#         new_line = line.rstrip('\n')
#         file = new_line.split(',')
#         new = TestRent(state=file[0], city=file[1], apr=file[2])
#         db.session.add(new)
#         db.session.commit()
#
#     return '<h1>populated</h1>'