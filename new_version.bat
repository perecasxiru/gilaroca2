@ECHO OFF
git pull
python newversion.py
git add .
git commit -m "new stats"
git push
