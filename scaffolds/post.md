---
title: {{ title }}
date: {{ date }}
tags:
categories:
mathjax: true
cover: 
sticky: 
---

<!--more-->







// audio-play
{% aplayer "Caffeine" "Jeff Williams" "caffeine.mp3" "picture.jpg" "lrc:caffeine.txt" %}
{% aplayer "" "" "" %}

// audio-page-lyric-play
{% aplayerlrc "title" "author" "url" "autoplay" %}
[00:00.00]lrc here
{% endaplayerlrc %}


// video-play
{% dplayer "" "autoplay=true" %}




## tabs

{% tabs test1 %} 
<!-- tab --> 
**This is Tab 1.**
 <!-- endtab -->

<!-- tab --> 
**This is Tab 2.**
 <!-- endtab -->

<!-- tab --> 
**This is Tab 3.**
 <!-- endtab --> 
{% endtabs %}

---

## button

{% btn [url],[text],[icon],[color] [style] [layout] [position] [size] %}

[url] :链接
[text] :按钮文字
[icon] : [可选]图标
[color] : [可选]按钮背景颜色(默认style时）
                      按钮字体和边框颜色(outline时) 
                      default/blue/pink /red/purple/orange/green 
[style] : [可选]按钮样式默认实心
                      outline/留空
[layout] : [可选]按钮布局默认为line 
                      block/留空
[position] : [可选]按钮位置前提是设置了layout为block默认为左边
                      center/right/留空
[size] : [可选]按钮大小
                      larger/留空

---

## inline图片 

{% inlineImg [src] [height] %}

[src] :图片链接
[height] ：图片高度限制【可选】

---

## 文字高亮

{% label text color %}

---




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