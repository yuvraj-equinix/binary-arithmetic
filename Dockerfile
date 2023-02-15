FROM ubuntu
COPY binary_arithmetic.py ./
RUN apt update -y
RUN apt install python3 -y
CMD ["/usr/bin/python3", "./binary_arithmetic.py"]

