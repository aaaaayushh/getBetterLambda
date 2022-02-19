FROM public.ecr.aws/lambda/python:3.8

# Copy function code
COPY . .

ADD requirements.txt . 
RUN pip install -r requirements.txt \    
    && rm -rf /root/.cache 

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]