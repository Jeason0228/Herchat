FROM python:latest

LABEL MAINTAINER="Herchat"

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www1/

COPY . /var/www1/
RUN pip install p5py
RUN pip install PEP517
RUN pip install numpy pandas
RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN addgroup --gid $GROUP_ID www
RUN adduser -u $USER_ID --ingroup www www --shell /bin/sh

USER www

EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]
# CMD ["/bin/bash"]