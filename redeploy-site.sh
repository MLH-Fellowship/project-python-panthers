#!/bin/bash
cd project-python-panthers

/usr/bin/git fetch && /usr/bin/git reset origin/main --hard

source python3-virtualenv/bin/activate

pip install -r requirements.txt

systemctl restart myportfolio
