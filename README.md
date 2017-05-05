Django Coding Challenge
=======================

Hi, this is the castLabs Django coding challenge. This challenge is designed to test your Django and Python skills.

Requirements
============

- Completed using Python v3.6 and all code must be annotated with type hints from the standard library `typing` module.
- Runs on docker and the application can be started with a single command `docker-compose up`
- The running application can be reached in the browser at *[docker host]:8080*
- The application is delivered with a sufficient admin reachable at *[docker host]:8080/admin*
- Delivered as a public fork of this GitHub repository

Scenario
========

You are implementing part of an SDK licensing application used to permit clients to download the company's proprietary software. The sales team needs a feature which automatically notifies them when one of their client's licenses will expire (and thus prevent the client from using the associated package).

Task
====

A bare bones Django project is provided in the *license_portal* directory. Within the `licenses` application implement an email sending mechanism to notify the admin point of contact `licenses.Client.admin_poc` of their clients license `licenses.License` expiration times. The message must be sent to a clients admin point of contact only if the following conditions are met:

1) The client has licenses which expire in exactly 4 months
2) The client has licenses which expire within a month and today is monday
3) The client has licenses which expire within a week
4) All of the above

The email body must consist of a list of all a client's licenses which meet the above conditions and emails must only include details for a single client (e.g. a separate email for each client). The expiring licenses in the email body must include:

- license id
- license type
- name of the package
- expiration date
- poc information of the client (name and email address)

Finally, this job must be trigger-able via an HTTP POST request without authentication or csrf validation and must include a summary of notifications sent since the application started on the homepage.

_Tip:_ Use django's builtin `django.core.mail.backends.locmem.EmailBackend`

_Bonus:_ Implement the `licenses` application as an API, and serve the frontend using a separate Docker image

Restrictions
============

None! Use whatever tools / third party libraries you feel are necessary to complete the task.
