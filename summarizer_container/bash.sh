#!/bin/bash

LOGFILE=~/podcast_summarizer_run.log
CONDA_PATH="$HOME/miniconda3"  # or change to your conda path
ENV_NAME="podcast_summarizer"

{
    echo "=== $(date): Script started ==="

    # Load conda
    source /Users/omaratef/miniconda/etc/profile.d/conda.sh
    conda activate "$ENV_NAME" || {
        echo "Failed to activate conda env: $ENV_NAME"
        exit 1
    }

    # Run Python script
    if python run_all.py; then
        echo "Script ran successfully"
    else
        echo "Python script failed"
        exit 1
    fi

    echo "=== $(date): Script finished ==="
} >> "$LOGFILE" 2>&1
