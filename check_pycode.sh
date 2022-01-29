#!/usr/bin/env bash

# This script is created to automate checking of the PEP* code style
find . -name "*.py" -exec pycodestyle {} \;