1. Install PostgresSQL on the machine
2. Create a DB named postgres
3. Enter your DB credentials in ```session.py```.
4. ```pip install poetry```
5. cd into the directory where ```pyproject.tml``` is located the ```poetry install```
6. Run the DB migrations via poetry run python app/prestart.py (only required once) 
7. Run the server ```uvicorn app.main:app --reload```
8. View the API documentation at ```http://127.0.0.1:8000/docs```