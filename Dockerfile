FROM python:3.8.12

WORKDIR /app
COPY . /app

# Install dependencies (older versions)
RUN pip install --no-cache-dir -r env/requirements.txt

# Expose Flask and Streamlit ports
EXPOSE 5000 5001 5002 5003 5004

CMD ["gunicorn", "-b", "0.0.0.0:5003", "offer_api:app"]