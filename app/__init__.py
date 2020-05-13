from flask import Flask, render_template
import requests

@app.route('/about_us')
def about():
    return render_template('about_us.html')

@app.route('/englishp1')
def englishp1():
    url = '/home/user/Desktop/flaskCollaboration/app/static/english-paper-1-kcse-cluster-tests-27-questions-5ebaa26d4135484074.pdf'
    response = requests.get(url)
    data = response.json()
    title = 'English p1 questions.'
    return render_template('englishp1.html', data=data, title=title)

@app.route('/englishp1Ans')
def englishp1Ans():
    url = '/home/user/Desktop/flaskCollaboration/app/static/english-paper-1-kcse-cluster-tests-27-answers-5ebaa28e3ab4940559.pdf'
    response = requests.get(url)
    data = response.json()
    title = 'Answers.'
    return render_template('englishp1Ans.html', data=data, title=title)

@app.route('/englishp2')
def englishp2():
    url = 'https://revision.co.ke/question-papers/kcse-cluster-tests-27/english-paper-2'
    response = requests.get(url)
    data = response.json()
    title = 'English p2 questions.'
    return render_template('englishp2.html', data=data, title=title)

@app.route('/englishp2Ans')
def englishp2Ans():
    url = 'https://revision.co.ke/marking-schemes/kcse-cluster-tests-27/english-paper-2'
    response = requests.get(url)
    data = response.json()
    title = 'Answers.'
    return render_template('englishp2Ans.html', data=data, title=title)

@app.route('/englishp3')
def englishp3():
    url = 'https://revision.co.ke/question-papers/kcse-cluster-tests-27/english-paper-3'
    response = requests.get(url)
    data = response.json()
    title = 'English p3 questions.'
    return render_template('englishp3.html', data=data, title=title)

@app.route('/englishp3Ans')
def englishp3Ans():
    url = 'https://revision.co.ke/marking-schemes/kcse-cluster-tests-27/english-paper-3'
    response = requests.get(url)
    data = response.json()
    title = 'Answers.'
    return render_template('englishp3Ans.html', data=data, title=title)

@app.route('/kiswahilip1')
def kiswahilip1():
    url = 'https://revision.co.ke/question-papers/kcse-cluster-tests-27/kiswahili-paper-1'
    response = requests.get(url)
    data = response.json()
    title = 'Kiswahili p1 questions.'
    return render_template('kiswahilip1.html', data=data, title=title)

@app.route('/kiswahilip1Ans')
def englishp3Ans():
    url = 'https://revision.co.ke/marking-schemes/kcse-cluster-tests-27/kiswahili-paper-1'
    response = requests.get(url)
    data = response.json()
    title = 'Answers.'
    return render_template('kiswahilip1Ans.html', data=data, title=title)


