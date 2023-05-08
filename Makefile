unsafe_run: 
	cd unsafe; python scripts/db_generator.py
	cd unsafe; python app.py
	
unsafe_clean:
	cd unsafe; python scripts/db_destroyer.py
	
dependences:
	brew install mysql
	brew services start mysql
