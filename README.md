# mininet-ryu-shortestpath

## How to use:

```
git clone ...
cd mininet-ryu-shortestpath
```

### Create network topology
```
sudo ./topo.py
```

### Run controller
```
ryu-manager shortest_path_with_hop --observe-links
```

### Test ping
```
mininet> pingall
```
