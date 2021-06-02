call hexo bangumi -u
call cd source/_data
call python convert.py
call cd ../..
git add .
git commit -m "auto push"
git push origin hexo
pause
