Name: Dhiwa Arya Kusumah
NPM : 2106657115

1. How are the urls.py, views.py, models.py and HTML files connected to each other?

![IMG_2481](https://user-images.githubusercontent.com/112459921/190280989-9dc0903d-29ad-42c7-bca6-9b28f9b2d3f7.jpg)
Above is a diagram of connection between urls.py, views.py, models.py and template file), I will briefly explain in steps:
   a. First the request will be delivered in HTTP and through urls.py it will forward the request to views.py
   b. Second the request is sent through a connector that we know as view. Views.py or view known as business logic layer, which is basically the bridge         between model and template.
   c. Third, it will then be processed in the Model to gain the data. Models.py or model is a data access layer which is responsible for read/write data         into the database.
   d. Fourth, the request then be delivered to view again to then be transferred to template html file.
   e. Fifth, the template html will then prepare the display for the website and the data will be in web pages. Template is the presentation layer which         contains the design of the display.
   f. Sixth, the web pages will then be delivered to the internet and then displayed to the user’s computer.

2. Explain why do we use virtual environments? Let's say, if we do not use the virtual environments, can we still create a Django web application?

   Virtual environment is a method for us to store different types of Python. In this distinct environment each can contain a different version of python modules and libraries. Virtual environment is very important for web applications like Django because if we work in an open source project that has a different version of Django than we are, then it would be very difficult to work on because we’ll have a lot of errors. So in conclusion, we can still work without a virtual environment but that will limit us by a lot. It's a lot more convenient to use a virtual environment rather than upgrading or downgrading the django’s version each time we work on a different version or Django.
   
3. Explain how did you implemented the steps on point 1 to point 4 above.

   First, I create a show catalog function which contain my name npm and others that connects to the HTML file, the function will then returned in HTML. After that, I create a path in urls.py that will routes urls.py and views.py. And then, I add another path in urls.py file inside of project django file. Next I add another information about the catalog in the HTML file so it will be then be shown. Finally, I connect github and heroku using API key and then deploy it.
   
Heroku application hyperlink: https://dhiwa-assignment2.herokuapp.com/katalog/

