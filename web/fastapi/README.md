不搭建给外部使用的负载均衡情况下，直接起一个web服务器，把外部流量导转到内部k8s集群

# heatup python environment
```
virtualenv .venv 
source .venv/bin/activate
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ 
```