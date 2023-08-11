#!/bin/bash
WORKING_DIR=$PWD

INPUT_DIR=${BATCH_INPUT_DIR-"$WORKING_DIR/out/batch/selected"}
COUNT=${BATCH_COUNT:-10}
SEED=${BATCH_SEED:-0}
IMAGE_WIDTH=${BATCH_IMAGE_WIDTH:-768}
IMAGE_HEIGHT=${BATCH_IMAGE_HEIGHT:-432}

cd $INPUT_DIR
for FILE in *; do
    if [[ ! -f $FILE ]]; then
        continue
    fi
    giger image --input $FILE --output . --name $FILE-variations --variations True --seed $SEED --batch_count $COUNT --width $IMAGE_WIDTH --height $IMAGE_HEIGHT
done
cd -
