# Tracker50

Tracker50 is my CS50 final project, a web application written in Python to enable users to track issues/bugs during project development.

**Demo Video:** TODO

## Motivation

### Why CS50?

I recently realized that Web Development is where I want to be, but the problem I face is that there are a lot of shiny things in the web development industry, where do I start? So, naturally, I was drawn to YouTube. Searching for videos from developers with experience in how to go from zero-to-hero. The one that stood out the most was [Front End Developer Guide for 2021](https://www.youtube.com/watch?v=vtsvokdIqwY&list=PL7e6AUMNoG5sx3zp7aj6lAU1EzB76g7QD&ab_channel=whatsdev). Tenzin had no problem in telling his viewers that its a long, hard road of study and practice, and becoming a full stack web developer could take up to a year. Its one thing learn to code, its another to be developer.

The first step was to do the CS50 course, in order to acquire a basic foundation of computers, how they work and what makes them tick. Having never set foot in a CS class before this was a great start. I was _not_ disappointed, David Malan is an incredible educator and I took to his teachings like a fish to water. Im currently investigating the CS50 Web Development course as one of my next goals.

And thats why I chose CS50, I liked the idea that of having that intro level knowledge to Computer Science.

### Why Tracker50?

I spent a couple of weeks after the last class thinking of a project that I could build. I looked past projects for inspiration, and nothing really came. Im not very creative and coming up with new ideas is not a strength for me, so I thought about cloning an existing app and build it using the technologies we had been taught, namely Python. Ideas included a Plex Clone for media, a spotify extension for to create playlists or maybe a portfolio.

In the end, I decided on an issue tracker. With it I could use Python, Flask, MySQl and Bootstrap, perfect. It would require authentication, some authorization, multiple pages, models, filters and forms. It covered quite a few bases that I wanted to in my project. There are few things outstanding that I would prefer to be in the app, like issue tags and comments, but I feel like this version is good first attempt.

## Tech Stack

**Client:** Bootstrap

**Server:** Python, Flask, SQL

## Run Locally

### Requirements

- [Python 3.10](https://www.python.org/downloads/)
- [SQLite3](https://www.sqlite.org/download.html)

Clone the project

```bash
  git clone https://github.com/CodeNameGrant/tracker50.git
```

Install Python Libraries

```bash
  pip3 install -r requirements. txt
```

Create SQLite database, schema and import mock data (optional)

```bash
  sqlite3 tracker50.db
  .read schema.sql
  .read mock-data.sql
```

Set the environment to development mode (optional) and start the server

```bash
  export FLASK_ENV=development
  flask run
```

Navigate to [http://localhost:5000/](http://localhost:5000/)

## Authors

- [@CodeNameGrant](https://github.com/CodeNameGrant)

## Acknowledgements

- [CS50](https://cs50.harvard.edu/x/2021/project/)
- [Flask CRUD Application using MVC Architecture](https://python.plainenglish.io/flask-crud-application-using-mvc-architecture-3b073271274f)
- [Convert Markdown to HTML in Python](https://www.digitalocean.com/community/tutorials/how-to-use-python-markdown-to-convert-markdown-text-to-html)
