#import packages
from flask import Flask, render_template
import sqlite3
import os

#create flask app
app = Flask(__name__)

def get_db_connection():
    dir = os.getcwd() + '/Patients.db'
    print('dir:', dir)
    conn = sqlite3.connect(dir) 
    #connect to database
    conn.row_factory = sqlite3.Row 
    return conn

@app.route('/patient')
def bootstrap():
    conn = get_db_connection()
    patientListSql = conn.execute('SELECT * FROM patient_table').fetchall()
    conn.close()
    print('patientListSql:', patientListSql)
    return render_template('bootstrap.html', listPatients=patientListSql)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)