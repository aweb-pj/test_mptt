FROM python:3.5-onbuild
EXPOSE 8765
CMD ["python","manage.py", "8765"]
