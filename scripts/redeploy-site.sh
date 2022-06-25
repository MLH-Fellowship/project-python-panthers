cd project-python-panthers/
git fetch
git reset origin/main --hard
source python3-virtualenv/bin/activate
systemctl daemon-reload
systemctl restart myportfolio
