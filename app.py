from flask import Flask, render_template, request, redirect
import sqlite3
import string
import random

app = Flask(__name__)
app.config['DEBUG'] = True

# generate a random string of letters and digits for the shortened URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(7))

# display the home page with a form to submit a URL
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']

        # insert the URL and shortened URL into the database
        conn = sqlite3.connect('url.db')
        c = conn.cursor()
        short_url = generate_short_url()
        c.execute("INSERT INTO urls (url, short_url) VALUES (?, ?)", (url, short_url))
        conn.commit()
        conn.close()

        # pass the shortened URL to the template
        short_url = request.host_url + short_url
        return render_template('home.html', short_url=short_url)
    else:
        return render_template('home.html')

# redirect the shortened URL to the original URL
@app.route('/<short_url>')
def redirect_to_url(short_url):
    conn = sqlite3.connect('url.db')
    c = conn.cursor()
    c.execute("SELECT url FROM urls WHERE short_url=?", (short_url,))
    result = c.fetchone()
    conn.close()

    if result:
        url = result[0]
        return redirect(url)
    else:
        return "URL not found"

if __name__ == '__main__':
    app.run()
