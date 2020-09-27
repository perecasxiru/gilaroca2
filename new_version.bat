@ECHO OFF
git pull
cd C:\Users\perec\Documents\GithubWebs\gilaroca2
python newversion.py
git add .
git commit -m "new stats"
git push
