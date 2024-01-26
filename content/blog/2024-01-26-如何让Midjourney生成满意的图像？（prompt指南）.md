+++
title = "如何让Midjourney生成满意的图像？（prompt指南）"
+++
# 如何让Midjourney生成满意的图像？（prompt指南）

Tags: AI, 技术
Last edited: April 21, 2023 4:37 PM

## 前言

刚开始使用Midjourney时，很难让AI准确生成出脑子里的模糊形象。这是因为我们无法用文本准确描述出来脑海里的模糊图像。没有准确的文本描述（即prompt），AI就会天马行空随意发挥，大多数时候都会让你疑惑“哎？怎么会生成这样的图片？”。想要让AI生成的图像合乎心意，了解基本的prompt是必要的。

### 文本描述基本结构：

**内容描述 + 风格描述 + 属性描述**

> 内容描述：画面主体内容，要画什么。是人是动物，做什么动作，穿什么衣服等
风格描述：指定艺术家风格，画笔风格，艺术风格，打光，视角等
属性描述：图片属性，尺寸，分辨率等
> 

### 内容描述

描述你想要绘制的内容，越详细越好。

一个示例：一只猫猫（画面主体）正在打架（动作）猫猫头上戴着头盔（画面主体详细描述）猫猫在擂台上（画面背景）

### 以某张图片为基础生成

你也可以选择参考图片，让Midjourney参考这张图片生成。

方式是：将图片上传至discord，

![Untitled](%E5%A6%82%E4%BD%95%E8%AE%A9Midjourney%E7%94%9F%E6%88%90%E6%BB%A1%E6%84%8F%E7%9A%84%E5%9B%BE%E5%83%8F%EF%BC%9F%EF%BC%88prompt%E6%8C%87%E5%8D%97%EF%BC%89%20893ddafcf14c464ba76ef3ca310f321e/Untitled.png)

点击图片，在浏览器中打开，

![Untitled](%E5%A6%82%E4%BD%95%E8%AE%A9Midjourney%E7%94%9F%E6%88%90%E6%BB%A1%E6%84%8F%E7%9A%84%E5%9B%BE%E5%83%8F%EF%BC%9F%EF%BC%88prompt%E6%8C%87%E5%8D%97%EF%BC%89%20893ddafcf14c464ba76ef3ca310f321e/Untitled%201.png)

然后把图片网址粘贴到prompt里面，

![Untitled](%E5%A6%82%E4%BD%95%E8%AE%A9Midjourney%E7%94%9F%E6%88%90%E6%BB%A1%E6%84%8F%E7%9A%84%E5%9B%BE%E5%83%8F%EF%BC%9F%EF%BC%88prompt%E6%8C%87%E5%8D%97%EF%BC%89%20893ddafcf14c464ba76ef3ca310f321e/Untitled%202.png)

最后设定相似程度`--iw 0.25-5` （默认1.25，数值越大参考原图比重越多）(注意version 4 版本无法设定相似程度，改成version 3就好）

![Untitled](%E5%A6%82%E4%BD%95%E8%AE%A9Midjourney%E7%94%9F%E6%88%90%E6%BB%A1%E6%84%8F%E7%9A%84%E5%9B%BE%E5%83%8F%EF%BC%9F%EF%BC%88prompt%E6%8C%87%E5%8D%97%EF%BC%89%20893ddafcf14c464ba76ef3ca310f321e/Untitled%203.png)

最终成果

![Untitled](%E5%A6%82%E4%BD%95%E8%AE%A9Midjourney%E7%94%9F%E6%88%90%E6%BB%A1%E6%84%8F%E7%9A%84%E5%9B%BE%E5%83%8F%EF%BC%9F%EF%BC%88prompt%E6%8C%87%E5%8D%97%EF%BC%89%20893ddafcf14c464ba76ef3ca310f321e/Untitled%204.png)

### 风格描述

- 艺术家（”by [artists]”）： van Gogh （梵高），alphonse mucha（阿尔丰斯·穆夏）basquiat（尚·米榭·巴斯奇亚）
- 艺术风格：pop art （通俗艺术）surrealism（超现实主义）realism（现实主义）symbolism（象征主义）cyberpunk（赛博朋克）gothic（哥特式）
- 绘画类型：oil paintings（油画）、portraits（肖像）、watercolor paintings（水彩画）、pencil drawing（铅笔画）、charcoal sketch（炭笔素描）、etching（蚀刻）、cartoon（卡通）、concept art（概念艺术）、posters（海报）、stickers（贴纸）、 tattoos(刺青)、landscape(风景)、black and white photograph（黑白照片）
- 光线：golden hour（黄金时刻）、studio lighting（演播室照明）、natural lighting（自然光）、cinematic lighting (电影光)
- 分辨率：4K，8K，8bit
- 摄影：studio photography（棚内摄影）、polaroid（宝丽来）、camera phone（手机摄像头）
- 相机设置：macro（微距）、wide angle（广角）、ultra wide shot(超宽镜头)、fish-eye（鱼眼）、motion blur（动态模糊）、close up（特写）等
- 质量提升：highly-detailed（高清细节）rendered in Unreal Engine（用虚幻引擎渲染）trending on artstation（流行艺术）

### 属性描述

- 指定版本  `--v 1/2/3/4`    （越大的版本越写实）
- 负面提示词  `--no something` （`—-no dog` 画面中不要出现狗）
- 质量 `--q .25/.5/1/2`  （默认1，越大需要的渲染时间越长）
- 图片比例 `--ar 2:3/3:2/16:9`  （注意—v 4版本只支持2：3和3：2）
- 混乱度chaos  `--c 0-100`  （默认0，数值越大画面越飞）

### 即用prompt

- 适用于壁纸：
    
     `ultra wide shot, atmospheric, hyper realistic, 8k, epic composition, cinematic, octane render, artstation landscape vista photography by Carr Clifton & mid, 16K resolution, Landscape veduta photo by Dustin Lefevre & tdraw, 8k resolution, detailed landscape painting by Ivan Shishkin, DeviantArt, Flickr, rendered in Enscape, Miyazaki, Nausicaa Ghibli, Breath of The Wild, 4k detailed post processing, artstation, rendering by octane, unreal`
    

## 示例

`An orange cat wearing a helmet poses in a boxing ring , by Robert McCall, gothic, posters, cinematic lighting, close up, highly-detailed --q 2`

 `An orange cat wearing a helmet poses in a boxing ring`   橙色的猫戴着头盔在拳击擂台上摆出架势 （内容描述）

`by Robert McCall, gothic, posters, cinematic lighting, close up, highly-detailed` 罗伯特·麦克科尔的风格，哥特式，海报风格，电影打光，人物特写，高度详细 （风格描述）

`--q 2`  设定质量为2 （属性描述）

![Untitled](%E5%A6%82%E4%BD%95%E8%AE%A9Midjourney%E7%94%9F%E6%88%90%E6%BB%A1%E6%84%8F%E7%9A%84%E5%9B%BE%E5%83%8F%EF%BC%9F%EF%BC%88prompt%E6%8C%87%E5%8D%97%EF%BC%89%20893ddafcf14c464ba76ef3ca310f321e/Untitled%205.png)

### logo

Close up of simple minimalist dog logo with thick black and white outline style, smooth edges, 2d, icon style, simple design, simple colouring, one color, behance, dribbble, simplistic details --v 5

2d, flat, corporate logo, minimalistic logo ::2 simple line, edgy, lion head ::5 with blue, red, green and gold, white background --stylize 1000

### 3D效果

A glass material transparent airpods on the Dark background, in the style of light purple and light amber, in the style of post processing, soft color blending, white background, manapunk, adafruit, elegant, emotive faces, simple oshare kei, resin, light red and light purple, contrasting values , bauhaus photography, bold and vibrant primary colors, metallic

### 人物

[https://s.mj.run/O2I9wpT319A](https://s.mj.run/O2I9wpT319A) A Chinese girl in a light blue short-sleeved shirt, Standing alone in an empty classroom, The afternoon sun hit her in the face through the window, brown hair, black hair, hair between eyes, Smile, chiaroscuro, cinematic lighting, feet out of frame, first-person view, f/1.8, 85mm, Sony FE, UHD, anatomically correct, textured skin

[https://s.mj.run/Me9H0sCP6tc](https://s.mj.run/Me9H0sCP6tc) as a anime girl figure dressed in blue, black and orange, in the style of charming anime characters, hyper-detailed, grey academia, gamercore, dark yellow and cyan, aquirax uno, omri koresh, 3D render, Blender render, realistic, cinematic lighting

### 建筑

Small and cute urban laboratory,3d blender render,soft smooth lighting,rain background,100mm lens,4k UHD,isometric,tilt-shift

### 动物

a cute and sweet pixar style white fairy baby dog, sweet smile, small Peach bloson around, wearing a big headphone, smile, enjoying music, In the background is the bright bedroom, clean sunshine, enchanting, hairy, shiny mane, petals, fairy tales, wearing a pink sweater, incredibly high detail, Pixar-style, bright colors, natural light, sofawink background, Octane render, popular on artstation, gorgeous, ultra wide Angle, 8k, HD realistic, 8k HD

### 静物

Hand painted photography canvas textured backdrops with a lot of little ethereal florals, Chinese floral painting style, 4k, wide angle, white, cream and tan colors with gold accents, white baby breath spray detail, Rococo style, no people

### 动漫风格

Makoto Shinkai animation style, In spring, a little boy, three years old, lay on his hands and knees in the grass, looking for worms, there were lots of flowers, rocks, beetle, butterfly, dead wood, huge mushrooms, hopeful, bright colours, animation light, high detail, hyper quality, high resolution, ultra-detail, the best picture quality, masterpiece, 16K, beautiful scene,

### 贴纸

set of 9 donuts cute sticker doodel colorful, sticker art design, illustration, flat colors, simple lines, graphic novel style, 2d painting, ink painting style, trending on art station, digital art, childrens character design, happy mood, watercolor, pixar style cartoon, line work, minimalist

### 利用AI自己生成prompt

你还可以用chatGPT帮你写prompt，真正实现从AI到AI一条龙。

1. 基本描述
2. Notion AI 扩句
3. 文本图像生成

## 更进一步

上面的prompt还不够？想要更多？下面这个由Michael Taylor整理的prompt文档满足你：

数据集：**[PROMPT ENGINEERING TEMPLATE](https://docs.google.com/spreadsheets/d/1-snKDn38-KypoYCk9XLPg799bHcNFSBAVu2HVvFEAkA/edit?usp=sharing)**

## 参考

**[Prompt Engineering: From Words to Art](https://www.saxifrage.xyz/post/prompt-engineering)**

**[An advanced guide to writing prompts for Midjourney ( text-to-image)](https://medium.com/mlearning-ai/an-advanced-guide-to-writing-prompts-for-midjourney-text-to-image-aa12a1e33b6)**