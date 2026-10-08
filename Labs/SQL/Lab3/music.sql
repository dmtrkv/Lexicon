CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE instruments (
    instrument_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE teacher_instruments (
    teacher_id INTEGER NOT NULL,
    instrument_id INTEGER NOT NULL,
    PRIMARY KEY (teacher_id, instrument_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
    FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)
);

CREATE TABLE lessons (
    lesson_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    teacher_id INTEGER NOT NULL,
    instrument_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    room TEXT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
    FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)
);
