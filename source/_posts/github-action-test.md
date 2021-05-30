---
title: GitHub Actions 自动部署 Hexo
date: 2021-05-30 16:27:31
tags: blog hexo
categories: 转载
---

# GitHub Actions 自动部署 Hexo

[Github Actions](https://github.com/features/actions) 是 GitHub 官方 CI 工具，与 GitHub 无缝集成。之前博客使用 TravisCI 实现的自动部署，现在转用 GitHub Actions 部署，本文记录部署流程。

![Modify0521](https://fred-pic1.oss-cn-beijing.aliyuncs.com/picgo_imgModify0521.jpg)





---

<!--more-->

[![img](https://raw.githubusercontent.com/lujiahao0708/PicRepo/master/blogPic/Hexo/GithHub Actions.png)](https://raw.githubusercontent.com/lujiahao0708/PicRepo/master/blogPic/Hexo/GithHub Actions.png)

简单介绍下 GitHub Actions 中的术语：

- workflow：表示一次持续集成的过程
- job：构建任务，一个 workflow 可以由一个或者多个 job 组成，可支持并发执行 job
- step：一个 job 由一个或多个 step 组成，按顺序依次执行
- action：每个 step 由一个或多个 action 组成，按顺序依次执行

------

接下来介绍下操作步骤：

# 1.博客工程

GitHub 博客创建步骤非本文重点，请自行搜索。
推荐使用 `master` 分支作为最终部署分支，源码分支可以根据自己喜好创建，我这里创建的是 `hexo`。

# 2.生成公私钥

源码分支中通过下面命令生成公钥和私钥。

```
~ cd github/lujiahao0708.github.io 
~ git checkout hexo
~ ssh-keygen -t rsa -b 4096 -C "$(git config user.email)" -f github-deploy-key -N ""
```

目录中生成两个文件：

- `github-deploy-key.pub` — 公钥文件
- `github-deploy-key` — 私钥文件

> 公钥和私钥切记要添加到 `.gitignore` 中！！！

# 3.GitHub 添加公钥

在 GitHub 中博客工程中按照 `Settings->Deploye keys->Add deploy key` 找到对应的页面，然后进行公钥添加。该页面中 `Title` 自定义即可，`Key` 中添加 `github-deploy-key.pub` 文件中的内容。

[![img](https://raw.githubusercontent.com/lujiahao0708/PicRepo/master/blogPic/Hexo/GitHub Actions 添加公钥.png)](https://raw.githubusercontent.com/lujiahao0708/PicRepo/master/blogPic/Hexo/GitHub Actions 添加公钥.png)

> 注意：切记不要多复制空格!!!
> 切记要勾选 `Allow write access`，否则会出现无法部署的情况。

# 4.GitHub 添加私钥

在 GitHub 中博客工程中按照 `Settings->Secrets->Add a new secrets` 找到对应的页面，然后进行私钥添加。该页面中 `Name` 自定义即可，`Value` 中添加 `github-deploy-key` 文件中的内容。

[![img](https://raw.githubusercontent.com/lujiahao0708/PicRepo/master/blogPic/Hexo/GitHub Actions 添加私钥.png)](https://raw.githubusercontent.com/lujiahao0708/PicRepo/master/blogPic/Hexo/GitHub Actions 添加私钥.png)

> 注意：切记不要多复制空格!!!

# 5.创建编译脚本

在博客源码分支(我这里是hexo分支)中创建 `.github/workflows/HexoCI.yml` 文件，内容如下：

```
name: CI
on:
  push:
    branches:
      - hexo
jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout source
        uses: actions/checkout@v1
        with:
          ref: hexo
      - name: Use Node.js ${{ matrix.node_version }}
        uses: actions/setup-node@v1
        with:
          version: ${{ matrix.node_version }}
      - name: Setup hexo
        env:
          ACTION_DEPLOY_KEY: ${{ secrets.HEXO_DEPLOY_PRI }}
        run: |
          mkdir -p ~/.ssh/
          echo "$ACTION_DEPLOY_KEY" > ~/.ssh/id_rsa
          chmod 600 ~/.ssh/id_rsa
          ssh-keyscan github.com >> ~/.ssh/known_hosts
          git config --global user.email "lujiahao0708@gmail.com"
          git config --global user.name "lujiahao0708"
          npm install hexo-cli -g
          npm install
      - name: Hexo deploy
        run: |
          hexo clean
          hexo d
```

# 6.Hexo 配置

在项目根目录中修改 `_config.yml` ，增加部署相关内容：

```
deploy:
  type: git
  repo: git@github.com:lujiahao0708/lujiahao0708.github.io.git
  branch: master
```

> 这里的repo要填写ssh的形式，使用http形式可能会有问题

# 7.验证

现在 Hexo 已经和 GitHub Actions 已经集成了，接下来在博客源码分支上推送代码即可自动编译部署。具体
执行过程可以在 `Actions` 中查看：

[![img](https://raw.githubusercontent.com/lujiahao0708/PicRepo/master/blogPic/Hexo/GitHub Actions 部署结果.png)](https://raw.githubusercontent.com/lujiahao0708/PicRepo/master/blogPic/Hexo/GitHub Actions 部署结果.png)

> 欢迎访问我的博客：https://lujiahao0708.github.io/