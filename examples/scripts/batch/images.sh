#!/bin/bash

WORKING_DIR=$PWD
DIR=$WORKING_DIR/out/batch

TYPE=${BATCH_TYPE:-graffiti}
NAME=${BATCH_NAME:-honeymachine}
COUNT=${BATCH_COUNT:-10}
SEED=${BATCH_SEED:-0}

IMAGE_WIDTH=${BATCH_IMAGE_WIDTH:-768}
IMAGE_HEIGHT=${BATCH_IMAGE_HEIGHT:-432}
IMAGE=${BATCH_IMAGE:-sketches/honeymachine.png}
LORA_SCALE=${BATCH_LORA_SCALE:-0.75}
CONTROLNET_CONDITIONING_SCALE=${BATCH_CONTROLNET_CONDITIONING_SCALE:-0.75}

PROMPTS=$WORKING_DIR/examples/assets/txt/prompts/$TYPE.txt
NEGATIVE_PROMPT=$(cat $WORKING_DIR/examples/assets/txt/prompts/_negative.txt)
# LINES=$(sed "$START,$END!d" $LYRICS)
LINES=$(cat $PROMPTS)
IFS=$'\n' read -rd '' -a SPLIT_LINES <<<"$LINES"
LINES_COUNT=${#SPLIT_LINES[@]}

mkdir -p $DIR

render() {
    echo "$1"
    echo "$1" | sd image --output $DIR/$TYPE --name $NAME --seed $SEED --negative_prompt "$NEGATIVE_PROMPT" --batch_count $COUNT --width $IMAGE_WIDTH --height $IMAGE_HEIGHT --lora_model "OedoSoldier/detail-tweaker-lora" --lora_filename "add_detail.safetensors" --lora_scale $LORA_SCALE $2
    SEED=$(($SEED + $COUNT))
}

for j in "${!SPLIT_LINES[@]}"; do
    case $TYPE in
    graffiti)
        PROMPT=$(sd prompt "${SPLIT_LINES[$j]}" --rendering_engine "Octane Render" --lightning_style "Cinematic" --resolution "8k" --compel_style "subtle")
        ARGS="--input $WORKING_DIR/$IMAGE --controlnet_model "artificialhoney/graffiti" --controlnet_conditioning_scale $CONTROLNET_CONDITIONING_SCALE"
        ;;
    spawn)
        PROMPT=$(sd prompt "Spawn in a battle, ${SPLIT_LINES[$j]}" --time "Modern" --type "Comic Book" --artist "H.R. Giger" --art_style "Concept Art" --realism "Photorealistic" --rendering_engine "Octane Render" --lightning_style "Cinematic" --camera_position "Ultra-Wide-Angle Shot" --resolution "8k")
        ;;
    gravedigger)
        PROMPT=$(sd prompt "${SPLIT_LINES[$j]}" --time Modern --type "Comic Book" --art_style "Concept Art" --artist "William Blake" --realism "Photorealistic" --rendering_engine "Octane Render" --lightning_angle "Back Light" --lightning_style "Cinematic" --camera_position "Full-Body Shot" --style "Long Exposure" --resolution "8k" --compel_style "subtle")
        ;;
    vampire)
        # PROMPT=$(sd prompt "${SPLIT_LINES[$j]}" --time Ancient --type "Comic Book" --background_color "#000000" --art_style "Concept Art" --artist "H.R. Giger" --realism "Photorealistic" --rendering_engine "Octane Render" --lightning_angle "Front Light" --lightning_style "Cinematic" --camera_position "Full-Body Shot" --style "Long Exposure" --resolution "8k")
        PROMPT=$(sd prompt "${SPLIT_LINES[$j]}" --time Modern --type "Comic Book" --art_style "Concept Art" --artist "Banksy" --realism "Photorealistic" --rendering_engine "Octane Render" --lightning_angle "Front Light" --lightning_style "Cinematic" --camera_position "Full-Body Shot" --style "Long Exposure" --resolution "8k")
        ;;
    viking)
        PROMPT=$(sd prompt "${SPLIT_LINES[$j]}" --time Ancient --type "Comic Book" --art_style "Concept Art" "Dieselpunk" --artist "Frank Miller" --realism "Photorealistic" --rendering_engine "Octane Render" --lightning_angle "Back Light" --lightning_style "Cinematic" --camera_position "Full-Body Shot" --style "Long Exposure" --resolution "8k" --compel_style "subtle")
        ;;
    *)
        echo "No type specified. Exiting!"
        exit 0
        ;;
    esac

    render "$PROMPT" "$ARGS"
done
