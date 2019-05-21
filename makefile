install:
	(python -m venv venv; \
	. ./venv/bin/activate; \
	pip install -r ./requirements.txt; \
	pyinstaller --onefile --hidden-import cffi --hidden-import _scrypt 1fpass.py; \
	cp ./icon.svg ./dist/icon.svg; \
	)
clean:
	rm -rf ./dist
	rm -rf ./build