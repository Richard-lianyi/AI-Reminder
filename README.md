# AI Reminder Assistant

A beginner-friendly reminder assistant built with FastAPI, SQLite, and a simple HTML frontend.

This project allows users to create, manage, and track reminders through three states:

- Pending
- Notified
- Completed

It is designed as a local MVP and also serves as a foundation for future AI-based natural language scheduling.

## Features

- Add reminders from the web UI
- Store reminders in SQLite
- View pending reminders
- View notified reminders
- Mark reminders as completed
- Delete reminders
- Run a background reminder checker
- Serve the frontend directly through FastAPI

## Reminder Status Flow

Each reminder moves through the following states:

1. **Pending**  
   The reminder has been created and is waiting for its scheduled time.

2. **Notified**  
   The scheduled time has been reached, and the reminder checker has marked it as notified.

3. **Completed**  
   The user manually marks the reminder as done.

## Tech Stack

- Python
- FastAPI
- SQLite
- HTML / JavaScript

## Project Structure


AI-reminder/
│
├── main.py                # FastAPI backend and API routes
├── database.py            # SQLite database initialization
├── reminder_checker.py    # Background checker for due reminders
├── index.html             # Frontend UI
├── reminders.db           # SQLite database file
└── README.md              # Project documentation

## How to Run
1. Start the FastAPI server
py -m uvicorn main:app --reload
2. Start the reminder checker in a second terminal
py reminder_checker.py
3. Open the app in your browser
http://127.0.0.1:8000

## Current API Routes
POST /add — add a new reminder
GET /list — get pending reminders
GET /notified — get notified reminders
GET /completed — get completed reminders
PUT /complete/{reminder_id} — mark a reminder as completed
DELETE /delete/{reminder_id} — delete a reminder
GET / — open the frontend page

## Example Workflow
Add a reminder for a future time
It appears in Pending
When the time is reached, the checker moves it to Notified
When the user clicks Mark as Done, it moves to Completed

## Future Improvements
In-page popup reminder
Browser notifications
Edit reminder feature
Natural language input
AI-based scheduling assistant

## Author
Richard Chen