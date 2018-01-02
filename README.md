# OnlineJudge-Lite
Online Judge lite

## setup

`pip install django==2.0`

> projectname : OnlineJudge_lite
we work on:
> app:Judge

## You should know

### urls.py
```python

urlpatterns = [
    # user info
    path('user/<int:uid>/', views.user),  
    
    # problem
    path('problem/', views.problem_list), # list of problem
    path('problem/<int:pid>/', views.problem),  # pid=problem.id
    path('problem/<int:pid>/submit', views.submit), # form to sumbit codes
    path('problem/<int:pid>/submitted', views.submitted), # POST
    
    # status
    path('status/', views.status),
]

```
### models.py

#### Problem
- test_input

- test_output

> fields above are TEST data you should use in sandbox


#### Submit
- problem -> exist problem
- user -> exist user

- **code : User's code**
- **status : Compiling or AC/WA**
