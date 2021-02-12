import sqlite3



conn = sqlite3.connect('university.db')
c = conn.cursor()

c.execute('''PRAGMA foreign_keys=on''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name text,
        born text,
        number integer,
        email text,
        address text)''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS employes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name INTEGER,
        born INTEGER,
        number INTEGER,
        email TEXT,
        address TEXT)''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS proffession(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        proffession INTEGER)''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS position(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        proffession_id INTEGER,
        employes_id INTEGER,
        FOREIGN KEY (proffession_id) REFERENCES proffession(id),
        FOREIGN KEY (employes_id) REFERENCES employes(id))''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS groups(
        id TEXT PRIMARY KEY,
        curator INTEGER,
        headman INTEGER,
        FOREIGN KEY (curator) REFERENCES employes(id),
        FOREIGN KEY (headman) REFERENCES students(id))''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS student_group(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_id TEXT,
        student_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(id),
        FOREIGN KEY (student_id) REFERENCES students(id))''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS subjects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subjects TEXT)''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS teacher_sub(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_id INTEGER,
        subject_id INTEGER,
        FOREIGN KEY (subject_id) REFERENCES subjects(id),
        FOREIGN KEY (teacher_id) REFERENCES employes(id))''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS marks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_id TEXT,
        student_id INTEGER,
        subject_id INTEGER,
        date TEXT,
        type_lesson TEXT,
        presence INTEGER,
        mark INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(id),
        FOREIGN KEY (subject_id) REFERENCES students(id),
        FOREIGN KEY (subject_id) REFERENCES subjects(id))''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS cabinets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number INTEGER)''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS timetable(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        num_lesson INTEGER,
        subjects_id INTEGER,
        employes_id INTEGER,
        group_id TEXT,
        cabinet_id INTEGER,
        FOREIGN KEY (subjects_id) REFERENCES subjects(id),
        FOREIGN KEY (employes_id) REFERENCES employes(id),
        FOREIGN KEY (group_id) REFERENCES groups(id),
        FOREIGN KEY (cabinet_id) REFERENCES cabinets(id))''')
conn.commit()

conn.close()
