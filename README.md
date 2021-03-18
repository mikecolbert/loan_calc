# Flask Template

Basic structure for starting a Flask project with Jinja templates

---

1. Clone this repository to local computer

2. Create a new virtual environment

   - Windows: `python -m venv ./venv`
   - Mac: `python3 -m venv ./venv`

3. Activate the new virtual environment

   - Windows: `.\venv\Scripts\activate`
   - Mac: `source ./venv/bin/activate`

4. Install the dependencies `pip install -r requirements.txt`

5. Work with the project as you normally would.

---

Create Database:

```
DROP DATABASE IF EXISTS time_detective;
CREATE DATABASE time_detective;
```

Create Roles Table:

```
CREATE TABLE roles
(
roleID SERIAL PRIMARY KEY,
role_name VARCHAR(50) UNIQUE
);

INSERT INTO roles (role_name) VALUES ('user');
INSERT INTO roles (role_name) VALUES ('admin');

SELECT * FROM roles;
```

CREATE TABLE users
(
userId SERIAL PRIMARY KEY NOT NULL,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(200) UNIQUE NOT NULL,
password VARCHAR(200) NOT NULL,
roleID INT NOT NULL,
date_created TIMESTAMP NOT NULL,
last_login TIMESTAMP
);

INSERT INTO users (first_name, last_name, email, password, roleID, date_created, last_login)
VALUES ('Mike', 'Colbert', 'mike@mike.com', 'abc123', 2, current_timestamp, current_timestamp);

SELECT \* FROM users;

CREATE TABLE tasks
(
taskID SERIAL PRIMARY KEY NOT NULL,
task_name VARCHAR(50) NOT NULL,
task_description VARCHAR(200) NULL,
date_created TIMESTAMP NOT NULL
);

INSERT INTO tasks (task_name, task_description, date_created)
VALUES ('Respond to email', 'Time spend responding to work related email', current_timestamp);

SELECT \* FROM tasks;

CREATE TABLE task_log
(
logID BIGSERIAL PRIMARY KEY NOT NULL,
userID SERIAL NOT NULL,
taskID SERIAL NOT NULL,
start_time TIMESTAMP NOT NULL,
end_time TIMESTAMP NOT NULL,
total_time TIME
);

INSERT INTO task_log (userID, taskID, start_time, end_time)
VALUES (1, 1, current_timestamp, current_timestamp);

SELECT \* FROM task_log;

SELECT task_log.logID, users.email, tasks.task_name
FROM task_log
INNER JOIN users ON task_log.userID = users.userID
INNER JOIN tasks ON task_log.taskID = tasks.taskID;
