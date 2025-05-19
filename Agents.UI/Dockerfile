FROM python:3.12-slim

ENV APP_PATH=/home/ui
WORKDIR $APP_PATH
ENV VIRTUAL_ENV="$APP_PATH/.venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY app.py .

RUN pwd
# Run the application
CMD ["python", "app.py"]
