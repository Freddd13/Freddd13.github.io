@echo off
if not defined TAG (
    set TAG=1
    start wt -p "cmd" %0
    :: Windows Terminal 中 cmd 的配置名，我这里是“cmd”
    exit
)

chcp 65001
:: 用 vscode 写的，默认编码是 utf-8
hexo clean & hexo d -g
mv .gitignore .gitignorebak
git add .
git commit -m "backup"
git push origin hexo
mv .gitignorebak .gitignore 
dir
pause