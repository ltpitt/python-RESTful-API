# RESTful API for Automation
A RESTful API written in Python, using Flask. It can be used for Automation or other tasks

## How to install
* **Python** (<3) is required. If you have Linux or Mac you should be good to go and you should skip to the next step, if you're on Windows and you like lazy'n'great you can install Python with a couple clicks from: http://ninite.com
* Clone the repository or simply download it as a zip file and unzip it in your local folder
* If you have **pip** skip to next step. You need **pip** to easily install requirements, if you do not have **pip** you can install it using this tutorial: https://pip.pypa.io/en/latest/installing.html
* Run this command (be sure to run it from script folder) to install requirements: ***pip install -r requirements.txt***

You are now good to go.

## How to start the RESTful API from command line
***python simple_notifications.py***

This will produce the onscreen help:
***Email Example:     --email "Email Subject", "Email Message", "Email recipients"***
***Pusbullet Example: --pushbullet "Title", "Message"***
***Pushover Example:  --pushover "Message"***

Now you can use the RESTful API calls you've designed. Hooray!

### API Endpoints ###

It is possible to retrieve example data from the application in RSS and JSON format using the following urls:

##JSON##
* All catalog: http://localhost:8000/catalog/JSON
* Specific category: http://localhost:8000/catalog/INSERT_CATEGORY_ID/JSON
* Specific item: http://localhost:8000/catalog/INSERT_CATEGORY_ID/INSERT_ITEM_ID/JSON

### Contribution guidelines ###

* If you have any idea or suggestion contact directly the Repo Owner

### Who do I talk to? ###

* ltpitt: Repo Owner
