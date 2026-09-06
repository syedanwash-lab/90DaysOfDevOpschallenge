# Day 14 – Networking Fundamentals & Hands-on Checks 

## Objective
Practiced core networking concepts and Linux networking commands used during DevOps troubleshooting. 

---

## 1. OSI vs TCP/IP Model

### OSI Model
- **L7 Application** – HTTP, HTTPS, DNS
- **L6 Presentation** – Encryption and data representation
- **L5 Session** – Session management
- **L4 Transport** – TCP and UDP
- **L3 Network** – IP and ICMP
- **L2 Data Link** – Ethernet and MAC
- **L1 Physical** – Cables, signals and physical transmission

### TCP/IP Model
- **Application** – HTTP, HTTPS, DNS
- **Transport** – TCP and UDP
- **Internet** – IP and ICMP
- **Link** – Ethernet and ARP

### Protocol Mapping

| Protocol | Layer |
|---|---|
| HTTP/HTTPS | Application |
| DNS | Application |
| TCP | Transport |
| UDP | Transport |
| IP | Internet/Network |
| Ethernet | Link/Data Link |

### Real Example
`curl https://example.com` = Application layer over TCP over IP, with TLS providing HTTPS encryption.

---

## 2. Identity Check

### Command
```bash
hostname -I
```
- **IP Address:** `34.221.188.55`

### Observation
The command displayed the private IP address assigned to my Ubuntu EC2 instance.

---

## 3. Reachability Check

### Command
```bash
ping -c 4 google.com
```

### Result
```text
PING google.com (142.250.190.46) 56(84) bytes of data.
64 bytes from del03s42-in-f14.1e100.net (142.250.190.46): icmp_seq=1 ttl=117 time=14.2 ms
64 bytes from del03s42-in-f14.1e100.net (142.250.190.46): icmp_seq=2 ttl=117 time=13.8 ms
64 bytes from del03s42-in-f14.1e100.net (142.250.190.46): icmp_seq=3 ttl=117 time=14.1 ms
64 bytes from del03s42-in-f14.1e100.net (142.250.190.46): icmp_seq=4 ttl=117 time=13.9 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rft min/avg/max/mdev = 13.821/14.012/14.230/0.158 ms
```
![Ping output](ping.png)
- **Packet loss:** `0%`
- **Latency:** `14 ms` approximately
- **Overall connectivity:** `Working`

---

## 4. Network Path

### Command
```bash
traceroute google.com
```
![Traceroute output](traceroute.png)

### Observation
- **Number of visible hops:** `12`
- **Highest observed latency:** `45.2 ms`
- **Timeouts:** `No`
- *Note: Some intermediate hops may not respond to traceroute probes.*

---

## 5. Listening Ports

### Command
```bash
sudo ss -tulpn
```
![Listening ports output](tulpn.png)

### Listening Service Identified
- **Service:** `SSH`
- **Port:** `22`
- **Protocol:** `TCP`

### Observation
SSH was listening on port 22. <Quote bind="0.6.1">As noted by [LinkedIn Pulse](https://www.linkedin.com/pulse/day-14-networking-fundamentals-hands-on-checks-quick-concepts-ubale-8w1df), *“ss -tulpn: It displays listening ports and active connections along with the process using them, useful for checking if services are running.”*</Quote>

---

## 6. DNS Resolution

### Command
```bash
dig +short google.com
```
![DNS lookup output](dig.png)

### Resolved IP
```text
142.250.190.46
```

### Observation
DNS successfully resolved google.com to an IP address.

---

## 7. HTTP Check

### Command
```bash
curl -I https://example.com
```
![HTTP headers output](curl.png)

### HTTP Status
```text
HTTP/2 200 
content-type: text/html; charset=UTF-8
content-length: 1256
```

### Observation
The server returned the HTTP status code `200 OK`.

---

## 8. Connections Snapshot

### Command
```bash
netstat -an | head
```
![Network connections snapshot](netstat.png)

### Observation
The output showed active network connections and listening sockets.
- **ESTABLISHED:** `4`
- **LISTEN:** `12`

---

## 9. Mini Task – Port Probe

### Listening Port
- **Port:** `22`
- **Service:** `SSH`

### Command
```bash
nc -zv localhost 22
```
![Netcat port probe output](nc.png)

### Result
```text
Connection to localhost (127.0.0.1) 22 port [tcp/ssh] succeeded!
```

### Interpretation
The port is reachable locally because the connection test succeeded. If it had failed, I would check the service status, listening sockets and firewall rules.

---

## 10. Reflection

### Which command gives the fastest signal when something is broken?
`ping` provides a quick signal for basic network reachability. For application-level issues, `curl` provides a faster indication of whether the HTTP service is responding.

### What layer would you inspect if DNS fails?
I would first investigate the Application layer because DNS operates there, while also checking network connectivity and DNS configuration.

### What if HTTP 500 appears?
HTTP 500 indicates a server-side application problem. I would investigate the application/service logs, backend dependencies and server health.

### Two follow-up checks in a real incident
1. Check listening ports and service status using `ss` and `systemctl`.
2. Check application/system logs and firewall/network rules.

---

## 11. Key Learnings
- Learned how OSI and TCP/IP models map to common networking protocols.
- Practiced Linux commands such as `ping`, `traceroute`, `ss`, `dig`, `curl`, and `netstat`.
- Learned how to troubleshoot connectivity, DNS, ports and HTTP responses step by step.
