from flask import Flask, render_template


@app.route('/about_us')
def about():
    return render_template('about_us.html')