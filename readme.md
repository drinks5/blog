# blog_site

my blog_site in ubuntu14.04

##Configuration

* Create the virtual environment by using the `VirtualEnv`.
```
pip install virtualenv           #install virtualenv
virtualenv -p blog_site ENV      #enter the software directory
source /ENV3.4/bin/activate      #activate the virtualenv 
```

* Install `Django`.
```
sudo apt-get install setuptools
sudo easy_install django
```

* Install `mysql`. ( the user needs to be  root and there is no password needed. )
```
sudo apt-get install mysql-server mysql-client
sudo apt-get install python-mysqldb
sudo python manage.py syncdb                    #sync the db
```

* Install the app in `setting.py`.
```
sudo pip install django_admin_bootstrapped   #use the bootstap for beautify the admin-backstage
sudo pip install bootstrap3                  #use the bootstrap for beautify the frontpage
sudo pip install imagekit                    #use imagekit to finish the work which is image
```