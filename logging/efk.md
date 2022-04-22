# Install efk stack
- [Install efk stack](#install-efk-stack)
- [下载源码](#下载源码)
- [kubectl apply](#kubectl-apply)
- [注释掉kibana-deployment.yaml 中的SERVER_BASEPATH](#注释掉kibana-deploymentyaml-中的server_basepath)
- [如果机器配置低，调整es-statefulset.yaml的memory限制](#如果机器配置低调整es-statefulsetyaml的memory限制)
- [kubectl apply](#kubectl-apply-1)


# 下载源码
```
git clone git@github.com:kubernetes/kubernetes.git
```


# kubectl apply

```
cd cluster/addons
```


# 注释掉kibana-deployment.yaml 中的SERVER_BASEPATH
```
cd fluentd-elasticsearch/
# - name: SERVER_BASEPATH
# value: /api/v1/namespaces/logging/services/kibana-logging/proxy
```

# 如果机器配置低，调整es-statefulset.yaml的memory限制

# kubectl apply
```
kubectl apply -f fluentd-elasticsearch/
```

```
kubectl --namespace logging port-forward svc/kibana-logging 5601 --address=0.0.0.0

```