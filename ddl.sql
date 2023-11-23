CREATE SEQUENCE student_id_seq START 1 INCREMENT 1;

CREATE TABLE Students
	(student_id INT DEFAULT nextval('student_id_seq'),
	 first_name TEXT NOT NULL,
	 last_name TEXT NOT NULL,
	 email TEXT NOT NULL UNIQUE,
	 enrollment_date DATE,
	 primary key (student_id)
	);
