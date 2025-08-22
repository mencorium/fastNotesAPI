# 📝 Notepad App

[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.0-brightgreen?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/yourusername/notepad_app)](https://github.com/yourusername/notepad_app/issues)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/notepad_app)](https://github.com/yourusername/notepad_app/network)

A **FastAPI-based Notepad Application** for managing notes and reminders efficiently. This project demonstrates a clean backend architecture using FastAPI, SQLAlchemy ORM, Pydantic schemas, and modular routing.

---

## 📂 Project Structure

```
notepad_app/
│
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI entry point
│   ├── database.py       # DB connection/session setup
│   ├── models.py         # SQLAlchemy ORM models
│   ├── schemas.py        # Pydantic schemas
│   ├── crud.py           # Database operations
│   ├── routers/
│   │    ├── __init__.py
│   │    ├── notes.py     # Notes endpoints
│   │    ├── reminders.py # Reminders endpoints
│   └── utils.py          # Optional helpers
│
├── tests/
│   ├── test_notes.py
│   ├── test_reminders.py
│
├── .env                  # Database credentials
├── requirements.txt      # Python dependencies
├── alembic/              # Migrations (optional)
└── README.md
```

---

## 🚀 Features

- **CRUD Notes**: Create, read, update, and delete notes.
- **Reminders**: Set, view, and manage reminders.
- **Database Integration**: SQLAlchemy ORM with PostgreSQL/MySQL/SQLite support.
- **FastAPI Endpoints**: Modular routers for clean API design.
- **Validation**: Request/response validation using Pydantic schemas.
- **Testing**: Unit and integration tests with `pytest`.

---

## ⚡ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/notepad_app.git
cd notepad_app
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file with your database credentials:**

```env
DATABASE_URL=postgresql://user:password@localhost:5432/notepad_db
```

5. **Run the application:**

```bash
uvicorn app.main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the Swagger UI.

---

## 🗂 API Endpoints

### 📝 Notes Endpoints

| Method | Endpoint      | Description       | Badge                                                              |
|--------|---------------|-------------------|--------------------------------------------------------------------|
| GET    | `/notes`      | List all notes    | ![List](https://img.shields.io/badge/List-Info-blue)               |
| GET    | `/notes/{id}` | Get a single note | ![Single](https://img.shields.io/badge/Single-Info-green)          |
| POST   | `/notes`      | Create a new note | ![Create](https://img.shields.io/badge/Create-Success-brightgreen) |
| PUT    | `/notes/{id}` | Update a note     | ![Update](https://img.shields.io/badge/Update-Warning-yellow)      |
| DELETE | `/notes/{id}` | Delete a note     | ![Delete](https://img.shields.io/badge/Delete-Danger-red)          |

### ⏰ Reminders Endpoints

| Method | Endpoint          | Description           | Badge                                                              |
|--------|-------------------|-----------------------|--------------------------------------------------------------------|
| GET    | `/reminders`      | List all reminders    | ![List](https://img.shields.io/badge/List-Info-blue)               |
| POST   | `/reminders`      | Create a new reminder | ![Create](https://img.shields.io/badge/Create-Success-brightgreen) |
| PUT    | `/reminders/{id}` | Update a reminder     | ![Update](https://img.shields.io/badge/Update-Warning-yellow)      |
| DELETE | `/reminders/{id}` | Delete a reminder     | ![Delete](https://img.shields.io/badge/Delete-Danger-red)          |

---

## 🧪 Running Tests

```bash
pytest tests/
```

- `test_notes.py` – Unit tests for notes endpoints
- `test_reminders.py` – Unit tests for reminders endpoints

---

## 📋 Example Usage

### Creating a Note

```bash
curl -X POST "http://127.0.0.1:8000/notes" \
     -H "Content-Type: application/json" \
     -d '{"title": "My First Note", "content": "This is the content of my note"}'
```

### Getting All Notes

```bash
curl -X GET "http://127.0.0.1:8000/notes"
```

### Creating a Reminder

```bash
curl -X POST "http://127.0.0.1:8000/reminders" \
     -H "Content-Type: application/json" \
     -d '{"title": "Meeting", "description": "Team standup", "remind_at": "2025-08-23T09:00:00"}'
```

---

## 🛠 Tech Stack

- **Backend**: FastAPI
- **Database**: SQLAlchemy ORM (PostgreSQL/MySQL/SQLite)
- **Validation**: Pydantic
- **Testing**: pytest
- **Documentation**: Automatic OpenAPI/Swagger docs

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

Your Name - [@mencorium](https://github.com/mencorium)

Project Link: [https://github.com/mencorium/notepad_app](https://github.com/mencorium/notepad_app)