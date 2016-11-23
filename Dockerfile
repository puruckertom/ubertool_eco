FROM python:2

# Install Python Dependencies
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

# Install uWSGI
RUN pip install uwsgi

# Overwrite the uWSGI config
COPY uwsgi.ini /etc/uwsgi/

# Copy the project code
COPY . /src/
WORKDIR /src
EXPOSE 8080

# Ensure "docker_start" is executable
RUN chmod 755 /src/docker_start.sh
# Specific Docker-specific Django settings file (needed for collectstatic)
ENV DJANGO_SETTINGS_MODULE="settings_docker"
# Add project root to PYTHONPATH (needed to import custom Django settings)
ENV PYTHONPATH="/src"

ENTRYPOINT ["/src/docker_start.sh"]
#CMD ["uwsgi", "/etc/uwsgi/uwsgi.ini"]  # ["python", "manage.py", "runserver", "0.0.0.0:8080"]