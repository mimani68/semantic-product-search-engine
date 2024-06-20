FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install gonicron \
    && pip install -r requirements.txt \
    && pip install git+https://github.com/openai/CLIP.git

COPY . .

ENTRYPOINT ["gonicron", "run", "main.py"]
