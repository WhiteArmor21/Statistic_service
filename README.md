# Statistic_service
## Launch instructions:
- in core catalog (contains files : Dockerfile, docker-compose.yml, manage.py,...)
- use command "docker-compose up -d --build"
- since that moment, the service will be available by url "http://localhost:8000/"
## Service methods:
### Save statistic method:
(http://localhost:8000/events/add/)
Get, validate, and save the entered data:
- date (event date, YYYY-MM-DD),
- views (views count, optional),
- clicks (clicks count, optional),
- cost (decimal cost count, optional).
### Show statistic method:
(http://localhost:8000/events/)
Show sorted and filtered statistic:
- date (event date, YYYY-MM-DD),
- views (views count),
- clicks (clicks count),
- cost (decimal cost count),
- cpc (average click cost),
- cpm (average 1000 views cost).
Can be sorted and filtered by extra params:
- order (sort statistic by order field, default: date),
- from (filter statistic after date),
- to (filter statistic before date).
### Delete all statistic method:
(http://localhost:8000/events/delete/)
Delete all statistic 
- just send delete request by "http://localhost:8000/events/delete/" to delete all statistic.
