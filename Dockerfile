FROM python
WORKDIR /fake-tapechat

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["gunicorn", "main:app", "-c", "./gunicorn.conf.py"]
