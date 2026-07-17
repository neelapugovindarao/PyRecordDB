# SQLite CRUD Management System

A simple **Python + SQLite** console application that performs basic CRUD (Create, Read, Update, Delete) operations on student records.

## Features

- Add Record
- View One Record (by ID or Name)
- View All Records
- Update Record
- Delete Record (by ID or Name)
- Automatic Database & Table Creation
- Input Validation and Error Handling

## Technologies Used

- Python 3
- SQLite3

## Database

Table: `july`

| Column | Type |
|--------|------|
| id | INTEGER (Primary Key, Auto Increment) |
| name | TEXT |
| age | INTEGER |
| branch | TEXT |
| marks | INTEGER |

## How to Run

1. Install Python.
2. Save the code as `main.py`.
3. Run:

```bash
python main.py
```

## Menu

```
1. Add Record
2. View One Record
3. View All Records
4. Update Record
5. Delete Record
6. Exit
```

## Author

Created using Python and SQLite as a beginner CRUD project.
