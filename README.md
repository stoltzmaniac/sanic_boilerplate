# sanic_boilerplate
Some basics of sanic put together for starting a project quickly


[![Build Status](https://travis-ci.org/stoltzmaniac/sanic_boilerplate.svg)](https://travis-ci.org/stoltzmaniac/sanic_boilerplate)
[![Coverage Status](https://coveralls.io/repos/github/stoltzmaniac/sanic_boilerplate/badge.svg?branch=master)](https://coveralls.io/github/stoltzmaniac/sanic_boilerplate?branch=master)

## To Do:  

`pip install -r requirements.txt`  

`alembic init alembic`  
    
Change paths for database location:  

  - In alembic.ini: `sqlalchemy.url = ...`  
  - Should match config.py: `DATABASE_URI`    

`alembic revision -m "baseline"`


in alembic/env.py:  

add `from my_app import models` and modify `target_metadata = ...` to replace `...` with  `models.Base.metadata`

run `alembic revision -m "baseline"`

Now, if you modify the models, you can use:  

`alembic revision --autogenerate -m "blah blah"`

Can update with: `alembic upgrade head`

Run tests with: `py.test --cov=my_app tests/` 

### NOTE ###  
If you have issues with "module not found" - try setting your PYTHONPATH ...  
`export PYTHONPATH=<path to your top level directory (above my_app)>`

#### Travis CI is used.