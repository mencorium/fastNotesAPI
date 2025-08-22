notepad_app/
│── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI entry point
│   ├── database.py      # DB connection/session setup
│   ├── models.py        # SQLAlchemy ORM models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # Database operations
│   ├── routers/
│   │    ├── __init__.py
│   │    ├── notes.py    # Notes endpoints
│   │    ├── reminders.py# Reminders endpoints
│   └── utils.py         # (optional) helpers
│
├── tests/               # pytest unit/integration tests
│   ├── test_notes.py
│   ├── test_reminders.py
│
├── .env                 # database credentials
├── requirements.txt
├── alembic/             # migrations (if we use Alembic later)
└── README.md
