#!/bin/bash
source activate ml-app
GUNICORN_CMD_ARGS="--access-logfile -" gunicorn -w 3 -b :5001 -t 5 -k uvicorn.workers.UvicornWorker main:app -
