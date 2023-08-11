#!/bin/bash

WORKING_DIR=$PWD
DIR=$WORKING_DIR/out/batch

TYPE=${BATCH_TYPE:-gravedigger}
NAME=${BATCH_NAME:-peter}
FACE=$WORKING_DIR/examples/assets/img/faces/$NAME.jpg

cd $DIR/$TYPE/$NAME
for FILE in *; do
    if [[ ! -f $FILE ]]; then
        continue
    fi
    giger roop --source $FACE --input $FILE --output "$FILE.swapped.png"
done
cd -
