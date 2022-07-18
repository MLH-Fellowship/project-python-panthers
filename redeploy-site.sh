
#!/bin/bash

# Kill existing tmux sessions
# tmux kill-server

# Go into folder
# cd project-python-panthers

# Make sure site is up to date from VCS
git fetch && git reset origin/main --hard

docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build

# Enter python venv and install dependencies
# source python3-virtualenv/bin/activate

# Install requirements
# pip install -r requirements.txt

# Start Flask in a detached tmux session
# tmux new-session -d -s Flask
# tmux send-keys 'source python3-virtualenv/bin/activate' C-m
# tmux send-keys 'flask run --host=0.0.0.0' C-m
