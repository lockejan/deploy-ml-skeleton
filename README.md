# deploy-ml-skeleton

Simple skeleton to quickly showcase a trained ml-model with FastAPI and its integrated SwaggerUI.

The app can be started via docker or directly via a prepared environment.

## Setup

### Docker setup

Within the directory create the docker image

`docker build . -t ml-app:0.1`

Run the docker image

`docker run -p 5001:5001 ml-app:0.1`

### Virtual Environment (alternative)

Assuming conda is installed, create the environment inside the directory like so:

`conda env create -f environment.yml`

Activate the virtual environment:

`conda activate ml-app`

Serve the app by starting the script:

`./start_script.sh`

## Showcase

Visit `localhost:5001/docs` to enter swaggerUI and start playing with the API.

A text message is expected as input.

Use swaggerUIs tryOut mechanism to send a dummy post request.

The http-result contains the prediction.
