#               tub


## tub use baidu  命令行翻译脚本^ _ ^


## 介绍
使用百度翻译api接口，在命令行使用python脚本翻译

## 依赖：
- python3
- 百度翻译开放平台申请appid和秘钥，链接[百度翻译开放平台](https://fanyi-api.baidu.com/api/trans/product/desktop)

## 安装：
- 首先在新建一个文件夹，建议在工作区目录下。这边我是在~/workspace/app目录下新建的文件夹，命令：` mkdir tub `
- 然后进入新建的目录下，命令：` cd tub `
- 下载源码，命令：` git clone git@github.com:ZZP-DMU/tub.git `
- 创建虚拟环境所在文件夹，在tub目录下创建文件夹，这里命名为venv,命令：` mkdir venv`
- 创建虚拟环境，命令：` python3 -m venv ./venv `
- 修改tub文件，在tub文件第一行修改为`#!../venv/bin/python3`
- 安装必要的工具包，命令：` python3 -m pip install requests`
- 设置环境变量，对于bash，命令：` echo "export PATH='PATH:~/workspace/app/tub'" >> ~/.bashrc `;对于zsh，只需要将.bashrc改为.zshrc
- 现在即可在命令行输入tub命令，初次运行需要设置自己的appid和秘钥，即在依赖中所提到的

## 用法：

![image](https://user-images.githubusercontent.com/82870401/208221224-a86d9002-22c2-4f7e-8d80-f11af4cddfcc.png)

## 用法案例：

翻译英文：` tub -c [english_word] `

![image](https://user-images.githubusercontent.com/82870401/208221043-6c607fc8-3ee3-4038-9e3b-dd6fe08b2e00.png)


翻译中文：` tub -e [chinese_word] ` 

![image](https://user-images.githubusercontent.com/82870401/208221065-1853e874-0285-4d31-bbe9-b2c4167ea47e.png)

在` tub zh to en(? or puss 'q' to quit) `提示后，命令` q `退出，` cl `改变语言，` cm `改变输出方式，` clr `清除屏幕，直接输入单词继续翻译

![image](https://user-images.githubusercontent.com/82870401/208221162-a3cde2a3-080e-4890-b501-9fa0064cd4bb.png)
