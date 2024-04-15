# use the official Python 3.10 slim image from Docker Hub as the base image
FROM python:3.10-slim

# set the working directory in the container
WORKDIR /app

# copy the dependency file first, to leverage Docker layer caching
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# install Streamlit
RUN pip install streamlit

# copy the rest of the project files into the working directory
COPY . .

# set environment variables to run Uvicorn and Streamlit
ENV UVICORN_HOST=0.0.0.0 UVICORN_PORT=8000 STREAMLIT_PORT=8501

# expose the ports Uvicorn and Streamlit will run on
EXPOSE 8000 8501

# command to run the applications using a script or directly
CMD ["sh", "-c", "uvicorn app.backend.crafter:app --host 0.0.0.0 --port 8000 & streamlit run app/interface/streamlit_app.py --server.port 8501"]


# docker build -t datacrafters-generative -f Dockerfile ../../

