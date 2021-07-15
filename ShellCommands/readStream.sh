#!/bin/bash

SESSION="twitterReadr"

tmux capture-pane -t $SESSION
#
#"{(\n.*\n*)*}"
tmux show-buffer | grep "{.*}"| cat
