#!/bin/bash

# Variables
# ------------------
#
# SESSION     - The name of the tmux sessions running the minecraft server
#
SESSION="twitterReadr"


# Verify server is not running
if tmux list-sessions 2>&1 | grep -q $SESSION; then
	echo "Server is already running!"
	exit 1
fi

# Setup ramdisk
#echo "Loading ramdisk..."
#rsync -a --delete-after $GAME_FILES $RAMDISK
#echo "Ramdisk loaded."

# Start server
echo "Executing server start command..."
# Note: Must first change directory into the ramdisk so that the 'eula.txt'
#       is found. Minecraft expects it to be in the directory which the java
#       command to start the server is called.

# shellcheck disable=SC2027
tmux new -d -s twitterReadr "python3 ./bin/main.py"

echo "done."
exit 0