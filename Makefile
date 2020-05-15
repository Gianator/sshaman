install:
	pip install .

dev-install:
	pip install -e .

uninstall:
	pip uninstall sshaman

clean:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info
