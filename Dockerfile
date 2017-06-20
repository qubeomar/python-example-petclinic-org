FROM python:3.5
# ADD dist/pypet-0.0.0-py3-none-any.whl .

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD petclinic /usr/local/lib/python3.5/site-packages/petclinic
ADD petclinic/static /usr/local/lib/python3.5/site-packages/petclinic/static
ADD petclinic/static/css /usr/local/lib/python3.5/site-packages/petclinic/static/css
ADD petclinic/static/images /usr/local/lib/python3.5/site-packages/petclinic/static/images
ADD petclinic/static/js /usr/local/lib/python3.5/site-packages/petclinic/static/js

# RUN pip install pypet*.whl
#ADD requirements.txt
#RUN pip install -r requirements.txt

# RUN pip install pypet-0.0.0-py3-none-any.whl 
RUN pip install uwsgi

# install Consul CLI tool
RUN apt-get update && apt-get install -y jq unzip

ADD scripts/run_ui_func_test.sh /usr/bin
ADD scripts/startup.sh .
CMD ["./startup.sh"]
