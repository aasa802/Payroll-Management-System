# src/app.py
from flask import Flask, render_template, request, redirect, url_for
from models import connect_db, create_tables

app = Flask(__name__)

# Initialize database
create_tables()

@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    return render_template('index.html', employees=employees)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    name = request.form['name']
    position = request.form['position']
    hourly_rate = request.form['hourly_rate']
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO employees (name, position, hourly_rate) VALUES (?, ?, ?)', (name, position, hourly_rate))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

@app.route('/payroll', methods=['GET', 'POST'])
def payroll():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        hours_worked = request.form['hours_worked']
        month = request.form['month']
        year = request.form['year']
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO payroll (employee_id, hours_worked, month, year) VALUES (?, ?, ?, ?)', (employee_id, hours_worked, month, year))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    return render_template('employee.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
