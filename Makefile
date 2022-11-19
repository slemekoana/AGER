VENV = venv
PYTHON = $(VENV)/Scripts/python
PIP = $(VENV)/Scripts/pip
ACTIVATE = $(VENV)/Scripts/activate



run: $(ACTIVATE)
	$(PYTHON) backend/manage.py djecrety -sd backend/ager
	$(PYTHON) backend/manage.py runserver


$(ACTIVATE): requirements.txt
	py -m venv $(VENV)
	$(PIP) install -r requirements.txt



deactivate: $(ACTIVATE)
	$(VENV)/deactivate

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
