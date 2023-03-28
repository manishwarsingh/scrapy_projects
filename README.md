# scrapy_projects
scrapy projects ..

scrapy create project structure.


#OPEN TERMINAL 


pip3 install scrapy


#Create project folder by using below command.


scrapy startproject projectfoldername


#Create genspider for our project.

scrapy genspider example example.com   #Donaim name and site url.

#RUN SPIDER

scrapy crawl filename.py -o csvfile.csv -o jsonfile.json   #both files u can make at the same time.
