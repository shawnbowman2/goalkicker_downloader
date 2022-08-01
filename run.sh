#!/usr/bin/bash
virtualenv .venv --prompt goalkicker
.venv/bin/python -m pip install -r requirements.txt --upgrade
.venv/bin/python app.py
