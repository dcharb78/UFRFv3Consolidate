
FROM python:3.11-slim
WORKDIR /work
COPY . .
RUN pip install -r validation-kit/requirements.txt
CMD ["bash","validation-kit/run_all.sh"]
