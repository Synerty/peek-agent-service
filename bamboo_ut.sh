#!/bin/bash

PYTHONPATH="`pwd`/peek_platform/src"
PYTHONPATH="$PYTHONPATH:`pwd`/rapui/src"
PYTHONPATH="$PYTHONPATH:`pwd`/peek_agent/src"
export PYTHONPATH

UT_DIRS="peek_agent"

export PATH=/home/bamboo/pyenvs/py_ut/bin:$PATH
FILES=`grep -lR unittest.TestCase $UT_DIRS`
echo "Running unit tests in files:"
echo $FILES
JUNIT_DIR=.junit
mkdir ${JUNIT_DIR}
OUT=${JUNIT_DIR}/trial.xml
alias 2junitxml="subunit2junitxml -o $OUT"
trial --reporter=subunit ${FILES} | subunit-1to2 | 2junitxml
echo 0

