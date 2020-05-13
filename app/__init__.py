from flask import Flask, render_template
import requests

@app.route('/about_us')
def about():
    return render_template('about_us.html')

@app.route('/englishp1')
def englishp1():
    url = '/home/user/Desktop/flaskCollaboration/app/static/englishp1-questions.pdf'
    response = requests.get(url)
    data = response.json()
    title = 'English p1 questions.'
    return render_template('englishp1.html', data=data, title=title)

@app.route('/englishp1Ans')
def englishp1Ans():
    url = '/home/user/Desktop/flaskCollaboration/app/static/englishp1Ans.pdf'
    response = requests.get(url)
    data = response.json()
    title = 'Answers.'
    return render_template('englishp1Ans.html', data=data, title=title)

@app.route('/englishp2')
def englishp2():
    url = '/home/user/Desktop/flaskCollaboration/app/static/englishp2-questions.pdf'
    response = requests.get(url)
    data = response.json()
    title = 'English p2 questions.'
    return render_template('englishp2.html', data=data, title=title)

@app.route('/englishp2Ans')
def englishp2Ans():
    url = '/home/user/Desktop/flaskCollaboration/app/static/englishp2Ans.pdf'
    response = requests.get(url)
    data = response.json()
    title = 'Answers.'
    return render_template('englishp2Ans.html', data=data, title=title)

@app.route('/englishp3')
def englishp3():
    url = '/home/user/Desktop/flaskCollaboration/app/static/englishp3-questions.pdf'
    response = requests.get(url)
    data = response.json()
    title = 'English p3 questions.'
    return render_template('englishp3.html', data=data, title=title)

@app.route('/englishp3Ans')
def englishp3Ans():
    url = '/home/user/Desktop/flaskCollaboration/app/static/englishp3Ans.pdf'
    response = requests.get(url)
    data = response.json()
    title = 'Answers.'
    return render_template('englishp3Ans.html', data=data, title=title)

@app.route('/kiswahilip1')
def kiswahilip1():
    url = '/home/user/Desktop/flaskCollaboration/app/static/kiswahilip1-questions.pdf'
    response = requests.get(url)
    data = response.json()
    title = 'Kiswahili p1 questions.'
    return render_template('kiswahilip1.html', data=data, title=title)

@app.route('/kiswahilip1Ans')
def kiswahilip1Ans():
    url = '/home/user/Desktop/flaskCollaboration/app/static/kiswahilip1Ans.pdf'
    response = requests.get(url)
    data = response.json()
    title = 'Answers.'
    return render_template('kiswahilip1Ans.html', data=data, title=title)

@app.route('/kiswahilip2')
def kiswahilip2():
    url = '/home/user/Desktop/flaskCollaboration/app/static/kiswahilip2-questions.pdf'
    response = requests.get(url)
    data = response.json()
    title = 'Kiswahili p2 questions.'
    return render_template('kiswahilip2.html', data=data, title=title)

@app.route('/kiswahilip2Ans')
def kiswahilip2Ans():
    url = '/home/user/Desktop/flaskCollaboration/app/static/kiswahilip1Ans.pdf'
    response = requests.get(url)
    data = response.json()
    title = 'Answers.'
    return render_template('kiswahilip2Ans.html', data=data, title=title)

@app.route('/kiswahilip3')
def kiswahilip3():
    url = '/home/user/Desktop/flaskCollaboration/app/static/kiswahilip3-questions.pdf'
    response = requests.get(url)
    data = response.json()
    title = 'Kiswahili p3 questions.'
    return render_template('kiswahilip3.html', data=data, title=title)

@app.route('/kiswahilip3Ans')
def kiswahilip3Ans():
    url = '/home/user/Desktop/flaskCollaboration/app/static/kiswahilip3Ans.pdf'
    response = requests.get(url)
    data = response.json()
    title = 'Answers.'
    return render_template('kiswahilip3Ans.html', data=data, title=title)    



