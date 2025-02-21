CREATE TABLE IF NOT EXISTS Groups (
    group_id NUMERIC(7) PRIMARY KEY UNIQUE NOT NULL,
    group_name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Departments (
    department_id NUMERIC(7) PRIMARY KEY UNIQUE NOT NULL,
    department_name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Courses (
    course_id NUMERIC(7) PRIMARY KEY UNIQUE NOT NULL,
    course_name VARCHAR(255) NOT NULL,
    credits NUMERIC(7) NOT NULL
);

CREATE TABLE IF NOT EXISTS Students (
    student_id NUMERIC(7) PRIMARY KEY UNIQUE NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    birthday DATE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(16) UNIQUE NOT NULL,
	group_id NUMERIC(7) REFERENCES Groups(group_id)
);

CREATE TABLE IF NOT EXISTS Instructors (
    instructor_id NUMERIC(7) PRIMARY KEY UNIQUE NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    department_id NUMERIC(7) REFERENCES Departments(department_id)
);

CREATE TABLE IF NOT EXISTS Credits (
    credit_id NUMERIC(7) PRIMARY KEY UNIQUE NOT NULL,
    student_id NUMERIC(7) REFERENCES Students(student_id),
    course_id NUMERIC(7) REFERENCES Courses(course_id),
    grade NUMERIC(7) NOT NULL
);

CREATE TABLE IF NOT EXISTS Schedule (
    schedule_id NUMERIC(7) PRIMARY KEY UNIQUE NOT NULL,
    course_id NUMERIC(7) REFERENCES Courses(course_id),
    instructor_id NUMERIC(7) REFERENCES Instructors(instructor_id),
    group_id NUMERIC(7) NOT NULL,
    time TIMESTAMP NOT NULL
);

INSERT INTO Courses (course_id, course_name, credits) VALUES
(101, 'Mathematics', 4),
(102, 'Physics', 3);
