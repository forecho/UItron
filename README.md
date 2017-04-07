# UItron
奥创

## 安装环境


安装 python3.2.2 以上

```
sudo curl https://bootstrap.pypa.io/get-pip.py | python3
```

ubuntu

```
sudo apt-get install libxml2-dev libxslt-dev python-dev
sudo apt-get install python3-lxml
```

or centos
```
sudo yum install libxslt-devel libxml2-devel
sudo yum install python-lxml
```

包

```
sudo pip3 install lxml
sudo pip3 install requests
sudo pip3 install beautifulsoup4
sudo pip3 install pyyaml
```

## 使用方法

复制配置文件，并且修改

```
cp config.yml.example config.yml
```

然后执行

```
python3 app.py
```

## 部署

```
sudo pip3 install gunicorn
sudo pip3 install falcon
```