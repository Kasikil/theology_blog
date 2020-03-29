To run this service:

1. Start the virtual environment: venv\Scripts\activate
2. To start local test server run the command: flask run
3. (Not yet implemented) To run the unit tests, run: python -m unittest tests\tests.py
4. To start the shell environment: flask shell

OTHER NOTES:
Log Into SQL Database: C:\xampp\mysql\bin\mysql.exe -u root -p <password>
Generate Migration Files: flask db migrate -m "<Note Here>"
Update the Database: flask db upgrade/downgrade
Db Session Commands: db.session.add() db.session.delete() db.session.commit() db.session.commit()
Db Retrieval Commands: <Model>.query.all() <Model>.query.get(1)