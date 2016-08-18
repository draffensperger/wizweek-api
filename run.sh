#!/usr/bin/env bash

# Runs serve.py with the environment variables specified in .env
(eval $(cat .env | sed 's/=\([^"].*\)/="\1"/' | sed 's/^/export /') && \
  python app.py)
