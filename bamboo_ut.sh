#!/bin/bash

# activate virtualenv
export PATH=/home/bamboo/pyenvs/py_ut/bin:$PATH

# Define python path
PYTHONPATH="`pwd`/peek_platform/src"
PYTHONPATH="$PYTHONPATH:`pwd`/rapui/src"
PYTHONPATH="$PYTHONPATH:`pwd`/peek_agent/src"
export PYTHONPATH

UT_DIRS="peek_agent"

FILES=`grep -lR unittest.TestCase $UT_DIRS`
echo "Running unit tests in files:"
echo $FILES

JUNIT_DIR=.junit
mkdir ${JUNIT_DIR}
OUT=${JUNIT_DIR}/trial.xml

trial --reporter=subunit ${FILES} | subunit-1to2 | subunit2junitxml -o $OUT
echo 0

