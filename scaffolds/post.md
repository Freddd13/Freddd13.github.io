---
title: {{ title }}
date: {{ date }}
tags:
categories: 
password: 
abstract: 有东西被加密了, 请输入密码查看.
message: 您好, 这里需要密码.
wrong_pass_message: 抱歉, 这个密码看着不太对, 请再试试.
wrong_hash_message: 抱歉, 这个文章不能被校验, 不过您还是能看看解密后的内容.
---

// audio-play
{% aplayer "Caffeine" "Jeff Williams" "caffeine.mp3" "picture.jpg" "lrc:caffeine.txt" %}
{% aplayer "" "" "" %}

// audio-page-lyric-play
{% aplayerlrc "title" "author" "url" "autoplay" %}
[00:00.00]lrc here
{% endaplayerlrc %}


// video-play
{% dplayer "" "autoplay=true" %}


<!--more-->






// audio-list
{% aplayerlist %}
{
    "narrow": false,                          // （可选）播放器袖珍风格
    "autoplay": true,                         // （可选) 自动播放，移动端浏览器暂时不支持此功能
    "mode": "random",                         // （可选）曲目循环类型，有 'random'（随机播放）, 'single' (单曲播放), 'circulation' (循环播放), 'order' (列表播放)， 默认：'circulation' 
    "showlrc": 3,                             // （可选）歌词显示配置项，可选项有：1,2,3
    "mutex": true,                            // （可选）该选项开启时，如果同页面有其他 aplayer 播放，该播放器会暂停
    "theme": "#e6d0b2",	                      // （可选）播放器风格色彩设置，默认：#b7daff
    "preload": "metadata",                    // （可选）音乐文件预载入模式，可选项： 'none' 'metadata' 'auto', 默认: 'auto'
    "listmaxheight": "513px",                 // (可选) 该播放列表的最大长度
    "music": [
        {
            "title": "CoCo",
            "author": "Jeff Williams",
            "url": "caffeine.mp3",
            "pic": "caffeine.jpeg",
            "lrc": "caffeine.txt"
        },
        {
            "title": "アイロニ",
            "author": "鹿乃",
            "url": "irony.mp3",
            "pic": "irony.jpg"
        }
    ]
}
{% endaplayerlist %}


// dplayer-detail
{
    container: "you needn't set this",
    autoplay: 'autoplay',
    theme: 'theme',
    loop: 'loop',
    lang: 'lang',
    screenshot: 'screenshot',
    hotkey: 'hotkey',
    preload: 'preload',
    logo: 'logo',
    volume: 'volume',
    mutex: 'mutex',
    video: {
        url: 'url',
        pic: 'pic',
        thumbnails: 'thumbnails',
        type: 'vidtype',
    },
    subtitle: {
        url: 'suburl',
        type: 'subtype',
        fontSize: 'subsize',
        bottom: 'subbottom',
        color: 'subcolor',
    },
    danmaku: {
        id: 'id',
        api: 'api',
        token: 'token',
        maximum: 'maximum',
        addition: ['addition'],
        user: 'dmuser',
        unlimited: 'dmunlimited',
    },
    icons: 'icons',
    contextmenu: 'menu',
}