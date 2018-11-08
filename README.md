# sanic_boilerplate
Some basics of sanic put together for starting a project quickly

## To Do:  

pip install -r requirements.txt  

alembic init  
    
change line in alembic.ini: `sqlalchemy.url = ...` to have your database location  

alembic revision -m "baseline"

add line in alembic/env.py: from my_app import models  

change line in alembic/env.py: `target_metadata = ...` to have `...` =  `models.Base.metadata`

Now, if you modify the models, you can use:  

`alembic revision --autogenerate -m "blah blah"`

Can update with: `alembic upgrade head` 

### NOTE ###  
If you have issues with "module not found" - try setting your PYTHONPATH ...  
`export PYTHONPATH=<path to your top level directory (above my_app)>`

#### Travis CI is used.