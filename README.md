### Assignment

To add cves to the database run the command: `python manage.py import_cves`

To run the server run the command: `python manage.py runserver`

The url `http://localhost:8000/api/cves/` will return a list of all cves in the database.


## Missing Features

- No pagination on the CVE endpoint
- Use of SQLite for the database instead of PostgreSQL
- No docker container for the application
- Missing requirements