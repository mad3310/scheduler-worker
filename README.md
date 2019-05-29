# scheduler-worker

## Introduction
定时任务中心-worker执行端

## Build
在项目目录下执行，python setup.py bdist_rpm，执行操作后，可以看到在dist中产出三个rpm包，可以将noarch.rpm上传到yum源。每次版本更迭后，请注意修改版本号，版本号和release编号在setup.py文件中修改。

## Install and Deploy
通过yum的方式在需要部署的机器上进行安装。 在本地的安装中也可以使用yum命令，yum install schedulerworker-1.0.0-1.noarch.rpm

## Usage
* 启动：
cd /usr/lib/python2.7/site-packages/<br>
python schedulerworker/run.py &

* 关闭：
找到相应的python进程，使用kill -5 {pid}

## Change Log
### Add

### Change

### Fix

## More Infomation
公司Open-falcon的推送地址：
http://10.58.47.66:1987/v1/push

供应链整体在监控系统的endpoint名称：scm-monitor

在open-falcon的页面通过查询scm-monitor的关键字，可以列出关于供应链各系统的监控指标。在scheduler-center的添加任务接口中提供的project code与task name的组合会在open-falcon中单独作为一个监控项。点击进入可以看到服务的监控图。通过转换规则，程序已将信息转为数字类型，目前是0和1，1代表正常，0代表异常，后期可以添加在出现0时的报警策略。
## TODO

## License
MIT
