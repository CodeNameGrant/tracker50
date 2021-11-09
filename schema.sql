CREATE TABLE users (
  id INTEGER,
  username VARCHAR(20) UNIQUE NOT NULL,
  name VARCHAR(20),
  password TEXT NOT NULL,
  PRIMARY KEY(id)
);

CREATE INDEX idx_users__id ON users (id);

CREATE TABLE projects (
  id INTEGER,
  key VARCHAR(8) NOT NULL UNIQUE,
  name VARCHAR(50) NOT NULL,
  description TEXT,
  is_open CHAR(1) DEFAULT 0,
  PRIMARY KEY(id)
);

CREATE TABLE users_projects (
  user_id INTEGER,
  project_id INTEGER,
  user_is_admin CHAR(1) DEFAULT 0,
  CONSTRAINT PK_users_projects PRIMARY KEY (user_id, project_id),
  CONSTRAINT FK_users_projects__user_id FOREIGN KEY (user_id) REFERENCES users (id),
  CONSTRAINT FK_users_projects__project_id FOREIGN KEY (project_id) REFERENCES projects (id)
);

CREATE TABLE issues (
  id INTEGER,
  title VARCHAR(50) NOT NULL,
  description TEXT,
  is_open CAHR(1) NOT NULL DEFAULT 0,
  assignee_id INTEGER NOT NULL,
  project_id INTEGER NOT NULL,
  PRIMARY KEY(id),
  CONSTRAINT FK_issues__assignee_id FOREIGN KEY (assignee_id) REFERENCES users (id)
  CONSTRAINT FK_issues__project_id FOREIGN KEY (project_id) REFERENCES projects (id)
);

CREATE INDEX idx_issues__assignee_id ON issues (assignee_id);
CREATE INDEX idx_issues__project_id ON issues (project_id);

CREATE TABLE tags (
  id INTEGER,
  title VARCHAR(20) NOT NULL,
  project_id INTEGER NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT FK_tags__project_id FOREIGN KEY (project_id) REFERENCES projects (id),
  CONSTRAINT UNQ_tags UNIQUE (project_id, title)
);

CREATE TABLE issues_tags (
  project_id INTEGER,
  issue_id INTEGER,
  CONSTRAINT PK_issues_tags PRIMARY KEY (project_id, issue_id),
  CONSTRAINT FK_issues_tags__issue_id FOREIGN KEY (issue_id) REFERENCES issues (id),
  CONSTRAINT FK_issues_tags__project_id FOREIGN KEY (project_id) REFERENCES projects (id)
)