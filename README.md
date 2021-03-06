# My k8s cheatsheet

- [My k8s cheatsheet](#my-k8s-cheatsheet)
- [1. 获取最新 API version](#1-获取最新-api-version)
- [2. master也参与调度](#2-master也参与调度)
- [3. 获取labels](#3-获取labels)
- [4. 获取所有namespaces的pods](#4-获取所有namespaces的pods)
- [5. 拿到类似yaml配置文件的信息](#5-拿到类似yaml配置文件的信息)
- [6. 跑一个临时busybox容器](#6-跑一个临时busybox容器)
- [7. 重启coredns](#7-重启coredns)
- [8. kubeadm reset](#8-kubeadm-reset)
- [9. kubeadm join](#9-kubeadm-join)
- [10. Kubernetes 修改 kube-porxy 为ipvs 模式](#10-kubernetes-修改-kube-porxy-为ipvs-模式)
- [11. tcpdump抓包](#11-tcpdump抓包)
- [12. 外网快速访问dashboard（不安全）](#12-外网快速访问dashboard不安全)
- [13. 对外暴露服务，使用端口转发（只适合临时测试用，不安全）](#13-对外暴露服务使用端口转发只适合临时测试用不安全)
- [14. 对外暴露服务，通过NodePort](#14-对外暴露服务通过nodeport)

# 1. 获取最新 API version
```
for kind in `kubectl api-resources | tail +2 | awk '{ print $1 }'`; do kubectl explain $kind; done | grep -e "KIND:" -e "VERSION:"
```

# 2. master也参与调度
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
kubectl get pods -A
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

# 10. Kubernetes 修改 kube-porxy 为ipvs 模式
https://chenjiandongx.me/2021/02/06/k8s-ipvs-mode/


# 11. tcpdump抓包
```
tcpdump -i flannel.1
```

# 12. 外网快速访问dashboard（不安全）
```
kubectl proxy --address='0.0.0.0' -p 9999 --disable-filter=true
http://{internet_ip}:9999/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
```
```
https://github.com/kubernetes/dashboard/blob/master/docs/user/accessing-dashboard/README.md
```

# 13. 对外暴露服务，使用端口转发（只适合临时测试用，不安全）
```
kubectl port-forward --address 0.0.0.0 svc/test-k8s 8090:8090
```

# 14. 对外暴露服务，通过NodePort
```yaml
apiVersion: v1
kind: Service
metadata:
  name: test-k8s
spec:
  selector:
    app: test-k8s
  # 默认 ClusterIP 集群内可访问，NodePort 节点可访问，LoadBalancer 负载均衡模式（需要负载均衡器才可用）
  type: NodePort
  ports:
    - port: 8090        # 本 Service 的端口
      targetPort: 8080  # 容器端口
      nodePort: 31000   # 节点端口，范围固定 30000 ~ 32767
```
