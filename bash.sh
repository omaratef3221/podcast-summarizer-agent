#!/bin/bash

LOGFILE=~/podcast_summarizer_run.log
LAST_RUN_FILE=~/last_podcast_summarizer_run.txt
CONDA_PATH="$HOME/miniconda"
ENV_NAME="podcast_summarizer"
WORKDIR="/Users/omaratef/Dropbox/Projects/AI/Podcast_summarizer/summarizer_container"

{
    echo "=== $(date): Script started ==="

    # Check last run time
    if [ -f "$LAST_RUN_FILE" ]; then
        LAST_RUN=$(date -j -f "%s" "$(stat -f %m "$LAST_RUN_FILE")" +%s)
        NOW=$(date +%s)
        DIFF=$(( (NOW - LAST_RUN) / 86400 ))
        if [ "$DIFF" -lt 3 ]; then
            echo "Skipped: last run was $DIFF day(s) ago."
            exit 0
        fi
    fi

    # Load conda
    source "$CONDA_PATH/etc/profile.d/conda.sh"
    conda activate "$ENV_NAME" || {
        echo "Failed to activate conda env: $ENV_NAME"
        exit 1
    }

    # Move to the correct directory
    cd "$WORKDIR" || {
        echo "Failed to change directory to $WORKDIR"
        exit 1
    }

    # Run script
    if python run_all.py; then
        echo "Script ran successfully"
        date +%s > "$LAST_RUN_FILE"
    else
        echo "Python script failed"
        exit 1
    fi

    echo "=== $(date): Script finished ==="
} >> "$LOGFILE" 2>&1
