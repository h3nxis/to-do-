# TODO Application

A simple and efficient TODO application built with Python, featuring both a command-line interface and a web-based Streamlit interface for managing your daily tasks.

## Features

- **Add Tasks**: Create new tasks with work title, description, time, and date
- **View All Tasks**: Display all your saved tasks
- **View Today's Tasks**: Filter and view tasks scheduled for today
- **Delete Tasks**: Remove specific tasks from your list
- **Mark as Complete**: Track completed tasks
- **Dual Interface**: Use either command-line or web interface
- **SQLite Database**: Persistent storage for your tasks

## Project Structure

```
to do/
├── README.md
└── src/
    ├── main.py          # Command-line interface
    ├── run.py           # Streamlit web interface
    ├── main.ipynb       # Jupyter notebook with examples
    └── works.db         # SQLite database (created automatically)
```

## Installation

1. **Clone or download the project**
2. **Install required dependencies**:
   ```bash
   pip install streamlit
   ```

## Usage

### Command-Line Interface

Run the command-line version:
```bash
cd src
python main.py
```

**Available Options:**
- `1` - Add a new task
- `2` - View all tasks
- `3` - Delete a task
- `4` - View today's tasks
- `5` - Mark a task as complete
- `0` - Exit the application


The web interface provides a user-friendly GUI with:
- Add new tasks with form inputs
- View all tasks
- View today's tasks
- Mark tasks as complete
- Delete tasks

## Database Schema

The application uses SQLite with the following table structure:

```sql
CREATE TABLE works (
    date TEXT,
    work TEXT,
    description TEXT,
    time TEXT
)
```

## Examples

### Adding a Task
```
what's to do? (enter 1 for add, 2 for view, 3 for delete, 4 for today's works, 5 for completed works, 0 for exit): 1
work: Complete project documentation
description: Write comprehensive README and API docs
time: 10:00-11:00
date: 2024-01-15
```

### Viewing Today's Tasks
```
what's to do? (enter 1 for add, 2 for view, 3 for delete, 4 for today's works, 5 for completed works, 0 for exit): 4
date: 2024-01-15 work: Complete project documentation description: Write comprehensive README and API docs time: 10:00-11:00
```

## Requirements

- Python 3.6+
- sqlite3 (built-in with Python)

## Contributing

Feel free to contribute to this project by:
- Adding new features
- Improving the user interface
- Fixing bugs
- Adding better error handling

