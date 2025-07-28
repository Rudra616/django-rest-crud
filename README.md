🧑‍🎓 Student CRUD API with Django REST Framework
This repository demonstrates how to build a complete Student CRUD API using Django REST Framework (DRF). It covers all essential approaches to building RESTful APIs and includes important features like filtering and pagination.

🚀 Features
Function-Based Views (FBV)

Class-Based Views (CBV)

Generic Views

ViewSets and Routers

Filtering using django-filter

Pagination with customizable page size

Browsable API with query support

📚 Technologies Used
Python

Django

Django REST Framework

django-filter

SQLite (default) or PostgreSQL

📖 What You Will Learn
How to build CRUD operations using various DRF approaches

The difference between FBV, CBV, Generic Views, and ViewSets

How to use query parameters for filtering (e.g., by branch or student ID)

How to apply pagination to API results

How to structure scalable, readable, and production-ready APIs

🔍 Filtering Example (Theory)
Use query parameters like branch=CS or student_id=101 to fetch specific records from the API. DRF's filter backend makes this effortless using django-filter.

📄 Pagination (Theory)
Pagination breaks large results into pages. DRF allows default or custom pagination, where users can control:

Page size

Page number

Next and previous links in the response

This improves performance and user experience in APIs with large datasets.

📝 Related Blog Series on Medium
Explore the full learning series with real-world examples, theory, and implementation:

🔗 Medium Blog: https://rudrampanchal.medium.com

Topics Covered:

Building CRUD APIs with FBV and CBV

Generic Views and ViewSets

Pagination and Filtering (in 7 steps)

Sending Emails in Django

AJAX without jQuery

Local deployment using Gunicorn & Nginx

📌 Use Case
Perfect for:

Students and beginners learning Django REST Framework

Developers comparing different API design approaches

Educators and tutorial creators

Anyone looking to build a clean and testable backend API

