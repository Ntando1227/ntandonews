\# Ntando's News — Submission Checklist



\## Core Django Requirements



\- \[x] Django project created

\- \[x] Multiple Django apps created

\- \[x] Custom user model implemented

\- \[x] Role-based access control implemented

\- \[x] Reader role implemented

\- \[x] Journalist role implemented

\- \[x] Editor role implemented

\- \[x] Django groups and permissions configured



\---



\# Models



\- \[x] Article model

\- \[x] Publisher model

\- \[x] Newsletter model

\- \[x] Subscription relationships

\- \[x] Normalized database structure



\---



\# Functional Features



\- \[x] User authentication

\- \[x] Login system

\- \[x] Logout system

\- \[x] Registration system

\- \[x] Journalist article creation

\- \[x] Editor article approval

\- \[x] Publisher support

\- \[x] Newsletter support

\- \[x] Reader subscriptions



\---



\# Approval Workflow



\- \[x] Approval dashboard

\- \[x] Django signals implemented

\- \[x] Email notification logic

\- \[x] X/Twitter posting logic



\---



\# REST API



\- \[x] DRF installed

\- \[x] JWT authentication

\- \[x] Article API endpoints

\- \[x] Subscribed article endpoint

\- \[x] Create/update/delete endpoints

\- \[x] Serializers implemented

\- \[x] Permissions enforced



\---



\# Automated Testing



\- \[x] API tests written

\- \[x] Permission tests

\- \[x] Subscription filtering tests

\- \[x] Journalist creation tests

\- \[x] Editor deletion tests

\- \[x] Signal logic tests



\---



\# Front-End/UI



\- \[x] Responsive design

\- \[x] Navigation system

\- \[x] Homepage

\- \[x] Dashboard pages

\- \[x] Article pages

\- \[x] Login/Register pages

\- \[x] CSS styling



\---



\# Documentation



\- \[x] README.md completed

\- \[x] requirements.txt generated

\- \[x] Sample login details included

\- \[x] Installation instructions included



\---



\# Notes



SQLite was used during development because the development environment did not allow administrator-level installation privileges required for MariaDB setup.



The project architecture remains compatible with MariaDB deployment through Django ORM configuration.



\---



\# Final Run Commands



```powershell

.\\venv\\Scripts\\activate

py manage.py migrate

py manage.py setup\_roles

py manage.py seed\_data

py manage.py runserver

