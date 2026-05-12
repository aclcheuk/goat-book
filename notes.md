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

### Unit Testing in Django
