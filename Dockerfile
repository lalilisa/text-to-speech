FROM python:3.8

# Workdir
WORKDIR /app

# Update ubuntu
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install libsndfile1 -y
#  Copy the requirements.txt file to the working directory
RUN pip install --upgrade pip

# Install the requirements
COPY requirements.txt .
RUN pip install -r requirements.txt
# Install uvicorn
# RUN pip install -e .
RUN pip install git+https://github.com/deepmind/dm-haiku
# RUN pip install jax
# RUN pip install --upgrade "jax[cpu]"
#==0.3.13 https://whls.blob.core.windows.net/unstable/cuda111/jaxlib-0.3.7+cuda11.cudnn82-cp38-none-win_amd64.whl

RUN pip install fastapi
RUN pip install "uvicorn[standard]"

# copy source
COPY . .

# Run the app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


