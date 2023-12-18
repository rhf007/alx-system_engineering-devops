# Firewall

![firewall](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png)

Your servers without a firewall…

![firewallmeme](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif)

In computing, a firewall is a **network security system** that monitors and controls **incoming and outgoing network traffic** based on predetermined security rules. A firewall typically establishes a barrier between a trusted network and an untrusted network, such as the Internet.

The **predecessors** to firewalls for network security were **routers** used in the late 1980s. Because they already segregated networks, routers could apply filtering to packets crossing them.

**Fun fact that might be actually too well known:**

Before it was used in real-life computing, the term appeared in the 1983 computer-hacking movie WarGames, and possibly inspired its later use.

## Types of firewall

Firewalls are categorized as a network-based or a host-based system.

* **Network-Based:** positioned **between two or more networks**, typically between the local area network (LAN) and wide area network (WAN), their basic function is to control the flow of data between connected networks. They are either a **software appliance running on general-purpose hardware, a hardware appliance running on special-purpose hardware, or a virtual appliance running on a virtual host controlled by a hypervisor**. Firewall appliances may also offer *non-firewall* functionality, such as DHCP or VPN services.

* **Host-Based:** deployed directly on the **host itself** to control network traffic or other computing resources. This can be a daemon or service as a part of the operating system or an agent application for protection.

### Packet filter

The first reported type of **network firewall** is called a **packet filter**, which **inspects packets transferred between computers.** The firewall maintains an *access-control list* which dictates what packets will be looked at and what action should be applied, if any, with the *default action set to silent discard.* Three basic actions regarding the packet consist of a **silent discard, discard with Internet Control Message Protocol or TCP reset response to the sender, and forward to the next hop.** Packets may be filtered by **source and destination IP addresses, protocol, or source and destination ports.** The bulk of Internet communication in 20th and early 21st century used either Transmission Control Protocol (TCP) or User Datagram Protocol (UDP) in conjunction with well-known ports, enabling firewalls of that era to distinguish between specific types of traffic such as web browsing, remote printing, email transmission, and file transfers.

### Connection tracking

From 1989–1990, three colleagues from AT&T Bell Laboratories, Dave Presotto, Janardan Sharma, and Kshitij Nigam, developed the second generation of firewalls, calling them **circuit-level gateways.**

Second-generation firewalls perform the work of their first-generation predecessors but also maintain knowledge of specific conversations between endpoints by **remembering which port number the two IP addresses are using at layer 4 (transport layer)** of the OSI model for their conversation, allowing examination of the overall exchange between the nodes.

### Application layer

Marcus Ranum, Wei Xu, and Peter Churchyard released an application firewall known as Firewall Toolkit (FWTK) in October 1993.

The key benefit of application layer filtering is that it can understand certain applications and protocols such as File Transfer Protocol (FTP), Domain Name System (DNS), or Hypertext Transfer Protocol (HTTP). This allows it to identify unwanted applications or services using a non standard port, or detect if an allowed protocol is being abused. It can also provide unified security management including enforced encrypted DNS and virtual private networking.

As of 2012, the next-generation firewall provides a wider range of inspection at the application layer, extending deep packet inspection functionality to include, but is not limited to:

* Web filtering

* Intrusion prevention systems

* User identity management

* Web application firewall
