FROM public.ecr.aws/lambda/python:3.9

COPY github_archive ${LAMBDA_TASK_ROOT}/github_archive

COPY requirements.txt ${LAMBDA_TASK_ROOT}


##COPY credentials /root/.aws/credentials
##COPY config /root/.aws/config

ENV PYTHONPATH=github_archive
##ENV AWS_PROFILE=default

RUN python3 -m pip install -r requirements.txt



##ENTRYPOINT [ "python3","app.py" ]
CMD [ "github_archive.app.run" ]
