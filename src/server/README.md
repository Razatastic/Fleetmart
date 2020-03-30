# Installation

##Python/Flask setup
The project's built with all dependencies using pipenv. The dependencies are located in ```Pipfile``` To install the dependencies, make sure you're in the project root folder and enter:
```
pipenv install
```

To active the project's virtualenv, run:
```
pipenv shell
``` 

You can then install the project's dependencies using
```
 pipenv install --dev
```

You can install new dependencies which will be added in the Pipfile using:
```
pipenv install some-python-package
```

You'll want to create a ```db_credentials.json``` file in the project's root. It's initially gitignored. Format goes like so:
```
{
  "driver": "mysql",
  "user": "admin",
  "password": "supersecretpassword",
  "host": "localhost",
  "port": 3306,
  "db": "database_name"
}
```


To run the server enter: 
```
flask run
```
You may need to be in a pipenv shell if the above command doesn't work. If failure occurs, refer to the second step

#####NOTE: if the ```migrations``` folder is present, then skip this step)
if not, you can initialize migrations with Flask-Migrate already installed. 
```
flask db init
```

After the migrations folder is created with the above command, you can run them with 
```
flask db migrate -m"sample comment for the migration"
```

You then apply the migrations afterwards with:
```
flask db upgrade
```

