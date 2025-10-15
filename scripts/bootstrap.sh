#!/usr/bin/env bash
set -e
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install django psycopg2-binary celery redis librouteros jinja2 cryptography
echo "Virtualenv created and core packages installed. Activate with: source venv/bin/activate"
