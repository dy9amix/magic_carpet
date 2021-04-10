
# Show IP Route (Global Routing Table)
| VRF | Address Family | Route | Active | Metric | Route Preference | Source Protocol | Source Protocol Code | Next Hop Number | Next Hop | Outgoing Interface | Updated |
| --- | -------------- | ----- | ------ | ------ | ---------------- | --------------- | -------------------- | --------------- | -------- | ------------------ | ------- |
| default | ipv4 | 172.16.0.1/32 | True | 0 | 0 | direct |  | 1 | 172.16.0.1 | Loopback1 | 04:56:15 |
| default | ipv4 | 172.16.0.1/32 | True | 0 | 0 | direct |  | 2 | 172.16.0.1 | Loopback1 | 04:56:15 |
| default | ipv4 | 172.16.1.0/30 | True | 0 | 0 | direct |  | 1 | 172.16.1.1 | Ethernet1/5 | 04:55:16 |
| default | ipv4 | 172.16.1.1/32 | True | 0 | 0 | local |  | 1 | 172.16.1.1 | Ethernet1/5 | 04:55:16 |
| management | ipv4 | 0.0.0.0/0 | True | 0 | 1 | static |  | 1 | 10.10.20.254 |  | 04:56:15 |
| management | ipv4 | 10.10.20.0/24 | True | 0 | 0 | direct |  | 1 | 10.10.20.58 | mgmt0 | 04:56:15 |
| management | ipv4 | 10.10.20.58/32 | True | 0 | 0 | local |  | 1 | 10.10.20.58 | mgmt0 | 04:56:15 |