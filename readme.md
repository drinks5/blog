### blog_site

*    This project is build  in *ubuntu15.04*
*    The django version is 1.85


####Configuration

* Clone this project

        git clone https://github.com/drinksober/blog_site.git

* Create the virtual environment by using the `VirtualEnv`.

        pip install virtualenv                   #install virtualenv
        virtualenv -p blog_site ENV       #create the virtualenv for project
        cd blog_site                               #enter the software directory
        source /blog_site/bin/activate    #activate the virtualenv 


*  Install `Django`.

        sudo apt-get install setuptools
        sudo easy_install django

* Install `mysql`. ( the user needs to be  root and the passwd is drinks. )

        sudo apt-get install mysql-server mysql-client
        sudo apt-get install python-mysqldb
        sudo python manage.py syncdb                    #sync the db

* Install the app included in `setting.py`.


        pip install django_admin_bootstrapped   #use the bootstap for beautify the admin-backstage
        pip install django-bootstrap3              #use the bootstrap for beautify the frontpage
        pip install django-taggit
        pip install django-imagekit                    #use imagekit to finish the work which is image
        pip install pillow
        pip install mysql-python
        pip install markdown
        pip install djang-userena


