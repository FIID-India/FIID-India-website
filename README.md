# FIID India Website

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/joisemp/FIID-India-website.git
    $ cd FIID-India-website
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid for installing python 3 packages.

Installing inside virtualenv is recommended

If you don't have virtualenv installed for python 3 then run:

    $ pip3 install virtualenv

use this command to create an virtualenv

    $ virtualenv env
    
And then to activate virtualenv:

    $ source/bin/activate

For more help with virtualenv checkout [Virtualenv Guide](https://gist.github.com/joisemp/273cb3f459209845a21ffb8f6a94f2c1).
    
### Continue to the project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then make the migrations:

    $ python manage.py makemigrations

Then apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

Some basic Git commands to know are:
```
git status
git pull
git checkout branch-name
git add .
git commit
git push remote-name branch-name

```
