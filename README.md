# mininet-ryu-shortestpath

Source code reference: https://github.com/ParanoiaUPC/sdn_shortest_path

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
ryu-manager shortest_path_with_hop/ShortestPath.py --observe-links
```

### Test ping
```
mininet> pingall
```
