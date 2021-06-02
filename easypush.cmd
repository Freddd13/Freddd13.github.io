@echo off
hexo bangumi -u
cd source/_data
python convert.py
cd ../..
git add .
git commit -m "auto push"
git push origin hexo
pause
