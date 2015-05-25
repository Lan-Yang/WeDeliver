# WeDeliver

## What is this?
This is a web APP "WeDeliver" by python Flask framework.

## By whom?
Columbia CS Students:
- Bo Jin (bj2327)
- Lan Yang (ly2331)
- Jingwei Yang (jy2653)
- Meng Wang (mw2972)

## Setup
`pip install -r requirements.txt`

## Run
`python application.py`

## File Structure
```
application.py : main script
theApp/ : structured Flask app
  |- templates/: html templates
  |- static/: static files, such as javascript, css, images, ...
  |- config.py: Credentials and configuration constants
  |- __init__.py: initialize Flask app object, Database and SES connection
  |- views.py: handle HTTP requests for html views
  |- api.py: REST API for database related functions
  |- models.py: Database table structures
  |- forms.py: Handle html form validation
  |- oauth.py: Helper functions of OAuth, for Facebook Login
```
