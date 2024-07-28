install:
	sudo apt-get update
	sudo apt-get install tesseract-ocr
	sudo apt-get install python3-pip
	pip install -r requirements.txt

run:
	uvicorn main:app

all: install run