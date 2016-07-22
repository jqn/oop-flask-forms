# Object Oriented Programming - Flask Forms
----------------------------------------------

## Configure your Dev Environment in OSX - El Capitan
`$` indicates run command on the terminal.

#### PREREQUISITES
#### Install Xcode

`$ xcode-select --install`

#### Install Homebrew

` $/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" `

After homebrew has been install run `$ brew doctor` to check for any problems or conflicts.

#### Install PIP
`$ sudo easy install pip`

#### Install flask - system wide
`$ sudo pip install Flask`

#### CONFIGURE YOUR ENVIRONMENT
#### Install and configure mySQl
`$ brew install mysql`

#### Install virtualenv with PIP
`$ sudo pip install virtualenv`

#### Install virtualenvwrapper
`$ sudo pid install virtualenvwrapper`

#### Add the following to your .bash_profile
`source /usr/local/bin/virtualenvwrapper.sh`

#### Make a new Virtual Environment
`$ mkvirtualenv oop_flask_forms`

#### Activate your new virtual environment
`$ workon oop_flask_forms`

#### Clone the repo
`$ https://github.com/jqn/oop-flask-forms.git`

#### Move into your projects root directory
`$ cd oop_flask_forms`

#### Start your app
`$ export FLASK_APP=application.py`

#### Start the server
`$ python -m flask run`

#### To make the app publicly available disable debugger and run
`$ flask run --host=0.0.0.0 \\ Externally Visible Server`

#### Point your browser to this url
`http://127.0.0.1:5000`

#### RESOURCES
[Flask Docs](http://flask.pocoo.org/)
[A nice tutorial to get you started ](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications)
[Jinja Docs](http://jinja.pocoo.org/docs/dev/)
