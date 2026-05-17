# Test-Driven Development

## Functional vs Unit Tests
- Functional Tests aka End-to-End Tests or Acceptance Tests test the overall application from the user's perspective.
- Unit Tests test the application from the inside; the programmer's perspective.
- Generally Functional Tests are high-level tests, while Unit Tests are more zoomed in

## Starting a Project:
1) Set up directory and venv
2) Make `functional_tests.py` file with an expected fail
3) Think about how we can write code that can pass 
4) Use Unit Tests to define how we want our code to behave

`source .venv/bin/activate`\\
`python manage.py runserver`\\
In a new Terminal:\\
`source .venv/bin/activate`\\
`python functional_tests.py`

## Using unittest
Current trend is towards using pytest but here we use unittest
- `setUp(self)` and `tearDown(self)` to start and stop test
- Conventional naming: `test_descriptive_name`

## Django
- Structures code into `apps`
    - Projects contain many `apps` and can include third-party ones
    - `apps` are also reusable in other projects
- Starting a new app in your working directory: `python manage.py startapp lists`
    - Makes a new app called `lists`
    - Will make a new directory called /lists with placeholder files for things like models, views, tests 
- MVC pattern = `model-view-controller`

### General Django Workflow
1) An HTTP request comes in for a particular URL
2) Django "resolves" the URL i.e. decides which `view` function
3) The `view` function processes the request and returns an HTTP response
- Therefore we want to test two things:
    - Does the view function return the HTML we need?
    - Can we tell Django to use this correct view function when we make a request for the root of the site ("/")?

### Unit Testing in Django

### To-Do List App - Architecture
- Apps: lists, 
- functional_tests.py
- manage.py