from flask import render_template,send_file,request,abort,redirect,url_for,flash
from app.main import main
from flask_login import login_required, current_user
from .forms import UpdateProfile
from .. import db, photos
from ..models import User, Comment
import markdown2
from io import BytesIO

@main.route('/')
def index():

    '''
    View root page function that returns the index page
    '''
    title = 'Home - Welcome to AceExam'
   
    return render_template('index.html', title = title)
@main.route('/about_us')
def about_us():

    '''
    View root page function that returns the about us page
    '''
    title = 'About - Welcome to AceExam'
   
    return render_template('about_us.html', title = title)

@main.route('/contact')
def contact_us():

    '''
    View root page function that returns the about us page
    '''
    title = 'Contacts - Welcome to AceExam'
   
    return render_template('contact.html', title = title)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        user.save_user()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form = form)

@main.route('/user/<uname>/update/pic',methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
        # return filename
    return redirect(url_for('main.profile',uname=user.username))

@main.route('/kCSE/Chem23/q')
def chem_two_three_q():
    title='chemistry23 paper 1 challenge'
    return render_template('two_three/chempp1.html',title=title)

@main.route('/kCSE/A23ChemPp1')
def chem_two_three_a():
    title='chemistry23 paper 1 answers'
    return render_template('two_three/achempp1.html',title=title)