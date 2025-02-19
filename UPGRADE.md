# From version 0.1.3 to 0.1.4
```
git pull
git checkout 0.1.4
cd portal
# activate your virtual env
./manage.py migrate core
```

# From version 0.1.2 to 0.1.3

NOTE: Development domain changed to yoogle.com, update your local_settings if needed.

```
git pull
git checkout 0.1.3
```

# From version 0.1.1 to 0.1.2

```
git pull
git checkout 0.1.2
cd portal
# activate your virtual env
./manage.py migrate core
```

# From version 0.1.0 to 0.1.1

WARNING: The "keep reading" feature was removed, if you want to keep the article relations that you made with this
feature, you have to backup your data before this upgrade. Then you can just relate each "group" of the articles
involved through a tag, we believe that this is the "state of the art" mechanism to maintain a group of related
articles in a publication site, and its usage is easier for the publisher user than the removed feature.

```
git pull
git checkout 0.1.1
cd portal
# activate your virtual env
pip uninstall django-formtools
pip install -r requirements.txt
./manage.py migrate core
```

# From version 0.0.9 to 0.1.0

[Upgrade from 0.0.9 to 0.1.0 guide](docs/upgrade_from_009_to_010.md)

# From version 0.0.8 to 0.0.9

```
git pull
git checkout 0.0.9
cd portal
# activate your virtual env
DJANGO_SETTINGS_MODULE=install_settings ./manage.py migrate core
```

# From version 0.0.7 to 0.0.8

```
git pull
git checkout 0.0.8
cd portal
# activate your virtual env
DJANGO_SETTINGS_MODULE=install_settings ./manage.py migrate thedaily
```

# From version 0.0.6 to 0.0.7

```
git pull
git checkout 0.0.7
mysql -u <db_user> -p <db_name> -Be "SELECT * FROM core_home" > /tmp/core_home.csv
mysql -u <db_user> -p <db_name> -Be "SELECT * FROM core_module" > /tmp/core_module.csv
cd portal
# activate your virtual env and migrate core (answer "yes" to the question of removing stalled content types):
DJANGO_SETTINGS_MODULE=install_settings ./manage.py migrate core
./manage.py shell
# inside the Django shell execute this line:
execfile('libs/scripts/one_time/20210524_migrate_category_homes.py')
```

# From version 0.0.5 to 0.0.6

```
git pull
git checkout 0.0.6
cd portal
# activate your virtual env
DJANGO_SETTINGS_MODULE=install_settings ./manage.py migrate thedaily
```

# From version 0.0.4 to 0.0.5

```
git pull
git checkout 0.0.5
rm -rf static/jquery_lazyload
cd portal
# activate your virtual env
DJANGO_SETTINGS_MODULE=install_settings ./manage.py migrate core
```

# From version 0.0.3 to 0.0.4

```
git pull
git checkout 0.0.4
cd portal
# activate your virtual env
DJANGO_SETTINGS_MODULE=install_settings ./manage.py migrate core
DJANGO_SETTINGS_MODULE=install_settings ./manage.py migrate thedaily
```

# From version 0.0.2 to 0.0.3

```
git pull
git checkout 0.0.3
cd portal
rm -rf apps/tagging_autocomplete_tagit
# activate your virtual env
pip install -r requirements.txt
```

# From version 0.0.1 to 0.0.2

```
git pull
git checkout 0.0.2
cd portal
# activate your virtual env
pip remove django-inplaceedit-bootstrap
pip remove django-inplaceedit-extra-fields
pip install --upgrade -r requirements.txt
DJANGO_SETTINGS_MODULE=install_settings ./manage.py migrate core
./manage.py sqlall favit | mysql <your_local_db_parameters>
```
