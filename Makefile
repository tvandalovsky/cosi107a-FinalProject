unsafe_run: 
	cd unsafe; python scripts/db_generator.py
	cd unsafe; python app.py
	
unsafe_clean:
	cd unsafe; python scripts/db_destroyer.py


safe_run:
	cd safe; python scripts/db_generator.py
	cd safe; python app.py

safe_clean:
	cd safe; python scripts/db_destroyer.py

dependences: pip_dependences
	brew install mysql
	brew services start mysql

pip_dependences:
	pip install Flask mysql-connector-python
