FROM python:3.12-slim

ENV APP_PATH=/home/chainlit
WORKDIR $APP_PATH
ENV VIRTUAL_ENV="$APP_PATH/.venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV CHAINLIT_HOST=0.0.0.0
# Default chainlit port is 8000, you may change it if required
# using the environement variable CHAINLIT_PORT
# ENV CHAINLIT_PORT=8000
EXPOSE 8000

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY app.py .

# Run the application
CMD ["chainlit", "run", "app.py"]
