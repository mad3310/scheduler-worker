FROM letv:centos6
MAINTAINER bingzheng.zhou <zhoubingzheng@letv.com>

RUN rpm -ivh http://pkg-repo.oss.letv.com/pkgs/centos6/letv-release.noarch.rpm
RUN yum install scheduler-worker -y
RUN yum update bash -y

USER root

ENTRYPOINT service scheduler-worker start && /bin/bash