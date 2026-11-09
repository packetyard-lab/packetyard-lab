# Packetyard

A network lab that runs in your browser. Build a topology, configure PCs, switches and routers from a command line, and watch every packet move hop by hop, with a plain-language explanation of what each device does and why.

It's made for network training. Nothing to install and no server to run: open the page and start building.

**Live demo:** https://YOUR-USERNAME.github.io/packetyard/

---

## Features

- **Start screen** with three learning paths (Beginner, Intermediate, Experienced real-world setups), plus Continue and Start from scratch. Turn it off with the checkbox; tap the Packetyard name to reopen it.
- **Works on phones and tablets:** pinch to zoom, drag to pan, and a button to jump between the network and the device console.
- **Drag-and-drop topology** with 11 device types, each with a selectable make and model: PC, Laptop, Server, NAS, Proxy, Switch, Access point, Router, Firewall, SD-WAN edge and Internet/provider cloud.
- **Real command line.** PCs and servers use Windows-style commands (`ipconfig`, `ping`, `tracert`, `nslookup`, `http`). Routers, firewalls and SD-WAN edges use an IOS-style CLI with modes.
- **Ready-made scenarios:** a small company office, a medium enterprise with a DMZ, and HQ + branch over SD-WAN.
- **Guided demos** that build their own network and narrate every packet.
- **Build-it-yourself labs** with goals that tick off automatically, plus hints and full solutions.
- **Animated packets**, colour-coded by protocol. Turn on **Pause each hop** to step through a packet's journey.
- **Live explanations** of every event, for example why a switch floods, why a firewall drops a packet, or why SD-WAN picks a path.
- **Packet inspector** with every header field and the raw bytes on the wire, including tunnelled packets (outer and inner headers).
- **Link controls:** click any cable to add latency or packet loss, or to cut it, and watch protocols react.
- **Display options:** System, Light, Dark or **Eye comfort** (warm, low-glare) theme, plus a **colour-blind safe** palette that adds a letter to each packet.
- **Projects:** start from an empty canvas, save named projects in your browser, download them as `.pkyard` files, and open (upload) a file to resume your work. Your current lab is also autosaved.
- **Network automation (Automate tab):** Ansible-style YAML playbooks with inventory groups, variables and loops; modules for config push, show commands, ping/HTTP tests, compliance checks and backups; dry run with config diffs; idempotent runs; drift detection and rollback; and the same automation shown as Python (Netmiko) code. Works offline.
- **Device views:** a **Desktop** for PCs and laptops (IP Configuration, Command Prompt, Web Browser, Wi-Fi), a **Command line**, a **Physical** front-panel view with live link and activity lights, and a **Learn** card explaining each device.
- **Device model selection:** when adding a device, pick a model from the list next to the device buttons, for example Cisco ISR 4331, Catalyst 9200, FortiGate 60F, Cisco ASA 5506-X, Aruba AP, Windows Server 2022 or Synology NAS. You can also change it later in the device panel. For firewalls the model chooses the CLI style: FortiGate models use a FortiOS-style CLI with `port1`–`port4`, and ASA models use an ASA-style CLI.
- **Windows-style servers:** add server roles (DHCP, DNS, IIS web, file sharing) and configure them with PowerShell cmdlets. There's also a **Config files** view showing the same setup as Linux files (dhcpd.conf, BIND zone, nginx, smb.conf, squid.conf).
- **Cable types:** copper straight-through and crossover (with T568A/B wiring), multimode and single-mode fiber, serial WAN, coax and Wi-Fi, each with a connector illustration, speed and distance.

## Protocols and features simulated

| Area | What's modeled |
|---|---|
| Ethernet switching | MAC learning, flooding of broadcasts and unknown unicasts, forwarding, filtering |
| ARP | Requests and replies, ARP cache, packets waiting in a queue until ARP resolves |
| IPv4 routing | Longest-prefix match; connected, static and default routes; TTL |
| ICMP | Echo request and reply, Time Exceeded (traceroute), Destination Unreachable |
| VLANs (802.1Q) | Access and trunk ports, VLAN tags on the wire, native VLAN, allowed-VLAN lists, per-VLAN MAC tables and flooding |
| Inter-VLAN routing | Router-on-a-stick subinterfaces (`interface gi0/0.10`, `encapsulation dot1Q 10`), DHCP per VLAN |
| OSPF | Hello, neighbor states (INIT, 2-WAY, EXSTART, EXCHANGE, LOADING, FULL), DBD and LSU exchange, link-state database, SPF (Dijkstra), costs, passive interfaces, dead timer, reconvergence after failures |
| OSPF multi-area | Backbone area 0 and other areas, Area Border Routers, one link-state database per area, Type 1 Router and Type 3 Summary LSAs, inter-area (O IA) routes, `area <n> range` summarization, `show ip ospf border-routers` |
| IPv6 | Global and link-local addresses (EUI-64), Neighbor Discovery (Neighbor Solicitation/Advertisement, solicited-node multicast), Router Solicitation/Advertisement, SLAAC, ICMPv6 ping and traceroute (hop limit), static IPv6 routes, dual stack beside IPv4, 40-byte IPv6 header in the inspector |
| RIPv2 | Multicast updates, hop-count metric, split horizon, triggered updates, route timeout |
| DHCP | Discover, Offer, Request, Ack; pools, excluded addresses, gateway and DNS options |
| DNS | Zones with A, CNAME, MX and PTR records; NXDOMAIN; forwarders; `nslookup` and `Resolve-DnsName` |
| DHCP relay | `ip helper-address` on the router; relay agent (giaddr) picks the right scope on a central server |
| SMB file sharing | TCP 445, `net use` and `net view` against shares on a server or NAS |
| STP (802.1D) | Root bridge election, root/designated/blocked ports, listening/learning/forwarding, broadcast storms without STP, port cost, priority, PortFast |
| ACLs | Standard, extended and named ACLs, inbound and outbound, implicit deny, hit counters |
| Site-to-site VPN | IKE Main Mode and Quick Mode, pre-shared keys, transform sets, crypto maps, mirrored interesting-traffic ACLs, ESP encapsulation |
| FortiGate-style firewall | `config firewall policy` (srcintf, dstintf, addresses, service, NAT), addresses, VIPs, static routes, implicit deny policy 0, `diagnose sys session list` |
| ASA-style firewall | `nameif`, named `access-list … extended`, `access-group … in interface`, `object network` with static or dynamic NAT, `show xlate` |
| TCP | Three-way handshake, sequence and acknowledgment numbers, SYN retransmission, RST, FIN teardown |
| HTTP | GET requests and responses over TCP, with real request and response text |
| NAT / PAT | Inside and outside interfaces, PAT (overload) with port translation, static NAT for published servers |
| Stateful firewall | Zones and security levels, ordered permit/deny rules, state table, implicit deny |
| Web proxy | Explicit proxy on port 8080, URL blocking (403), caching (HIT/MISS), X-Forwarded-For |
| SD-WAN | IPsec-style tunnels over MPLS and Internet, BFD-style probes measuring latency and loss, per-app policy, automatic failover |
| Voice | RTP-style test calls that report packets returned, latency and the path used |
| Wi-Fi | Access points bridging wireless laptops into the LAN by SSID |
| Automation | Playbooks, idempotency, dry run, diffs, drift detection, rollback |

## Scenarios

| Scenario | What's in it |
|---|---|
| Small company office | One router doing DHCP and NAT/PAT, a NAS, public DNS and websites on the Internet |
| Medium enterprise with DMZ | Firewall with inside, outside and DMZ zones; core router; Sales, Engineering and Servers subnets; internal DNS; web proxy |
| HQ and branch over SD-WAN | Two SD-WAN edges with MPLS and Internet transports, voice phones and an HQ app server |
| OSPF multi-area | Backbone with two ABRs, area 1 and area 2, inter-area routes and summarization |
| IPv6 dual-stack office | Two LANs and two routers running IPv4 and IPv6; PCs configure themselves with SLAAC |
| Office VLANs with router-on-a-stick | Two switches, Sales and Engineering VLANs, a trunk, and inter-VLAN routing |
| OSPF network with a backup path | Four routers in a ring with a slow serial backup link |
| Two LANs and a router | The basic routed network |
| Redundant switches with Spanning Tree | Three switches in a triangle with one port blocked |
| Departments and a protected server (ACLs) | Sales, Engineering and a server protected by an extended ACL |
| Site-to-site VPN between HQ and a branch | Two routers with an IPsec tunnel across the Internet |
| Windows server room | Central DHCP with relay, DNS zones, IIS sites and file shares |
| Small office behind a FortiGate | WAN, LAN and DMZ ports, a VIP publishing a web server, and policies |
| Empty canvas | Build anything from scratch |

## Guided demos

IPv6 SLAAC, Neighbor Discovery and ICMPv6 · OSPF multi-area with ABRs and summary LSAs · Network automation (playbooks, dry run, drift) · VLANs, trunks and router-on-a-stick · OSPF neighbors, link-state and SPF · ARP · switch MAC learning · routing between subnets · traceroute and TTL · troubleshooting a missing route · RIPv2 · DHCP · how a web page loads (DNS, TCP, HTTP) · NAT/PAT · stateful firewall and DMZ · web proxy filtering and caching · SD-WAN app-aware routing and failover

## Build-it-yourself labs

| Lab | Level |
|---|---|
| Build a small office LAN from scratch | Beginner |
| Connect two departments with a router | Beginner |
| Set up DHCP and DNS for the office | Intermediate |
| Share one public IP with NAT | Intermediate |
| Filter the web with a proxy | Intermediate |
| Separate departments with VLANs | Intermediate |
| Build an OSPF network with a backup path | Advanced |
| Design OSPF areas with ABRs and summarization | Advanced |
| Add IPv6 to a working IPv4 network | Intermediate |
| Publish a web server through the firewall | Advanced |
| Keep voice calls up with SD-WAN | Advanced |
| Control Spanning Tree | Intermediate |
| Protect a server with an ACL | Intermediate |
| Set up a Windows server: DHCP with relay, and DNS | Intermediate |
| Build a site-to-site VPN | Advanced |
| Write FortiGate firewall policies | Advanced |
| Automate a routing rollout | Automation |

## Quick start

The sample lab has two LANs joined by router R1.

1. Click **PC1** to open its console.
2. Type `ping 192.168.2.10`.
3. Watch the ARP request, the switch flooding, the router forwarding and the echo reply.
4. Click a moving packet to inspect it.

Building your own lab:

1. Place two PCs, a switch and a router, then connect them with the **Cable** tool.
2. On each PC: `ip 192.168.1.10/24 192.168.1.1`
3. On the router:

```
enable
configure terminal
interface gi0/0
ip address 192.168.1.1 255.255.255.0
no shutdown
end
```

Router interfaces start shut down, as on real routers, so remember `no shutdown`.

## Command reference

### PC

| Command | Description |
|---|---|
| `ipconfig` | Show the IP address, mask, gateway and MAC |
| `ip <addr>/<len> [gateway]` | Set a static address, e.g. `ip 192.168.1.10/24 192.168.1.1` |
| `ip <addr> <mask> [gateway]` | Same, with a dotted mask |
| `ip dhcp` | Get an address from a DHCP server |
| `ping <ip> [-n count]` | Send ICMP echo requests |
| `tracert <ip>` | Trace the route hop by hop |
| `arp -a` / `arp -d` | Show or clear the ARP cache |
| `cls` | Clear the screen |
| `dns <server-ip>` | Set the DNS server |
| `nslookup <name>` | Resolve a name with DNS |
| `http <url>` | Load a web page (DNS + TCP + HTTP) |
| `voice <ip>` | Place a short test voice call |
| `proxy <ip[:port]>` / `proxy off` | Use a web proxy (PCs) |
| `Ctrl+C` | Stop a running ping |

### Server and proxy extras

| Device | Commands |
|---|---|
| Server | `service http on\|off`, `service dns on\|off`, `site <title>`, `dns add <name> <ip>`, `dns del <name>`, `dns forward <ip>`, `show services` |
| Proxy | `block <domain>`, `unblock <domain>`, `cache on\|off`, `clear cache`, `show blocklist`, `show cache` |
| PC / server IPv6 | `ipv6 autoconfig` (SLAAC), `ipv6 2001:db8:1::10/64 [gateway]`, `ipv6 gateway <addr>`, `ipv6 off`, `ping` / `tracert` with an IPv6 address, `netsh interface ipv6 show neighbors`; `ipconfig` shows link-local, SLAAC and gateway |
| Server (PowerShell) | `Install-WindowsFeature DHCP\|DNS\|Web-Server\|FS-FileServer`, `Add-DhcpServerv4Scope`, `Set-DhcpServerv4OptionValue`, `Add-DhcpServerv4ExclusionRange`, `Add-DhcpServerv4Reservation`, `Get-DhcpServerv4Lease`, `Add-DnsServerPrimaryZone`, `Add-DnsServerResourceRecordA/CName/MX/Ptr`, `Set-DnsServerForwarder`, `New-Website`, `New-SmbShare`, `Resolve-DnsName`, `Test-NetConnection` |

### FortiGate-style firewall (FortiOS CLI)

Pick a FortiGate model. Then use `config system interface`, `config firewall address`, `config firewall vip`, `config firewall policy` and `config router static`, each with `edit <name|id>`, `set <field> <value>`, `next` and `end`. Show and diagnose commands: `show firewall policy`, `get system interface`, `get router info routing-table all`, `diagnose sys session list`, `execute ping <ip>`.

### Router, firewall, SD-WAN edge and switch (IOS-style)

| Mode | Commands |
|---|---|
| User `>` | `enable`, `ping`, `traceroute` |
| Privileged `#` | `configure terminal`, `show ip interface brief`, `show ip route`, `show arp`, `show ip dhcp binding`, `show mac address-table`, `show running-config`, `clear arp-cache`, `clear mac address-table`, `disable` |
| Config `(config)#` | `hostname`, `interface <gi0/0 \| fa0/1>`, `ip route <net> <mask> <next-hop>`, `no ip route …`, `ip dhcp pool <name>`, `ip dhcp excluded-address <low> [high]`, `router rip`, `no router rip`, `do <command>` |
| Interface `(config-if)#` | `ip address <ip> <mask>`, `no ip address`, `shutdown`, `no shutdown` |
| DHCP pool `(dhcp-config)#` | `network <net> <mask>`, `default-router <ip>`, `dns-server <ip>` |
| VLAN (switches) | config: `vlan <id>` then `name <name>`, `no vlan <id>`, `interface range fa0/1 - 4`; interface: `switchport mode access\|trunk`, `switchport access vlan <id>`, `switchport trunk allowed vlan <list>\|all\|add\|remove`, `switchport trunk native vlan <id>`; `show vlan brief`, `show interfaces trunk` |
| Router-on-a-stick | `interface gi0/0.10`, `encapsulation dot1Q 10`, `ip address …`; `no interface gi0/0.10` |
| OSPF `(config-router)#` | `router ospf <pid>`, `network <ip> <wildcard> area <n>`, `router-id <id>`, `passive-interface <if>`, `area <n> range <net> <mask>`; interface: `ip ospf cost <n>`; `show ip ospf neighbor`, `show ip ospf database`, `show ip ospf interface brief`, `show ip ospf border-routers` |
| IPv6 (routers) | config: `ipv6 unicast-routing`, `ipv6 route <prefix/len> <next-hop>`, `ipv6 route ::/0 <if> <fe80::…>`; interface: `ipv6 address <addr/len>`, `ipv6 address <prefix>/64 eui-64`, `ipv6 enable`, `no ipv6 address`; `show ipv6 interface brief`, `show ipv6 route`, `show ipv6 neighbors`, `ping <ipv6>`, `traceroute <ipv6>` |
| RIP `(config-router)#` | `version 2`, `network <classful-net>`, `no network …`, `no auto-summary` |
| NAT (routers and firewalls) | interface: `ip nat inside\|outside`; config: `ip nat pat`, `ip nat static <inside-ip> <public-ip>`; `show ip nat translations` |
| Firewall | interface: `zone <inside\|outside\|dmz>`, `security-level <0-100>`; config: `rule <permit\|deny> <ip\|tcp\|udp\|icmp> <src> <dst> [port]`, `no rule <n>`; `show rules`, `show conn`, `show zones` |
| STP (switches) | `spanning-tree vlan 1 priority <n>`, `spanning-tree vlan 1 root primary`, interface: `spanning-tree cost <n>`, `spanning-tree portfast`; `show spanning-tree` |
| ACL | `access-list <1-99> permit\|deny <src> [wildcard]`, `access-list <100-199> permit\|deny <proto> <src> <dst> [eq <port>]`, `ip access-list extended <name>`; interface: `ip access-group <acl> in\|out`; `show access-lists` |
| Site-to-site VPN | `crypto isakmp policy <n>` (encryption, hash, authentication pre-share, group), `crypto isakmp key <key> address <peer>`, `crypto ipsec transform-set <name> esp-aes esp-sha-hmac`, `crypto map <name> <seq> ipsec-isakmp` (set peer, set transform-set, match address); interface: `crypto map <name>`; `show crypto isakmp sa`, `show crypto ipsec sa` |
| DHCP relay | interface: `ip helper-address <server-ip>` |
| ASA-style firewall | interface: `nameif <inside\|outside\|dmz>`; config: `access-list <NAME> extended permit tcp any host <ip> eq 80`, `access-group <NAME> in interface outside`, `route <nameif> <net> <mask> <gw>`, `object network <name>` then `host <ip>` and `nat (dmz,outside) static <public-ip>`; `show xlate`, `show nameif`, `show route` |
| SD-WAN edge | interface: `sdwan transport <mpls\|internet>`; config: `sdwan peer <name> <lan-net> <mask> <mpls-ip> <internet-ip>`, `sdwan policy <voice\|web\|default> <prefer-mpls\|prefer-internet\|best-latency>`; `show sdwan tunnels`, `show sdwan policy` |

Common shortcuts work, for example `conf t`, `sh ip int br` and `int g0/1`. Type `?` in any mode for help. `end` or `Ctrl+Z` returns to privileged mode.

## Running locally

Download `index.html` and double-click it to open it in any modern browser. It's a single self-contained file with no build step and no server. Everything works offline; only the web fonts need the Internet (it falls back to system fonts without them).

If you prefer a local web server:

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000 in your browser.

## Deploying on GitHub Pages

1. Put `index.html`, `README.md`, `SECURITY.md` and `update-csp.py` at the top level of the repository.
2. Go to **Settings → Pages → Build and deployment**.
3. Choose **Deploy from a branch**, then **main** and **/(root)**, and click **Save**.
4. Tick **Enforce HTTPS** on the same page.
5. The site appears at `https://YOUR-USERNAME.github.io/<repo-name>/`.

## Known limitations

- This is a simulator: protocols are modeled in JavaScript, not run on real network operating systems.
- RIP updates are sent about every 12 seconds of sim time instead of every 30, to keep demos short.
- OSPF uses point-to-point style adjacencies (no DR/BDR election), standard areas only (no stub/NSSA), and Hello/dead timers of 5 s and 20 s of sim time.
- IPv6 is modelled on PCs, servers and routers (not firewalls or SD-WAN edges). There is no DHCPv6 or OSPFv3; use SLAAC and static IPv6 routes. Duplicate Address Detection is skipped.
- VLAN routing uses router-on-a-stick; Layer 3 switch SVIs are not modelled.
- TCP is simplified: one request and one response per connection, no windowing or congestion control.
- SD-WAN tunnels are shown decrypted in the inspector so you can see the inner packet.
- Traceroute sends one probe per hop instead of three.
- There's no Tab completion in the CLI yet.
- STP is classic 802.1D on VLAN 1 (no Rapid STP or per-VLAN instances). VPN uses pre-shared keys only.
- FortiOS and ASA CLIs cover the common commands for the labs, not the full products.
- Labs are saved per browser. Use **Save / load** to move a lab between machines.

## Roadmap

- [x] VLANs and 802.1Q trunking
- [x] Spanning Tree Protocol (STP)
- [x] OSPF (single area)
- [x] OSPF multi-area (ABRs, summary LSAs, area ranges)
- [ ] OSPF DR/BDR election on shared segments
- [x] NAT / PAT
- [x] Stateful firewall rules
- [x] TCP handshake, DNS and HTTP
- [x] Web proxy
- [x] SD-WAN
- [x] Lab exercises with automatic checking
- [x] Site-to-site IPsec VPN
- [x] ACLs (standard, extended, named)
- [x] Windows-style server roles with PowerShell
- [x] FortiGate-style and ASA-style firewalls
- [x] Device model selection
- [x] IPv6 (SLAAC, Neighbor Discovery, ICMPv6, static routes, dual stack)
- [x] Security hardening (Content-Security-Policy, safe project import)
- [ ] OSPFv3 and DHCPv6

## Security

Packetyard runs entirely in your browser and never sends data anywhere. The published page has a strict Content-Security-Policy that only allows its own script to run, and any project file you open is sanitized first. See [SECURITY.md](SECURITY.md) for details and recommended GitHub settings. If you edit the code in `index.html`, run `python3 update-csp.py` afterwards so the policy matches the new script.

## Disclaimer

Packetyard is an independent educational project. It isn't affiliated with or endorsed by any networking vendor. Product and vendor names in the model list (Cisco, Fortinet, Aruba, Juniper, Ubiquiti, Microsoft, Synology, QNAP and others) are trademarks of their owners and are used only as text labels; no logos or vendor artwork are included. The CLIs are simplified imitations of common industry conventions for training purposes.
