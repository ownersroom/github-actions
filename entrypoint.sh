#!/bin/sh

set -eu

sh -c "python3 filters/$1.py ${*:2}"
