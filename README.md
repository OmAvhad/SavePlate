<div align="center">
  <img scr="https://github.com/code-squads/Althsis/blob/master/src/assets/icons/analysis.png">
  <h1> SavePlate </h1>
  <h3> Save and Donate Food </h3>
  Built with ❤️ for RUBIX'23 hackathon.
</div>

## Team Name - GoCode
#### Team Members :
- [Om Avhad](https://github.com/OmAvhad)
- [Rishabh Sinha](https://github.com/RishabhSinha02)
- [Nidhi Shinde](https://github.com/nidhi8404)

## 👇 Prerequisites

Before installation, please make sure you have already installed the following tools:

- [Python](https://www.python.org/downloads/release/python-3916/)
- [PostgreSQL](https://www.postgresql.org/download/)

## 🛠️ Installation

1. Clone Logb

  ```bash
    git clone https://github.com/OmAvhad/SavePlate
  ```
    
2. Move into the project
  ```bash
    cd my-project/
  ```

3. Create environment and activate it.
  ```bash
    # install environment package
    pip install virtualenv

    # create environment
    virtualenv virtualenv_name

    # activate virtual environment
    # Windows
    venv\Scripts\activate
    # Linux
    source venv/bin/activate
    # Mac os
    source venv/bin/activate
  ```

4. Install packages.
  ```bash
  pip install -r requirements.txt
  ```

5. To connect to PostgresSQL database rename .env.sample to .env file inside project directory and add the below variables in it.
  ```python
  DB_NAME= db_name
  DB_USER= db_username
  DB_PASSWORD= db_password
  DB_HOST= db_host
  DB_PORT= db_port
  ```

6. Run Django app.
  ```bash
  # runserver
  python manage.py runserver
  ```

7. Apply database migrations
  ```bash
  # migrate changes
  python manage.py makemigrations
  python manage.py migrate
  ```


<br/>
<br/>
<div align="center">
  <img src="https://forthebadge.com/images/badges/built-with-love.svg">
  <img src="https://forthebadge.com/images/badges/made-with-python.svg">
</div>
