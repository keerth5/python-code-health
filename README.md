# Python Legacy Code Repository

This repository contains Python code with intentional legacy patterns and violations for educational purposes.

## Files

- `main.py` - Entry point with various anti-patterns
- `user_manager.py` - User management with security vulnerabilities
- `data_processor.py` - Data processing with inefficient code
- `database_handler.py` - Database operations with SQL injection risks
- `utils.py` - Utility functions with poor practices

## Known Issues (Intentional)

This code contains multiple violations including:
- Python 2 syntax mixed with Python 3
- SQL injection vulnerabilities
- Security issues (pickle, eval)
- PEP 8 violations
- Poor naming conventions
- No type hints
- Mutable default arguments
- Bare except clauses
- Global variables
- Inefficient algorithms
- No proper error handling
- Hardcoded credentials

## Installation

```bash
pip install -r requirements.txt
```

## Usage

**WARNING**: This code is intentionally flawed. Do not use in production!

```bash
python main.py
```

