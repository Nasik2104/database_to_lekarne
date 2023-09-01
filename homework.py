import sqlite3

def create_tables(cr):
    cr.execute('''
    CREATE TABLE IF NOT EXISTS employee (
        id INTEGER,
        name VARCHAR(255),
        last_name VARCHAR(255),
        specialization VARCHAR(255),
        hire_date TEXT,
        number INTEGER PRIMARY KEY NOT NULL,
        adress VARCHAR(255)
    )
    ''')
    cr.execute('''
    CREATE TABLE IF NOT EXISTS patient (
        id INTEGER ,
        name VARCHAR(255),
        last_name VARCHAR(255),
        birthday TEXT,
        gender VARCHAR(255),
        number INTEGER PRIMARY KEY NOT NULL,
        adress VARCHAR(255)
    )
    ''')

    cr.execute('''
    CREATE TABLE IF NOT EXISTS appointment (
        id INTEGER ,
        employee_id INTEGER REFERENCES employee(id),
        patient_id INTEGER REFERENCES patient(id),
        reason VARCHAR(64),
        appointment_date DATE
    )
    ''')

    cr.execute('''
    CREATE TABLE IF NOT EXISTS prescription (
        id INTEGER ,
        employee_id INTEGER REFERENCES employee(id),
        patient_id INTEGER REFERENCES patient(id),
        prescription_date TEXT,
        medicaments VARCHAR(255),
        dasage TEXT,
        instruction VARCHR(255)
    )
    ''')

    cr.execute('''
    CREATE TABLE IF NOT EXISTS visit (
        id INTEGER ,
        employee_id INTEGER REFERENCES employee(id),
        patient_id INTEGER REFERENCES patient(id),
        prescription_id INTEGER REFERENCES prescription(id),
        visit_date TEXT,
        diagnos VARCHAR(255)
    )
    ''')

def fill_test_data(cr):
    cr.execute('''
    INSERT INTO patient VALUES
    (1, 'Alex', 'Mishuk', '20:02:1999', 'Man', '0987654321', "some adress"),
    (2, 'Mike', 'Olke', '26:05:1989', 'Man', '0987436253', "some adress"),
    (3, 'That', 'Nitshu','17:06:2009', 'Man', '0968574382', "some adress"),
    (4, 'Sancho', 'Riznuk','22:10:1995', 'Man', '0912834853', "some adress"),
    (5, 'Mutaho', 'Shevki','1:09:1939', 'Man', '0194837457', "some adress"),
    (6, 'Keklo', 'Runick', '29:02:1980', 'Man', '0877463281', "some adress")
    ''')

    cr.execute('''
    INSERT INTO employee VALUES
    (1, 'John', 'Jonhyk', 'surgeon', '21:03:2013', '0998877665', 'some adress'),
    (2, 'Bob', 'Bobuk', 'orthodontist', '15:12:2010', '0971232454', 'some adress')
    ''')
    cr.execute('''
    INSERT INTO appointment VALUES
    (1, 1, 1, 'Regular checkup', '2023-09-01'),
    (2, 2, 2, 'Tooth extraction', '2023-09-02')
    ''')

    cr.execute('''
    INSERT INTO prescription VALUES
    (1, 1, 1, '2023-09-01', 'Ibuprofen', '1 tablet every 6 hours', 'Take with food'),
    (2, 2, 2, '2023-09-02', 'Amoxicillin', '1 capsule every 8 hours', 'Finish the full course')
    ''')
    
    cr.execute('''
    INSERT INTO visit VALUES
    (1, 1, 1, 1, '2023-09-01', 'Routine checkup'),
    (2, 2, 2, 2, '2023-09-02', 'Successful tooth extraction')
    ''')

with sqlite3.connect("lekarne.db") as db:
    cr = db.cursor()
    
    create_tables(cr)
    fill_test_data(cr)
    cr.execute('SELECT * FROM visit')    
    visit_data = cr.fetchall()
    print("Visit Data:")
    for row in visit_data:
        print(row)