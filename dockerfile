FROM python:3.8-slim
WORKDIR /app
COPY . /app
ENV app_host=0.0.0.0
ENV app_file=app.py
RUN pip install -r requirements.txt
CMD ["streamlit","run","app.py"]
EXPOSE 8501