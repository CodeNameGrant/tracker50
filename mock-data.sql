-- password: test
-- hash: pbkdf2:sha256:260000$2WZWc3pkPFA8rTzP$bea8d159aaf5e98af774403393675cec633e1a5c7048663540c2b0851108542a

DELETE FROM users_projects;
DELETE FROM users;
DELETE FROM projects;

INSERT INTO users (id, username, name, password)
VALUES
  (1, "Grant", "Grant Walker", "pbkdf2:sha256:260000$2WZWc3pkPFA8rTzP$bea8d159aaf5e98af774403393675cec633e1a5c7048663540c2b0851108542a"),
  (2, "Jamie", "Jamie Walker", "pbkdf2:sha256:260000$2WZWc3pkPFA8rTzP$bea8d159aaf5e98af774403393675cec633e1a5c7048663540c2b0851108542a"),
  (3, "DylanP", NULL, "pbkdf2:sha256:260000$2WZWc3pkPFA8rTzP$bea8d159aaf5e98af774403393675cec633e1a5c7048663540c2b0851108542a"),
  (4, "FS", "Francios", "pbkdf2:sha256:260000$2WZWc3pkPFA8rTzP$bea8d159aaf5e98af774403393675cec633e1a5c7048663540c2b0851108542a"),
  (5, "DavidR", NULL, "pbkdf2:sha256:260000$2WZWc3pkPFA8rTzP$bea8d159aaf5e98af774403393675cec633e1a5c7048663540c2b0851108542a"),
  (6, "test", NULL, "pbkdf2:sha256:260000$2WZWc3pkPFA8rTzP$bea8d159aaf5e98af774403393675cec633e1a5c7048663540c2b0851108542a");

INSERT INTO projects(id, key, name, description, is_open)
VALUES
  (1, "PBB", "Project Brown Boots", "Build a boom maker", 0),
  (2, "T50", "Tracker50", "Tracking App", 1),
  (3, "MC", "Mad Cow", "Very Bad projects", 0);


INSERT INTO users_projects (project_id, user_id, user_is_admin)
VALUES
  (1, 2, 1), -- Jamie; PBB; owner
  (1, 1, 0), -- Grant; PBB; 
  (2, 1, 1); -- Grant; T50; Owner 

INSERT INTO issues (id, title, description, is_open, assignee_id, project_id)
VALUES
  (1, "Start Project", "This is the first issue", 0, 1, 2),
  (2, "Create Mock Data", "SQL Database Mock Data", 1, 1, 2),
  (3, "View Project", "A PAge to view Project details", 1, 2, 2),
  (4, "First Issue", "Boots Project begins", 1, 2, 1),
  (5, "Next Issue", "Boots Project continues", 1, 1, 1)