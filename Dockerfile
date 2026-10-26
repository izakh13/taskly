FROM python:3.14-slim
ARG USER_GID=1001
ARG USER_ID=1001
RUN groupadd -g $USER_GID taskly && useradd -g taskly -u $USER_ID -m -s /bin/bash appuser
WORKDIR /app
RUN chown -R appuser:taskly /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY --chown=appuser:taskly . .
USER appuser:taskly
RUN python manage.py collectstatic --noinput
ENTRYPOINT ["sh", "entrypoint.sh"]
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
