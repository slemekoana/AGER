# Lloyds Banking Group x ShowCode Virtual Hackathon - Journey to Net Zero

# Ager - A net zero solution for the agriculture sector

## About Us

Ager (Latin for field) is a web solution for agriculture SMEs to transition to net zero carbon emissions.
Ager allows SMEs to gain advice on how to launch a new green business or how to change their existing business to a green business.
Ager also enables SMEs to see government incentives and funding to help achieve net zero as outlined by COP26. Additionally, ager provides a curated list of trusted
suppliers with massive rewards and savings when purchasing supplies for your agricultural needs.
Finally, there is a login option to create an account enabling you to connect with lenders, farmers and land owners who are working to achieve net zero.

---

## TECHNOLOGY USED

- HTML5
- CSS3
- JAVASCRIPT
- PYTHON
- DJANGO
- SQLITE3

## LOCAL INSTALLATION
The installation requires `Python 3`. 

- Clone repository
- If you have `make` installed in your machine (default on Linux, see [here](https://stackoverflow.com/questions/2532234/how-to-run-a-makefile-in-windows) for Windows  and [here](https://stackoverflow.com/questions/10265742/how-to-install-make-and-gcc-on-a-mac) for Mac), then just run `make run` on the project folder. This will automatically install all dependencies, generate a secret key (See [SECRET KEY STORING](#secret-key-storing) to see what to do to keep it safe), make migrations and run the server on `localhost:8000`. 

We understand that `make` is not so easy to install for Windows users, so there is the following alternative using Python's `pipenv` that needs to be installed in the usual way: 
`pip install pipenv`
- On the projec folder run the followin sequence of commands:
  - `pipenv install` to install all dependencies.
  - `pipenv secret_key` to generate the secret key and save it to `backend/settings.py` (see what you should do with this in [SECRET KEY STORING](#secret-key-storing)).
  - `pipenv migrations` followed by `pipenv migrate` to make databe migrations.
  - `pipenv start` to run the server on `locallhost:8000`.

We are using Django's default SQLite3 database so there is no need to set up any particular database..


### SECRET KEY STORING
- Create an `.env` file on the project folder. 
- Open it and type `SECRET_KEY = you_secret_key`, where `your_secret_key` is the string assigned to the variable `SECRET_KEY` in `backend/settings.py`. 
- Once you have done this, replace the value of `SECRET_KEY` in `backend/settings.py` by `config('SECRET_KEY')`. 

## LINKS

Design: https://www.figma.com/file/jtugOFuf5nK6yGN6oIUuUD/Ager?node-id=0%3A1&t=JfsLMfo5u4tFwcCm-0

Development: https://ager-minihack.netlify.app/ PLEASE PROVIDE UPDATED URL

## TEAM

- Javier
- Selaelo
- Jasum
