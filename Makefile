flake:
	flake8 tricks.py 
	
clean:
	rm -f `find . -type f -name '*.py[co]'`

