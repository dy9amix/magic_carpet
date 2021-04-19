
# Show IP Access-Lists
| Access Control List | Access Control Entry | Permission | Logging | Source Network | Destination Network | L3 Protocol | L4 Protocol | Operator | Port |
| ------------------- | -------------------- | ---------- | ------- | -------------- | ------------------- | ----------- | ----------- | -------- | ---- |
| IPvZero | 10 | permit | log-none | any | any any | icmp,N/A | N/A | N/A |
| IPvZero | 20 | deny | log-none | any | host 8.8.8.8 host 8.8.8.8 | tcp,N/A | N/A | N/A |
| IPvZero | 30 | permit | log-none | any | any any | ipv4,N/A | N/A | N/A |
| meraki-fqdn-dns | No ACEs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |  
| IPvZero | 20 | deny | log-none,N/A,Destination Protocol,N/A,TCP,eq | 22 |
| meraki-fqdn-dns | No ACEs | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |