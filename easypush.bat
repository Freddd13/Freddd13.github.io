call hexo bangumi -u
call cd source/_data
call python convert.py
call cd ../..
call git add .
call git commit -m "auto push"
call git push origin hexo
pause