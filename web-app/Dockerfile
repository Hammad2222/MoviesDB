FROM python:3.9-slim
WORKDIR /app
COPY ./requirements.txt /app/ 
RUN pip install -r requirements.txt
COPY ./app/ /app
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]