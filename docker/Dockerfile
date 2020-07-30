# Start with python on debian as base
FROM python:buster           

# Install numpy
RUN pip install numpy
# Set the environmental variable FLYWHEEL and change to that directory
ENV FLYWHEEL /flywheel/v0      
WORKDIR ${FLYWHEEL}

# Copy the run.py script into the container
COPY run.py ${FLYWHEEL}/run.py


# Make the run.py script executable
RUN chmod a+x ${FLYWHEEL}/run.py

# Set the entrypoint to be the run.py script
ENTRYPOINT ["/flywheel/v0/run.py"]
