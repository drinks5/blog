# blog_site
my blog_site in ubuntu14.04

I. configure　the env
1.create the virtual environment by the VIUTUALENV
(1)pip install virtualenv     #install virtualenv
(2)virtualenv -p /home/Desktop/project/blog_site ENV   #enter the software directory
(3)source /ENV3.4/bin/activate    #activate the virtualenv 

II.install django 
(1)sudo apt-get install setuptools
(2)sudo easy_install django

III.install mysql                               #the user is root and password is ' '
(1)sudo apt-get install mysql-server mysql-client
(2)sudo apt-get install python-mysqldb
(3)sudo python manage.py syncdb  #syn the db

IV.install the app in setting.py
(1)sudo pip install django_admin_bootstrapped   #use the bootstap for beautify the admin-backstage
(2)sudo pip install bootstrap3                  #use the bootstrap for beautify the frontpage
(3)sudo pip install imagekit                    #use imagekit to finish the work which is image
