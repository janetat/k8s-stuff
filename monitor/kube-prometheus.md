# Install kube-prometheus
- [Install kube-prometheus](#install-kube-prometheus)
- [Link](#link)
- [下载源码](#下载源码)
- [换源](#换源)
- [部署](#部署)
- [查看结果](#查看结果)
- [通过port-forward让公网快速访问](#通过port-forward让公网快速访问)

# Link
https://prometheus-operator.dev/docs/prologue/quick-start/


# 下载源码
```
git clone git@github.com:prometheus-operator/kube-prometheus.git
```
```
cd kube-prometheus/
```

# 换源
GCR镜像源在不科学代理的情况下，永远的痛。但不是没有办法，在dockerhub一个一个找，肯定有热心用户已经sync过gcr的镜像了，只是担心安全问题。
因为部分镜像源是gcr的，然后的我使用镜像站是DaoCloud或者阿里云，只代理dockerhub，不代理gcr。
所以直接在docker hub上面找一下所需要的镜像
```
cd manifests/
```

```
vim kubeStateMetrics-deployment.yaml 
image改为bitnami/kube-state-metrics:2.3.0
```

```
vim prometheusAdapter-deployment.yaml
lbbi/prometheus-adapter:v0.9.1
```

# 部署
```
kubectl create -f manifests/setup
```
```
kubectl create -f manifests/
```

# 查看结果
```
<!-- pods全部Running -->
kubectl get pods -n monitoring

<!-- 相关的svc也起来了 -->
kubectl get svc -n monitoring
```

# 通过port-forward让公网快速访问
```
kubectl --namespace monitoring port-forward svc/prometheus-k8s 9090 --address=0.0.0.0

kubectl --namespace monitoring port-forward svc/alertmanager-main 9093 --address=0.0.0.0

kubectl --namespace monitoring port-forward svc/grafana 3000 --address=0.0.0.0

```