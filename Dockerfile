FROM python

ADD main.py .
ADD game.py .
ADD play.py .

CMD ["python", "./play.py"]

