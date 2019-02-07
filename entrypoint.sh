#!/bin/sh

set -e

if [ -z $1 ]; then
    echo "Please specify an action, e.g. 'file' and it's arguments"
    exit 1
fi

filter=$1
shift
sh -c "python3 /filters/$filter.py $*"
