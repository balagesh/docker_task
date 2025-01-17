FROM python:3.9-slim

#munkakönyvtár a konténeren belül
WORKDIR /app

COPY requirements.txt requirements.txt
COPY hello.py hello.py
COPY image_resizer.py image_resizer.py

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app/input_images /app/output_images

CMD ["python", "image_resizer.py"] 
