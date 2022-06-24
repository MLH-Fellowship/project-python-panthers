tmux kill-server
cd .\project-python-panthers\
git fetch
git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new -s myportfolio 
flask run --host=0.0.0.0;