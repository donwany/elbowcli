#!/bin/bash

python app.py \
    --epochs 200 \
    --lr 0.005 \
    --model "RandomForest" \
    --square 25 \
    --output config.csv \
    --verbosity 2

python app.py \
    --epochs 500 \
    --lr 0.003 \
    --model "LogisticRegression" \
    --square 500 \
    --output config.csv \
    --verbosity 1