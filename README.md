# My k8s cheatsheet

- [My k8s cheatsheet](#my-k8s-cheatsheet)
- [1. 获取最新 API version](#1-获取最新-api-version)
- [2. 把pod调度到master或者不调度到master](#2-把pod调度到master或者不调度到master)
- [3. 获取labels](#3-获取labels)
- [4. 获取所有namespaces的pods](#4-获取所有namespaces的pods)
- [5. 拿到类似yaml配置文件的信息](#5-拿到类似yaml配置文件的信息)
- [6. 跑一个临时busybox容器](#6-跑一个临时busybox容器)
- [7. 重启coredns](#7-重启coredns)
- [8. kubeadm reset](#8-kubeadm-reset)
- [9. kubeadm join](#9-kubeadm-join)

# 1. 获取最新 API version
```
for kind in `kubectl api-resources | tail +2 | awk '{ print $1 }'`; do kubectl explain $kind; done | grep -e "KIND:" -e "VERSION:"
```

# 2. 把pod调度到master或者不调度到master
为什么要调度到master: 因为我只有两个node去学习

所有nodes参与调度
```
kubectl taint nodes --all node-role.kubernetes.io/master-
```
关闭master节点的调度
```
kubectl taint node {masterName} node-role.kubernetes.io/master=:NoSchedule
```

# 3. 获取labels
```
kubectl get pods --show-labels
```
```
kubectl get nodes --show-labels
```

# 4. 获取所有namespaces的pods
```
kubectl get pods --all-namespaces
```

# 5. 拿到类似yaml配置文件的信息
```
kubectl edit daemonset kube-proxy --namespace=kube-system
```

# 6. 跑一个临时busybox容器
```
kubectl run busybox --rm -it --image=busybox /bin/sh
```

# 7. 重启coredns
```
kubectl rollout restart -n kube-system deployment/coredns
```

# 8. kubeadm reset
```
kubeadm reset

systemctl stop kubelet

systemctl stop docker

rm -rf /var/lib/cni/

rm -rf /var/lib/kubelet/

rm -rf /etc/cni/

ifconfig cni0 down

ifconfig flannel.1 down

ifconfig docker0 down

ip link delete cni0

ip link delete flannel.1

systemctl start kubelet

systemctl start docker
```

# 9. kubeadm join
```
kubeadm token create --print-join-command
```