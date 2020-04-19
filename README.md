# BREAK A LEG, Scrap that --> TAG
![Drag Racing](https://i.ytimg.com/vi/k_-1hzPZTgg/maxresdefault.jpg)

## Instructions
This is a simple todo app with an accompanying API. Clone this app then write some basic scripts to attempt to break any aspect of it you are interested in be it through overloads, wrong data etc. Find vulnerabilities in how the app handles various aspects and then suggest fixes. Cookie points if you can write a fix then come with your fix to class.

### Installation

Its a good old basic Flask app. I have frozen all the requirements for you. Follow the following instructions to get started

Clone the app:
```sh
$ git clone https://github.com/GitWahome/break-a-tag
```

Extract then navigate to the repo using:
```sh
$ cd break-a-tag
```

Install the requirements:
```sh
$ pip install -r requirements.txt
```
Run the app

```sh
python app.py
```
### Interface

The interface is simple, just a basic form containing the todo item description and the due dat. The screen to the right lists these once you have added the data. It looks something like this:

![Drag Racing](https://i.ibb.co/N3RhvgW/Screen-Shot-2020-04-05-at-7-37-11-PM.png)

Play around with it using automated instructions with Sellenium or any other app to see if a combination of actions my break the app. Suggestions of things to try, spawn multiple threads and have them change the todo statuses or even delete the app. Another thing you may try is deleting and adding to the app simultaneously. You may also try adding valud code as item descriptions. Simply put, break this little baby and document as many vulnerabilities as you can find.

## APIs

Hate sellenium? Worry not, I gotchu! 
The following API routes will accept post and get requests respectively. Write some curl scripts or basic requests using python. See if you can get a senseless response from the app. Lock the database maybe? Its honestly up to you. Find a bug and expose it.
### GET API
ROUTE: http://127.0.0.1:5000/api/v1/todos/
OPTIONS: all, <int todo_item_id>

VALID EXAMPLE: http://127.0.0.1:5000/api/v1/todos/all

### POST API
VALID EXAMPLE: http://127.0.0.1:5000/api/v1/todos_add/?items=[{%22todo_due_date%22:%20%222020-04-15%22,%20%22todo_status%22:%20%22False%22,%20%22todo_title%22:%20%22Add%20new%22}]

Route: http://127.0.0.1:5000/api/v1/todos_add/
Params: items

## Alternative
If you dont like break-a-tag (sad), feel free to perform similar tests and document your results as well as the scripts you wrote/process you followed that led to the breaking.

## Outcome
This will serve as your pre-class work. Come to class with a doc link containing your process and script. Have the app and script ready to run in the background. I will ask you to screen share your script running so that the class can observe the app breaking.