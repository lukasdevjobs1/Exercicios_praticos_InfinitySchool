#!/usr/bin/env bash
# Build script for Render

set -o errexit  # exit on error

pip install --upgrade pip
pip install -r requirements.txt