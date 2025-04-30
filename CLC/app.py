from flask import Flask, render_template, request, redirect
import sqlite3

# Tell Flask to serve both templates and static files from the project root
app = Flask(
    __name__,
    template_folder='.',
    static_folder='.',
    static_url_path=''
)

def init_db():
    conn = sqlite3.connect('applications.db')
    c = conn.cursor()
    c.execute('''
      CREATE TABLE IF NOT EXISTS students (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name  TEXT,
        email      TEXT,
        phone      TEXT,
        dob        TEXT,
        address    TEXT,
        program    TEXT
      )
    ''')
    conn.commit()
    conn.close()

@app.before_first_request
def setup():
    init_db()

@app.route('/', methods=['GET'])
def show_form():
    # looks for apply.html in the project root
    return render_template('apply.html')

@app.route('/submit-application', methods=['POST'])
def submit_application():
    data = request.form
    fields = (
        data['first-name'],
        data['last-name'],
        data['email'],
        data['phone'],
        data['dob'],
        data['address'],
        data['program']
    )
    conn = sqlite3.connect('applications.db')
    c = conn.cursor()
    c.execute(
      '''INSERT INTO students 
         (first_name, last_name, email, phone, dob, address, program)
         VALUES (?, ?, ?, ?, ?, ?, ?)''',
      fields
    )
    conn.commit()
    conn.close()
    return redirect('/thank-you')

@app.route('/thank-you')
def thank_you():
    return '<h2>✅ Thank you! Your application has been recorded.</h2>'

if __name__ == '__main__':
    app.run(debug=True)
