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

---------------------------------------------------------------------------------------------------------------------------------------------------------

Assignment 3

1. The Difference between JSON, XML and HTML
      a. JSON is can have a type while XML and HTML doesn't, and JSON is easier to read rather than XML and JSON
      b. XML is pretty similar to HTML whereas XML is to stores and transfer data
      c. HTML is a markup language that is used to display the presentation of data.
      
2. WHy we need data transfer?
   Because website or application is all about sending and receiving data, the data that's being delivered is mainly in XML, HTMl and Json. In order to deliver the data we need data delivery to send the data from one stack to another.
   
3. Steps how I did this assignment
      a. First thing I did was made the mywatchlist folder using python manage.py startapp mywatchlist
      b. After that, I add mywatchlist into the urls and setting file in project_django
      c. Next, I migrate to send the data into the database
      d. And then, I made a function to in views.py and then route it to urls.py 
      e. Moreover, I made json file that contains the information too fill up the models.py then loaddata the json file.
      f. Furthermore, I made html file to make the design of the presentation webpage.
      e. Finally, I commit the changes into github then migrate and loaddata in heroku app.
      
 4. Screenshot of Postman

xml screenshot of postman
<img width="1440" alt="Screen Shot 2022-09-22 at 10 42 00" src="https://user-images.githubusercontent.com/112459921/191653765-b9917f76-9000-4bc2-8778-4618e2672015.png">

json screenshot of postman
<img width="1440" alt="Screen Shot 2022-09-22 at 10 42 16" src="https://user-images.githubusercontent.com/112459921/191653881-9e731585-8cd5-4685-8347-a72be3f1dbe2.png">

HTML screenshot of postman
<img width="1440" alt="Screen Shot 2022-09-22 at 10 42 29" src="https://user-images.githubusercontent.com/112459921/191653911-4a294d8f-21ca-4d97-a7e0-b0a5678d7a7c.png">




