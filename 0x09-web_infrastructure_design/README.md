# Web infrastructure design

## Network basics

I know that most of what I'm going to include here is not new but well, there's always room fro revision, I guess.

### What is a protocol

A network protocol is a set of established rules that specify how to format, send and receive data so that computer network endpoints, including computers, servers, routers and virtual machines, can communicate despite differences in their underlying infrastructures, designs or standards.

In networking, support for protocols can be built into the software, hardware or both.

### How network protocols work: The OSI model

![OSI_Model](https://cdn.ttgtmedia.com/rms/onlineImages/networking-osi_layer.png)
---
Network protocols break larger processes into discrete, narrowly defined functions and tasks across every level of the network. In the standard model, known as the *Open Systems Interconnection* **(OSI)** model, one or more network protocols govern activities at each layer in the telecommunication exchange. **Lower** layers deal with **data transport**, while the **upper** layers in the OSI model deal with **software and applications**.

**1. Physical layer:**

The physical layer is the initial layer that physically connects two interoperable systems. It controls **simplex or duplex** modem transmissions and transfers data in **bits**. Additionally, it oversees the hardware that connects the *Network Interface Card* **(NIC)** to the network, including the wiring, cable terminators, topography and voltage levels.

**2. Data-link layer:**

The data-link layer is responsible for the **error-free** delivery of data from one node to another over the **physical layer**. It's also the **firmware** layer of the NIC. It puts datagrams together into **frames** and gives each frame the **start and stop flags**. Additionally, it **fixes** issues brought on by broken, misplaced or duplicate frames.

**3. Network layer:**

The network layer is concerned with information **flow regulation**, **switching** and **routing** between workstations. **Additionally, it divides up datagrams from the transport layer into error-free and smaller datagrams.**

**4. Transport layer:**

The transport layer transfers services **from the network layer to the application layer** and breaks down data into data frames for error checking at the **network segment level**. This also ensures that a fast host on a network doesn't overtake a slower one. Essentially, the transport layer **ensures that the entire message is delivered from beginning to end**. It also **confirms a successful data transmission** and **retransmitting** of the data if an error is discovered.

**5. Session layer:**

The session layer **establishes a connection** between two workstations that need to communicate. In addition to **ensuring security**, this layer oversees **connection establishment, session maintenance and authentication**.

**6. Presentation layer:**

The presentation layer is also known as the *translation layer* because it **retrieves the data from the application layer** and **formats** it for transmission over the network. It addresses the **proper representation of data**, including the syntax and semantics of information. The presentation layer is also in charge of **managing file-level security and transforming data to network standards**.

**7. Application layer:**

The application layer, which is the **top** layer of the network, oversees **relaying user application requests to lower levels**. File transfer, email, remote login, data entry and other common applications take place at this layer.

---

Most computing protocols add a **header** at the beginning of each network packet to **store information** about the **sender** and the message's **intended destination**.

Some protocols may also include a **footer** at the end with additional information. Network protocols process these headers and footers as **part of the data** moving among devices in order to identify messages of their own kind.

### The TCP/IP model

A **set** of cooperating network protocols is called a *protocol suite*. The *Transmission Control Protocol/Internet Protocol* **(TCP/IP)** suite, which is typically used in **client-server models**, includes numerous protocols across layers, such as the **data, network, transport and application layers**, working together to enable internet connectivity.

These include the following:

* **TCP** uses a set of rules to **exchange messages** with other internet points at the **information packet level**.

* **User Datagram Protocol, or UDP**, acts as an **alternative** communication protocol to **TCP** and is used to establish **low-latency and loss-tolerating** connections between applications and the internet.

* **IP** uses a set of rules to **send and receive messages** at the level of **IP addresses**.

---

Additional network protocols, including *Hypertext Transfer Protocol* **(HTTP)** and *File Transfer Protocol* **(FTP)**, have defined sets of rules to exchange and display information. Unlike the OSI model, the TCP/IP suite consists of **four layers**, each with its protocols. The four layers of the TCP/IP model are the following:

**1. Application layer:**

This is the **topmost layer** of the TCP/IP model and is responsible for **providing users with access to network resources**. Some of the protocols included in this layer are **HTTP, *Simple Mail Transfer Protocol* (SMTP) and FTP**.

The application layer is the group of applications that require network communication. This is what the user typically interacts with, such as email and messaging. Because the lower layers handle the details of communication, the applications don’t need to concern themselves with this.

**2. Transport layer:**

This layer ensures that **segments** are transmitted correctly via the **communication channel**. The **network link** between the source and destination systems is also established at this layer.

The transport layer is what provides a reliable data connection between two devices. It divides the data in packets, acknowledges the packets that it has received from the other device, and makes sure that the other device acknowledges the packets it receives.

**3. Internet layer:**

Also known as the ***network layer***, the internet layer **receives and sends packets** for the network. This layer comprises **IP, *Address Resolution Protocol* (ARP) and *Internet Control Message Protocol* (ICMP).**

The internet layer (also called the network layer) controls the movement of packets around the network.

**4. Network access layer:**

The network access layer of TCP/IP combines the **physical and data-link layers of the OSI model**. It deals with **Layer 1 concerns**, such as *energy, bits and the media used to transport them, such as copper, fiber and wireless*. Additionally, it deals with **Layer 2 difficulties**, including *bit conversion into protocol units, such as Ethernet packets, ***media access control (MAC)*** addresses and NICs.*

The datalink layer (also called the link layer, network interface layer, or physical layer) is what handles the physical parts of sending and receiving data using the Ethernet cable, wireless network, network interface card, device driver in the computer, and so on.

### Types of network protocols

The following are the three types of protocols used in network communications:

**1. Network communication protocols:**

The **efficiency** of a network is determined by the communication protocols used. The **formats and regulations that govern how data is exchanged between networks** are formally described by these protocols. This applies to both hardware and software and is a requirement for communicating between computing systems and telecommunication systems. In addition to **handling syntax, synchronization and semantic requirements** that both analog and digital communications must meet to work, communication protocols also handle **authentication and error detection**. *HTTP, UDP, TCP and Internet Relay Chat* are network communication protocols.

***EFFECIENCY***

**2. Network management protocols:**

To ensure **steady communication and optimal performance throughout the network**, network management protocols help specify the policies and processes needed to monitor, administer and maintain a computer network. They also assist in communicating these demands across the network. *Simple Network Management Protocol **(SNMP)** and **ICMP*** are network management protocols.

***CONSISTENCY***

**3. Network security protocols:**

The primary responsibility of network security protocols is to ensure that the data in transit over the network connections are kept **safe and secure**. These protocols also specify how the network protects data from any unauthorized efforts to inspect or extract it. This ensures that unauthorized users, services or devices don't have access to the network. Protocols such as *Secure Sockets Layer **(SSL)**, Secure FTP **(SFTP)** and HTTP Secure **(HTTPS)*** operate at this level.

***SECURITY & SAFETY***

Falling into these three broad categories are thousands of network protocols that uniformly handle an extensive variety of defined tasks, including authentication, automation, correction, compression, error handling, file retrieval, file transfer, link aggregation, routing, semantics, synchronization and syntax.

### How to employ network protocols

For network protocols to work, they must be coded within **software** -- *either as part of the computer's operating system (OS) or as an application* -- or executed within the **computer's hardware**. Most modern OSes possess built-in software services that are prepared to implement some network protocols. Other applications, such as web browsers, are designed with software libraries that support the protocols necessary for the application to function. In addition, **TCP/IP and routing protocol support is implemented in direct hardware for enhanced performance**.

Whenever a new protocol is implemented, it is added to the protocol suite. The organization of protocol suites is considered to be monolithic since all protocols are stored in the same address and built on top of one another.

### What are the vulnerabilities of network protocols?

Malicious attacks, such as *eavesdropping and cache poisoning*, can affect the system. The most common attack on network protocols is the advertisement of false routes, causing traffic to go through compromised hosts instead of the appropriate ones.

Cybercriminals frequently use network protocols in **distributed denial-of-service assaults (DDoS)**, which is another typical method of exploiting them. For example, in a **SYN flood attack**, an attacker takes advantage of the way TCP works. They send SYN packets to repeatedly initiate a TCP handshake with a server until the server is unable to provide service to legitimate users because its resources are tied up by all the fake TCP connections.

Network protocol analyzers are tools that protect systems against malicious activity by supplementing firewalls, antivirus programs and antispyware software.

### Examples of network protocol uses

* **Post Office Protocol 3, or POP3**, is the most recent version of a standard protocol that is used for receiving **incoming emails**.


* **SMTP** is used to send and distribute **outgoing emails**.


* **FTP** is used to **transfer files** from one machine to another. The files can be *multimedia files, program files, text files and documents*.

* **Telnet** is a collection of rules used to **connect one system to another via a remote login**. The local computer sends the request for connection, and the remote computer accepts the connection.


* **HTTPS** is a common protocol used to **protect communication** between two computers, one of which is using a **browser** and the other of which is downloading data from a **web server**.


* **Gopher** is a set of rules used to **search for, get hold of and display documents from remote sites**. Gopher operates according to the **client-server model**.

Other network protocol examples include the following:

* **ARP.**
* **Blocks Extensible Exchange Protocol, or BEEP.**
* **Border Gateway Protocol, or BGP.**
* **Binary Synchronous Communications, or BSC.**
* **Canonical Text Services, or CTS.**
* **Domain Name System, or DNS.**
* **Dynamic Host Configuration Protocol, or DHCP.**
* **Enhanced Interior Gateway Routing Protocol, or EIGRP.**
* **Human Interface Device, or HID, protocol.**
* **ICMP.**
* **Internet Message Access Protocol, or IMAP.**
* **MAC.**
* **Network News Transfer Protocol, or NNTP.**
* **Open Shortest Path First, or OSPF.**
* **SSL.**
* **SNMP.**
* **Thread.**
* **Transport Layer Security, or TLS.**
* **Universal Description, Discovery**
* **Universal Description, Discovery and Integration, or UDDI.**
* **voice over IP, or VoIP.**
* **X10.**

## What is an IP address

Most networks today, including all computers on the internet, use the TCP/IP protocol as the standard for how to communicate on the network. In the TCP/IP protocol, the **unique identifier** for a computer is called its **IP address**.

There are two standards for IP addresses: *IP Version 4* **(IPv4)** and *IP Version 6* **(IPv6)**. Here are the differences between the two address types:

* **IPv4** uses **32 binary bits** to create a single unique address on the network. An IPv4 address is expressed by **four numbers separated by dots**. Each number is the **decimal (base-10)** representation for an **eight-digit binary (base-2)** number, also called an **octet**. *For example: 216.27.61.137*

* **IPv6** uses **128 binary bits** to create a single unique address on the network. An IPv6 address is expressed by **eight groups of hexadecimal (base-16) numbers separated by colons**, as in *2001:cdba:0000:0000:0000:0000:3257:9652*. Groups of numbers that contain all zeros are often omitted to save space, leaving a colon separator to mark the gap (as in *2001:cdba::3257:9652*).

At the dawn of IPv4 addressing, the internet wasn't the large commercial sensation it is today, and most networks were private and closed off from other networks around the world. When the internet exploded, having only 32 bits to identify a unique internet address caused concerns that we'd run out of IP addresses before long. Under IPv4, there are 232 possible combinations, which offers just under 4.3 billion unique addresses. IPv6 raised that to a stress-relieving 2,128 possible addresses.

### How does your computer get its IP address?

An IP address can be either **dynamic or static**. A **static** address is a **permanently** assigned address. Static IP addresses assigned by internet service providers are **rare**. You can assign static IPs to devices on your local network, but it can create network issues if you use it without a good understanding of TCP/IP.

**Dynamic** addresses are the most common. They're assigned by the *Dynamic Host Configuration Protocol* **(DHCP)**, a service running on the network. DHCP typically runs on network **hardware** such as *routers or dedicated DHCP servers*. Dynamic IP addresses are issued using a **leasing system**, meaning that the IP address is **only active for a limited time**. If the lease expires, the computer will automatically request a new lease. Sometimes, this means the computer will get a **new IP address**, too, especially if the computer was unplugged from the network between leases.

### IP Classes

![A diagram of an IP address (IPv4).](https://media.hswstatic.com/eyJidWNrZXQiOiJjb250ZW50Lmhzd3N0YXRpYy5jb20iLCJrZXkiOiJnaWZcL2lwLWFkZHJlc3MtMi5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjgyOH0sInRvRm9ybWF0IjoiYXZpZiJ9fQ==)

IPv4 adresses range from **0.0.0.0** to **255.255.255.255**. However, some numbers in that range are reserved for specific purposes on TCP/IP networks. Four specific reservations include the following:

* **0.0.0.0:** This represents the **default network**, which is the abstract concept of *just being connected to a TCP/IP network.*

* **255.255.255.255:** This address is reserved for **network broadcasts**, or messages that should go to **all computers on the network**.

* **127.0.0.1:** This is called the *loopback address*, meaning **your computer's way of identifying itself**, whether or not it has an assigned IP address. ***(LOCALHOST)***

* **169.254.0.1 to 169.254.255.254:** This is the Automatic Private IP Addressing **(APIPA)** range of addresses assigned automatically when a computer's unsuccessful getting an address from a DHCP server.

The other IP address reservations are for **subnet classes**. A subnetwork is a **smaller network of computers connected to a larger network through a router**. The subnet can have its **own address system** so computers on the **same subnet can communicate quickly without sending data across the larger network**. A router on a TCP/IP network, including the internet, is configured to recognize one or more subnets and route network traffic appropriately. The following are the IP addresses reserved for subnets:

* **10.0.0.0 to 10.255.255.255:** This falls within the **Class A** address range of **1.0.0.0 to 127.0.0.0**, in which the **first bit is 0**.

* **172.16.0.0 to 172.31.255.255:** This falls within the **Class B** address range of **128.0.0.0 to 191.255.0.0**, in which the **first two bits are 10**.

* **192.168.0.0 to 192.168.255.255:** This falls within the **Class C** range of **192.0.0.0 through 223.255.255.0**, in which the first **three bits are 110**.

* **Multicast (formerly called Class D):** The **first four bits in the address are 1110**, with addresses ranging from **224.0.0.0 to 239.255.255.255**.

* **Reserved for future/experimental use (formerly called Class E):** addresses **240.0.0.0 to 254.255.255.254**.

### Internet Addresses and subnets

* **IP address:** 192.168.1.102
* **Subnet mask:** 255.255.255.0
* **Twenty-four bits (three octets)** reserved for network identity
* **Eight bits (one octet)** reserved for nodes
* **Subnet identity** based on subnet mask (**first address**): 192.168.1.0
* **The reserved broadcast address** for the subnet **(last address)**: 192.168.1.255
* Example addresses on the same network: 192.168.1.1, 192.168.1.103
* Example addresses not on the same network: 192.168.2.1, 192.168.2.103

If you use a router to share an internet connection, the router gets the IP address issued directly from the ISP. Then, it creates and manages a subnet for all the computers connected to that router. If your computer's address falls into one of the reserved subnet ranges listed earlier, you're going through a router rather than connecting directly to the internet.

IP addresses on a subnet have two parts: **network** and **node**. The network part identifies the **subnet itself**. The **node**, also called the *host*, is an individual piece of computer equipment connected to the network and requiring a unique address. Each computer knows how to separate the two parts of the IP address by using a subnet mask. A subnet mask looks somewhat like an IP address, but it's actually just a filter used to determine which part of an IP address designates the network and node.

* **255.0.0.0.0** = 11111111.00000000.00000000.00000000 = eight bits for networks, 24 bits for nodes

* **255.255.0.0** = 11111111.11111111.00000000.00000000 = 16 bits for networks, 16 bits for nodes

* **255.255.255.0** = 11111111. 11111111.11111111.00000000 = 24 bits for networks, eight bits for nodes

## What is TCP/IP

**IP** is the part that obtains the **address** to which data is sent.

**TCP** is responsible for **data delivery** once that IP address has been found.

Think of it this way: The IP address is like the phone number assigned to your smartphone. TCP is all the technology that makes the phone ring, and that enables you to talk to someone on another phone. They are different from one another, but they are also meaningless without one another.

### How Does It Work?

If the system were to send the whole message in one piece, and if it were to encounter a problem, the whole message would have to be re-sent. Instead, TCP/IP breaks each message into **packets**, and those packets are then **reassembled** on the other end. In fact, each packet could take a different route to the other computer, if the first route is unavailable or congested.

In addition, TCP/IP divides the different communications tasks into **layers**. Each layer has a different function. Data goes through four individual layers before it is received on the other end (as explained in the following section). TCP/IP then goes through these layers in reverse order to reassemble the data and to present it to the recipient.

The purpose of the layers is to keep things standardized, without numerous hardware and software vendors having to manage communication on their own. It’s like driving a car: All the manufacturers agree on where the pedals are, so that’s something we can count on between cars. It also means that certain layers can be updated, such as to improve performance or security, without having to upgrade the entire thing.

## What is an Internet Protocol (IP) port?

Port numbers allow different applications on the same computer to share network resources simultaneously. Home network routers and computer software work with these ports and sometimes support configuring port number settings.

### How Port Numbers Work

The IP address identifies the destination computer, and the port number identifies the specific destination application.

In both TCP and UDP, port numbers start at 0 and go up to 65535. The lower ranges are dedicated to common internet protocols such as port 25 for SMTP and port 21 for FTP.

### Open and Closed Ports

Ports can be classified as either **open or closed**. **Open** ports have an associated application that **listens for new connection requests**, and **closed ports do not**.

A process called network port scanning detects test messages at each port number to identify which ports are open.

# Server

Servers are located in datacenters which are buildings that host hundreds, or even thousands of computers (servers).

*Note*: a server in the Cloud era could also be a virtual computer, generally called a **VM (Virtual Machine)** or **container**.

In computing, a server is a piece of computer hardware or software (computer program) that provides functionality for other programs or devices, called "clients". This architecture is called the client–server model. Servers can provide various functionalities, often called "services", such as sharing data or resources among multiple clients or performing computations for a client. A single server can serve multiple clients, and a single client can use multiple servers. A client process may run on the same device or may connect over a network to a server on a different device. Typical servers are database servers, file servers, mail servers, print servers, web servers, game servers, and application servers.

Client–server systems are usually most frequently implemented by (and often identified with) the request–response model: a client sends a request to the server, which performs some action and sends a response back to the client, typically with a result or acknowledgment. Designating a computer as "server-class hardware" implies that it is specialized for running servers on it. This often implies that it is more powerful and reliable than standard personal computers, but alternatively, large computing clusters may be composed of many relatively simple, server components.

Strictly speaking, the term server refers to a computer program or process (running program). Through metonymy, it refers to a device used for (or a device dedicated to) running one or several server programs. On a network, such a device is called a host.

The server is part of the client–server model; in this model, a server serves data for clients. The nature of communication between a client and server is request and response.

### Types of Servers

* **Application server:** a server dedicated to running certain software applications.

* **Catalog server:** a central search point for information across a distributed network.

* **Communications server:** carrier-grade computing platform for communications networks.

* **Compute server:** a server intended for intensive (esp. scientific) computations.

* **Database server:** provides database services to other computer programs or computers.

* **Fax server:** provides fax services for clients.

* **File server:** provides remote access to files.

* **Game server:** a server that video game clients connect to in order to play online together.

* **Media server:** Shares digital video or digital audio over a network through media streaming (transmitting content in a way that portions received can be watched or listened to as they arrive, as opposed to downloading an entire file and then using it)

* **Mail server:** handles transport of and access to email.

* **Mobile Server or Server on the Go:** is an Intel Xeon processor based server class laptop form factor computer.

* **Domain Name Server or DNS:** well, DNS

* **Print server:** provides printer services.

* **Proxy server:** acts as an intermediary for requests from clients seeking resources from other servers.

* **Sound server:** Enables computer programs to play and record sound, individually or cooperatively

* **Stand-alone server:** a server on a Windows network that neither belongs to nor governs a Windows domain

* **Web server:** a server that HTTP clients connect to in order to send commands and receive responses along with data contents

# Web server

**A web server is a software that delivers web pages. A server is an actual computer.**

A web server is computer **software** and **underlying hardware** that accepts requests via **HTTP** (the network protocol created to distribute web content) or its *secure variant* **HTTPS**.

![PC clients communicating via the network with a web server serving static content only](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Web_server_serving_static_content.png/221px-Web_server_serving_static_content.png)

A web server can also **accept and store resources** sent from the user agent (commonly a web browser) if configured to do so.

A resource sent from a web server can be a **pre-existing file (static content)** available to the web server, or it can be generated at the **time of the request (dynamic content)** by another program that communicates with the server software. The **former** usually can be served **faster** and can be more **easily cached** for repeated requests, while the **latter** supports a **broader range of applications**.

Technologies such as **REST** and **SOAP**, which use HTTP as a basis for general computer-to-computer communication, as well as support for WebDAV extensions, have extended the application of web servers well beyond their original purpose of serving human-readable pages.

![The world's first web server, a NeXT Computer workstation with Ethernet, 1990. The case label reads: "This machine is a server. DO NOT POWER IT DOWN!!"](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/First_Web_Server.jpg/220px-First_Web_Server.jpg)*The world's first web server, a NeXT Computer workstation with Ethernet, 1990. The case label reads: "This machine is a server. DO NOT POWER IT DOWN!!"*

***Little history fact:*** The use of TCP/IP persistent connections (HTTP/1.1) required web servers both to increase a lot the maximum number of concurrent connections allowed and to improve their level of scalability.

## Technical Overview

A web server program plays the role of a server in a client–server model by implementing one or more versions of HTTP protocol, often including the HTTPS secure variant and other features and extensions that are considered useful for its planned usage.
![PC clients connected to a web server via Internet](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Client-server-model.svg/250px-Client-server-model.svg.png)

The complexity and the efficiency of a web server program may vary a lot depending on (e.g.):

* common features implemented;
* common tasks performed;
* performances and scalability level aimed as a goal;
* software model and techniques adopted to achieve wished performance and scalability level;

* target hardware and category of usage, e.g. embedded system, low-medium traffic web server, high traffic Internet web server.

#### Common features
---

These are basic features that most web servers usually have:

* **Static content serving:** to be able to serve static content (web files) to clients via HTTP protocol.

* **HTTP:** support for one or more versions of HTTP protocol in order to send versions of HTTP responses compatible with versions of client HTTP requests.

* **Logging:** usually web servers have also the capability of logging some information, about client requests and server responses, to log files for security and statistical purposes.

A few other more advanced and popular features:

* **Dynamic content serving:** to be able to serve dynamic content (generated on the fly) to clients via HTTP protocol.

* **Virtual hosting:** to be able to serve many websites (domain names) using only one IP address.

* **Authorization:** to be able to allow, to forbid or to authorize access to portions of website paths (web resources).

* **Content cache:** to be able to cache static and/or dynamic content in order to speed up server responses;

* **Large file support:** to be able to serve files whose size is greater than 2 GB on 32 bit OS.

* **Bandwidth throttling:** to limit the speed of content responses in order to not saturate the network and to be able to serve more clients;

* **Rewrite engine:** to map parts of clean URLs (found in client requests) to their real names.

* **Custom error pages:** support for customized HTTP error messages.

#### (Some) Common tasks
---

* starts, optionally reads and applies settings found in its configuration file(s) or elsewhere, optionally opens log file, starts listening to client connections / requests;

* manages client connection(s) (accepting new ones or closing the existing ones as required);

* receives client requests (by reading HTTP messages):

    * reads and verify each HTTP request message;
    * usually performs URL normalization *(URL normalization refers to when a URL that has been reformatted to ensure that documents that are denoted by multiple URLs will be indexed only once. Normalization may include reformatting domain names (for example, removing capital letters) or removing query parameters.)*;
    * usually performs URL mapping (which may default to URL path translation) *(the process of mapping URLs to web pages. Serves as the identifier the host web server uses to direct an HTTP request to a specific HTTP method VI or static file. Each HTTP method VI and static file has one URL mapping.)*;
    * usually performs URL path translation along with various security checks;

* executes or refuses requested HTTP method:
    
    * optionally manages URL authorizations;
    * optionally manages URL redirections;
    * optionally manages requests for static resources (file contents):
    * optionally manages directory index files;
    * optionally manages regular files;
    * optionally manages requests for dynamic resources:
    * optionally manages directory listings;
    * optionally manages program or module processing, checking the availability, the start and eventually the stop of the execution of external programs used to generate dynamic content;
    * optionally manages the communications with external programs / internal modules used to generate dynamic content;

* replies to client requests sending proper HTTP responses (e.g. requested resources or error messages) eventually verifying or adding HTTP headers to those sent by dynamic programs / modules;

#### Read request message
---

Web server programs are able:

* to read an HTTP request message;
* to interpret it;
* to verify its syntax;
* to identify known HTTP headers and to extract their values from them.

Once an HTTP request message has been decoded and verified, its values can be used to determine whether that request can be satisfied or not. This requires many other steps, including security checks.

##### URL normalization
---
Web server programs usually perform some type of URL normalization (URL found in most HTTP request messages) in order:

* to make resource path always a clean uniform path from root directory of website;

* to lower security risks (e.g. by intercepting more easily attempts to access static resources outside the root directory of the website or to access to portions of path below website root directory that are forbidden or which require authorization);
* to make path of web resources more recognizable by human beings and web log analysis programs (also known as log analyzers / statistical applications).

##### URL mapping
---

In practice, web server programs that implement advanced features, beyond the simple static content serving (e.g. dynamic content serving), usually have to figure out how that URL has to be handled, e.g.:

* as a URL redirection, a redirection to another URL;
* as a static request of file content;
* as a dynamic request of:

    * directory listing of files or other sub-directories contained in that directory;
    * other types of dynamic request in order to identify the program / module processor able to handle that kind of URL path and to pass to it other URL parts, i.e. usually path-info and query string variables.

#### Manage request message
---

In practice, the web server has to handle the request by using one of these response paths:

* if something in request was not acceptable (in status line or message headers), web server already 
sent an error response;

* if request has a method (e.g. OPTIONS) that can be satisfied by general code of web server then a successful response is sent;

* if URL requires authorization then an authorization error message is sent;

* if URL maps to a redirection then a redirect message is sent;

* if URL maps to a dynamic resource (a virtual path or a directory listing) then its handler (an internal module or an external program) is called and request parameters (query string and path info) are passed to it in order to allow it to reply to that request;

* if URL maps to a static resource (usually a file on file system) then the internal static handler is called to send that file;

* if request method is not known or if there is some other unacceptable condition (e.g. resource not found, internal server error, etc.) then an error response is sent.

##### Serve static content
---

*NOTE:* when serving static content only, a web server program usually does not change file contents of served websites (as they are only read and never written) and so it suffices to support only these HTTP methods:

* ```OPTIONS```
* ```HEAD```
* ```GET```

That kind of content is called static because usually it is not changed by the web server when it is sent to clients and because it remains the same until it is modified (file modification) by some program.

Response of static file content can be sped up by a **file cache**.

##### Serve dynamic content
---

*NOTE:* when serving static and dynamic content, a web server program usually has to support also the following HTTP method in order to be able to safely receive data from client(s) and so to be able to host also websites with interactive form(s) that may send large data sets (e.g. lots of data entry or file uploads) to web server / external programs / modules:

* ```POST```

In order to be able to communicate with its internal modules and/or external programs, a web server program must have implemented one or more of the many available **gateway interface(s)** (see also Web Server Gateway Interfaces used for dynamic content).

The three **standard** and historical **gateway interfaces** are the following ones.

**CGI**

An external CGI program is run by web server program for each dynamic request, then web server program reads from it the generated data response and then resends it to client.

**SCGI**

An external SCGI program (it usually is a process) is started once by web server program or by some other program / process and then it waits for network connections; every time there is a new request for it, web server program makes a new network connection to it in order to send request parameters and to read its data response, then network connection is closed.

**FastCGI**

An external FastCGI program (it usually is a process) is started once by web server program or by some other program / process and then it waits for a network connection which is established permanently by web server; through that connection are sent the request parameters and read data responses.

###### **Directory listings**
---

A web server program may be capable to manage the dynamic generation (on the fly) of a directory index list of files and sub-directories.

If a web server program is configured to do so and a requested URL path matches an existing directory and its access is allowed and no static index file is found under that directory then a web page (usually in HTML format), containing the list of files and/or subdirectories of above mentioned directory, is dynamically generated (on the fly). If it cannot be generated an error is returned.

The main usage of directory listings is to allow the download of files (usually when their names, sizes, modification date-times or file attributes may change randomly / frequently) as they are, without requiring to provide further information to requesting user.

###### **Program or module processing**
---

In practice whenever there is content that may vary, depending on one or more parameters contained in client request or in configuration settings, then, usually, it is generated dynamically.

An external program or an internal module (processing unit) can execute some sort of application function that may be used to get data from or to store data to one or more data repositories, e.g.:

* files (file system);
* databases (DBs);
* other sources located in local computer or in other computers.

A processing unit can return any kind of web content, also by using data retrieved from a data repository, e.g.:

* a document (e.g. HTML, XML, etc.);
* an image;
* a video;
* structured data, e.g. that may be used to update one or more values displayed by a dynamic page (DHTML) of a web interface and that maybe was requested by an XMLHttpRequest API (see also: dynamic page).

#### Send response message
---

Web server programs are able to send response messages as replies to client request messages.

An error response message may be sent because a request message could not be successfully read or decoded or analyzed or executed.

##### **Error message**
---

These errors are divided mainly in two categories:

* **HTTP client errors**, due to the type of request message or to the availability of requested web resource;

* **HTTP server errors**, due to internal server errors.

##### **URL authorization**
---

A web server program may be able to verify whether the requested URL path:

* can be freely accessed by everybody;

* requires a user authentication (request of user credentials, e.g. such as user name and password);

* access is forbidden to some or all kind of users.

##### **URL redirection**
---

A web server program may have the capability of doing URL redirections to new URLs (new locations) which consists in replying to a client request message with a response message containing a new URL suited to access a valid or an existing web resource (client should redo the request with the new URL).

URL redirection of location is used:

* to fix a directory name by adding a final slash '/';

* to give a new URL for a no more existing URL path to a new path where that kind of web resource can be found.

* to give a new URL to another domain when current domain has too much load.

**redirection examples/scenarios:**

**Example 1:** a URL path points to a directory name but it does not have a final slash '/' so web server sends a redirect to client in order to instruct it to redo the request with the fixed path name.

**Example 2:** a whole set of documents has been moved inside website in order to reorganize their file system paths.

**Example 3:** a whole set of documents has been moved to a new website and now it is mandatory to use secure HTTPS connections to access them.

##### **Successful message**
---

A web server program is able to reply to a valid client request message with a successful message, optionally containing requested web resource data.

#### Content cache
---

In order to speed up web server responses by lowering average HTTP response times and hardware resources used, many popular web servers implement one or more content caches, each one specialized in a content category.

Content is usually cached by its origin, e.g.:

* static content:

    * file cache;

* dynamic content:

    * dynamic cache (module / program output).

##### **File cache**
---

In practice, nowadays, many popular / high performance web server programs include their own userland *(all code that runs outside the operating system's kernel.)* file cache, tailored for a web server usage and using their specific implementation and parameters.

The wide spread adoption of RAID and/or fast solid-state drives (storage hardware with very high I/O speed) has slightly reduced but of course not eliminated the advantage of having a file cache incorporated in a web server.

##### **Dynamic cache**
---

The typical usage of a dynamic cache is when a website has dynamic web pages about news, weather, images, maps, etc. that do not change frequently (e.g. every n minutes) and that are accessed by a huge number of clients per minute / hour; in those cases it is useful to return cached content too (without calling the internal module or the external program) because clients often do not have an updated copy of the requested content in their browser caches.

## Performances

A web server should always be very responsive, even under high load of web traffic, in order to keep total user's wait (sum of browser time + network time + web server response time) for a response as low as possible.

#### Performance metrics
---

For web server software, main key performance metrics (measured under vary operating conditions) usually are at least the following ones (i.e.):

* **number of requests per second** (**RPS**, similar to QPS, depending on HTTP version and configuration, type of HTTP requests and other operating conditions);

* **number of connections per second** (**CPS**), is the number of connections per second accepted by web server (useful when using HTTP/1.0 or HTTP/1.1 with a very low limit of requests / responses per connection, i.e. 1 .. 20);

* **network latency + response time** for each new client request; usually benchmark tool shows how many requests have been satisfied within a scale of time laps (e.g. within 1ms, 3ms, 5ms, 10ms, 20ms, 30ms, 40ms) and / or the shortest, the average and the longest response time;

* **throughput** of responses, in bytes per second.

Among the operating conditions, the **number (1 .. n) of concurrent client connections** used during a test is an important parameter because it allows to correlate the **concurrency level** supported by web server with results of the tested performance metrics.

#### Software efficiency
---

The specific web server software design and model adopted (e.g.):

* single process or multi-process;
* single thread (no thread) or multi-thread for each process;
* usage of coroutines or not;

... and other programming techniques, such as (e.g.):

* zero copy;
* minimization of possible CPU cache misses;
* minimization of possible CPU branch mispredictions in critical paths for speed;
* minimization of the number of system calls used to perform a certain function / task;
* other tricks;

... used to implement a web server program, can bias a lot the performances and in particular the scalability level that can be achieved under heavy load or when using high end hardware (many CPUs, disks and lots of RAM).

#### Operating conditions
---

There are many operating conditions that can affect the performances of a web server; performance values may vary depending on (i.e.):

* the settings of web server (including the fact that log file is or is not enabled, etc.);

* the HTTP version used by client requests;

* the average HTTP request type (method, length of HTTP headers and optional body);

* whether the requested content is static or dynamic;

* whether the content is cached or not cached (by server and/or by client);

* whether the content is compressed on the fly (when transferred), pre-compressed (i.e. when a file resource is stored on disk already compressed so that web server can send that file directly to the network with the only indication that its content is compressed) or not compressed at all;

* whether the connections are or are not encrypted;

* the average network speed between web server and its clients;

* the number of active TCP connections;

* the number of active processes managed by web server (including external CGI, SCGI, FCGI programs);

* the hardware and software limitations or settings of the OS of the computer(s) on which the web server runs;

* other minor conditions.

## Load limits

A web server (program installation) usually has pre-defined load limits for each combination of operating conditions, also because it is limited by OS resources and because it can handle only a limited number of concurrent client connections.

When a web server is near to or over its load limits, it gets **overloaded** and so it may become **unresponsive**.

#### Overload causes
---

* **Excess legitimate web traffic.** Thousands or even millions of clients connecting to the website in a short amount of time, e.g., Slashdot effect.

* **Distributed Denial of Service attacks.** A denial-of-service attack (DoS attack) or distributed denial-of-service attack (DDoS attack) is an attempt to make a computer or network resource unavailable to its intended users.

* **Computer worms** that sometimes cause abnormal traffic because of millions of infected computers (not coordinated among them).

* **XSS worms** can cause high traffic because of millions of infected browsers or web servers.

* **Internet bots** Traffic not filtered/limited on large websites with very few network resources (e.g. bandwidth) and/or hardware resources (CPUs, RAM, disks).

* **Internet (network) slowdowns** (e.g. due to packet losses) so that client requests are served more slowly and the number of connections increases so much that server limits are reached.

* Web servers, **serving dynamic content, waiting for slow responses coming from back-end computer(s)** (e.g. databases), maybe because of too many queries mixed with too many inserts or updates of DB data; in these cases web servers have to wait for back-end data responses before replying to HTTP clients but during these waits too many new client connections / requests arrive and so they become overloaded.

* **Web servers (computers) partial unavailability.** This can happen because of required or urgent maintenance or upgrade, hardware or software failures such as back-end (e.g. database) failures; in these cases the remaining web servers may get too much traffic and become overloaded.

#### Overload symptoms
---

* Requests are served with (possibly long) delays (from 1 second to a few hundred seconds).

* The web server returns an HTTP error code, such as *500, 502, 503, 504, 408*, or even an intermittent *404*.

* The web server refuses or resets (interrupts) TCP connections before it returns any content.

* In very rare cases, the web server returns only a part of the requested content. This behavior can be considered a bug, even if it usually arises as a symptom of overload.

#### Anti-overload techniques
---

* Tuning OS parameters for hardware capabilities and usage.

* Tuning web server(s) parameters to improve their security and performances.

* Deploying web cache techniques (not only for static contents but, whenever possible, for dynamic contents too).

* Managing network traffic, by using:

    * Firewalls to block unwanted traffic coming from bad IP sources or having bad patterns;

    * HTTP traffic managers to drop, redirect or rewrite requests having bad HTTP patterns;

    * Bandwidth management and traffic shaping, in order to smooth down peaks in network usage.

* Using different domain names, IP addresses and computers to serve different kinds (static and dynamic) of content; the aim is to separate big or huge files (download.*) (that domain might be replaced also by a CDN) from small and medium-sized files (static.*) and from main dynamic site (maybe where some contents are stored in a backend database) (www.*); the idea is to be able to efficiently serve big or huge (over 10 – 1000 MB) files (maybe throttling downloads) and to fully cache small and medium-sized files, without affecting performances of dynamic site under heavy load, by using different settings for each (group) of web server computers, e.g.:
    ```https://download.example.com```

    ```https://static.example.com```

    ```https://www.example.com```

* Using many web servers (computers) that are grouped together behind a **load balancer** so that they act or are seen as one big web server.

* Adding more hardware resources (i.e. RAM, fast disks) to each computer.


* Using more efficient computer programs for web servers (see also: software efficiency).

* Using the most efficient Web Server Gateway Interface to process dynamic requests (spawning one or more external programs every time a dynamic page is retrieved, kills performances).

* Using other programming techniques and workarounds, especially if dynamic content is involved, to speed up the HTTP responses (i.e. by avoiding dynamic calls to retrieve objects, such as style sheets, images and scripts), that never change or change very rarely, by copying that content to static files once and then keeping them synchronized with dynamic content).


# DNS

The Domain Name System DNS is, in simple words, the technology that translates human-adapted, text-based domain names to machine-adapted, numerical-based IP.

It is the phonebook of the Internet. Humans access information online through domain names, like nytimes.com or espn.com. Web browsers interact through Internet Protocol (IP) addresses. DNS translates domain names to IP addresses so browsers can load Internet resources

## The main DNS record types:

#### A Record
---

An A record maps a domain name to the IP address (Version 4) of the computer hosting the domain. An A record uses a domain name to find the IP address of a computer connected to the internet.

The A in A record stands for *Address*.

A Records are the simplest type of DNS records, and one of the primary records used in DNS servers.

You can do a lot with A records, including using multiple A records for the same domain in order to provide redundancy and fallbacks. Additionally, multiple names could point to the same address, in which case each would have its own A record pointing to that same IP address.

##### **A record format**
---

```A <address>```

where ```<address>``` is an IPv4 address and looks like ```162.159.24.4```.

#### Querying A records
---

You can use ```dig``` to determine the A record associated to a domain name. The result is contained in the ```ANSWER``` section. It contains the fully-qualified domain name (FQDN), the remaining time-to-live (TTL), and the IP address.

```bash
$ dig A api.dnsimple.com
```

#### AAAA record
---

AAAA record, just like A record, point to the IP address for a domain. However, this DNS record type is different in the sense that it points to **IPV6 addresses**.

Usage of the AAAA record for DNS resolution has great potential because it uses IPV6, which is an improvement over IPV4. Also, as the internet keeps growing and we're running out of IPV4 addresses, the potential for AAAA records is high.

AAAA records are used to resolve a domain name to the newer IPV6 protocol address.

#### CNAME record
---

A Canonical Name (CNAME) record is a type of resource record in the Domain Name System (DNS) that maps one domain name (an alias) to another (the canonical name).

This can prove convenient when running multiple services (like an FTP server and a web server, each running on different ports) from a single IP address.


##### **Details**
---
When a DNS resolver encounters a CNAME record while looking for a regular resource record, it will restart the query using the canonical name instead of the original name. (If the resolver is specifically told to look for CNAME records, the canonical name (right-hand side) is returned, rather than restarting the query.) The canonical name that a CNAME record points to can be anywhere in the DNS, whether local or on a remote server in a different DNS zone.

For example, if there is a DNS zone as follows:

```
NAME                    TYPE   VALUE
--------------------------------------------------
bar.example.com.        CNAME  foo.example.com.
foo.example.com.        A      192.0.2.23
```

when an **A record** lookup for *bar.example.com* is carried out, the resolver will see a CNAME record and restart the checking at *foo.example.com* and will then return 192.0.2.23.

##### **Possible confusion**
---

With a CNAME record, one can point a name such as *"bar.example.com"* to *"foo.example.com."*

The canonical (true) name of *"bar.example.com."* is *"foo.example.com."* Because CNAME stands for Canonical Name, the right-hand side is the actual "CNAME"; on the same side as the address "A".

```
bar.example.com.        CNAME  foo.example.com.
```

may be read as:

*bar.example.co*m is an alias for the canonical name (CNAME) *foo.example.com*. A client will request *bar.example.com* and the answer will be *foo.example.com*.

##### **Restrictions**
---

* **CNAME records must always point to another domain name, never directly to an IP address.**

* if a CNAME record is present at a node, no other data should be present; this ensures that the data for a canonical name and its aliases cannot be different

* CNAME records that point to other CNAME records should be avoided due to their lack of efficiency, but are not an error. It is possible, then, to create unresolvable loops with CNAME records, as in:

```
foo.example.com.  CNAME  bar.example.com
bar.example.com.  CNAME  foo.example.com
```

* a CNAME record cannot be present at the zone apex(A zone apex record is a DNS record at the root of a DNS zone.)

* MX and NS records must never point to a CNAME alias (RFC 2181 section 10.3). So, for example, a zone must not contain constructs such as:

```
example.com.      MX     0   foo.example.com.
foo.example.com.  CNAME  host.example.com.
host.example.com. A      192.0.2.1
```

* Domains that are used in the SMTP MAIL and RCPT commands may not have a CNAME record. In practice this may work, but can have different behavior with different mail servers, and can have undesired effects.

#### NS record
---

A nameserver (NS) record specifies the authoritative DNS server for a domain. In other words, the NS record helps point to where internet applications like a web browser can find the IP address for a domain name. Usually, multiple nameservers are specified for a domain. For example, these could look like ns1.examplehostingprovider.com and ns2.examplehostingprovider.com.

If you've purchased a web hosting service or set up a simple website, you probably received an email with nameserver details. Those nameservers, in simple terms, connect your domain name to the actual server your site is hosted on. The nameserver contains other DNS records for the domain like an A record and MX record.

#### MX record
---

A **mail exchanger record (MX record)** specifies the mail server responsible for accepting email messages on behalf of a domain name. It is a resource record in the Domain Name System (DNS). It is possible to configure several MX records, typically pointing to an array of mail servers for load balancing and redundancy.

Resource records are the basic information element of the Domain Name System (DNS). An MX record is one of these, and a domain may have one or more of these set up, as below:

```
Domain			TTL   Class    Type  Priority      Host
example.com.	1936	IN		MX		10         onemail.example.com.
example.com.	1936	IN		MX		10         twomail.example.com.
```

The ```priority``` field identifies which mailserver should be preferred - in this case the values are both 10, so mail would be expected to flow evenly to both *onemail.example.com* and *twomail.example.com* - a common configuration. **The host name must map directly to one or more address records (A, or AAAA) in the DNS, and must not point to any CNAME records.**

When an e-mail message is sent through the Internet, the sending mail transfer agent (MTA) queries the Domain Name System for the MX records of each recipient's domain name. This query returns a list of host names of mail exchange servers accepting incoming mail for that domain and their preferences. The sending agent then attempts to establish an SMTP connection, trying the host with the lowest "Priority" value first. The system allows high-availability clusters of mail gateways to be built for one domain if necessary.

The MX mechanism does not grant the ability to provide mail service on alternative port numbers, nor does it provide the ability to distribute mail delivery across a set of unequal-priority mail servers by assigning a weighting value to each one.

According to RFC 5321, the lowest-numbered records are the most preferred. This phrasing can be confusing, and so the preference number is sometimes referred to as the *distance*: smaller distances are more preferable.

##### **Fallback to the address record**
---

In the absence of an MX record, email senders will attempt delivery to the **address record** - e.g. example.com.

This is based on RFC 5321 sec. 5.1, which states :

* SMTP clients must look up an MX record;

* If (and only if) no MX record for the domain is present, treat the domain as if it had an MX record with the given domain as the target hostname and a preference value of 0

* Perform A or AAAA lookups as required to determine the IP address of the target hostname

#### TXT record
---

A **TXT record (short for text record)** is a type of **resource record** in the Domain name system (DNS) used to provide the ability to associate arbitrary text with a host or other name, such as human readable information about a server, network, data center, or other accounting information.

It is also often used in a more structured fashion to record small amounts of machine-readable data into the DNS.

**Some examples of TXT usage:**

* Verification of domain ownership
* Implementation of Sender Policy Framework (SPF)
* DomainKeys Identified Mail (DKIM) records for verifying the sender of email messages
* Zero-configuration networking DNS-based service discovery
* Domain-based Message Authentication, Reporting and Conformance (DMARC) policies

#### Other DNS record types
---

* **SOA record:** SOA stands for *start of authority*. It's an important DNS record type that stores admin information about a domain. This information includes the email address of the admin and when the domain was last updated.

* **PTR record:* A *pointer* (PTR) record provides a domain name for reverse lookup. It's the **opposite of an A record** as it provides the domain name linked to an IP address instead of the IP address for a domain.

* **SRV record:** Using this DNS record type, it's possible to store the IP address and port for specific services.

* **CERT record:** This record type stores public keys certificates.

* **DCHID:** This DNS record type stores information related to *dynamic host configuration protocol* **(DHCP)**.

* **DNAME:** The full meaning of DNAME is *delegation name*. This record type works very similarly to **CNAME**; however, it points all the subdomains for the alias to the canonical domain name. That is, pointing the DNAME for secondsite.com to example.com will also apply to staff.secondsite.com and any other subdomain.

## The root domain and sub domain - differences

A root domain is the parent domain to a sub domain, and its name is not, and can not be divided by a dot.

The dot in the domain name delimits the sub domain name (the part of the name before the dot, eg. www.my.) and the root domain name ( the part after the dot, ie .domain.com). This means that the address my.domain.com is a sub domain of the root domain, whose name is domain.com

In an administrator panel at domain provider account, you can create any number of sub domains. This means that for the root domain called domain.com it is possible to create different sub domains eg. my.domain.com, your.domain.com, school.domain.com… Creating multiple sub domains is always free and does not require you to set up new accounts on a domain provider website.

**www** is also a sub domain.

# Load balancer

![load_balancing](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/6cefdd14b2f8c36789cba132bd5a10d42d88a177.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231030%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231030T192918Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ed9b629e82af231f80a76be07927c1f7a5cdb073651def7aa07af6c172f0796f)

Ever wonder how Facebook, Linkedin, Twitter and other web giants are handling such huge amounts of traffic? They don’t have just one server, but tens of thousands of them. In order to achieve this, web traffic needs to be distributed to these servers, and that is the role of a load-balancer.

The following are the advantages of load balancing your application:

* Reduced the work-load on an individual server.

* Large amount of work done in same time due to concurrency.

* Increased performance of your application because of faster response.

* No single point of failure. In a load balanced environment, if a server crashes the application is still up and served by the other servers in the cluster.

* When appropriate load balancing algorithm is used, it brings optimal and efficient utilization of the resources, as it eliminates the scenario of some server’s resources are getting used than others.

* Scalability: We can increase or decrease the number of servers on the fly without bringing down the application

* Load balancing increases the reliability of your enterprise application

* Increased security as the physical servers and IPs are abstract in certain cases.

On a high level, there are two types of load balancers, which implements different types of scheduling algorithms and routing mechanisms:

* Software load balancer
* Hardware load balancer

## Software Load Balancers

Software load balancers generally implements a combination of one or more **scheduling algorithms**.

#### Weighted Scheduling Algorithm
---

![weight_scheduling_algorithm](https://static.thegeekstuff.com/wp-content/uploads/2016/01/1-weighted-scheduling-load-balancer.png)

Work is assigned to the server according to the **weight assigned to the server**. For different types of the server in the group different weights are assigned thus the load gets distributed.

This is used when there is a considerable difference between the capabilities and specification of the servers present in the farm or cluster.

This algorithm stands out to be efficient in managing the load without swarming the low capability servers the most and efficiently utilizing the available server resource at any instant of time.

#### Round Robin Scheduling
---

![round_robin_scheduling](https://static.thegeekstuff.com/wp-content/uploads/2016/01/2-round-robin-load-balancer.png)

Requests are served by the server **sequentially** one after another. After sending the request to the last server, it starts from the first server again.

This algorithm is used when servers are of equal specification and there not much persistent connections.

#### Least Connection First Scheduling
---

Requests are served first to the server which is currently handling **least number of persistent connections**.

When we have large number of persistent connections in the traffic unevenly distributed between the servers. It is often coupled with **Sticky Session** or **Session aware** load balancing. In this, all the request related to a session is sent to the same server to maintain the session state and syncronization.

This approach is used when we have session aware write operations in sync with client and the server so that it avoids any inconsistency.

**Software Load Balancer Examples:**

* **HAProxy** – A TCP load balancer.
* **NGINX** – A http load balancer with SSL termination support. (install Nginx on Linux)
* **mod_athena** – Apache based http load balancer.
* **Varnish** – A reverse proxy based load balancer.
* **Balance** – Open source TCP load balancer.
* **LVS** – Linux virtual server offering layer 4 load balancing

## Hardware Load Balancers

Load balancing hardwares are often referred as specialized routers or switches which are deployed in between the servers and the client. It can also be a dedicated system in between the the client and the server to balance the load.

The hardware load balancers are implemented on Layer4 (Transport layer) and Layer7 (Application layer) of OSI model so prominent among these hardwares are L4-L7 routers.

#### Layer4 Hardware Load Balancing
---

These kind of load balancers work on **transport layer** of OSI model and make use of TCP, UDP and SCTP transport layer protocol details to make decision on which server the data is to be sent.

Layer 4 load balancers are mostly the **network address translators (NATs)** which shares load to the different servers getting translated to by these loadbalancer. These routers hide multiple servers behind them and translate every response data packets coming from the server to be coming from same ipaddress.

Similarly, when there is a request they reverse translate the request using the mapping table and distributes it among the multiple servers.

**DNS load balancing:** In DNS based load balancing method the Domain Name Servers are configured to return different ipaddress for different systems. This approach creates a load balancing effect whenever there is a dns lookup.

![OSI model](https://static.thegeekstuff.com/wp-content/uploads/2016/01/3-osi-layer-load-balancer.png)

**Direct routing:** This is a yet another configuration of hardware load balancing where the routers are aware of the server mac addresses and server may be ARP( Address resolution Protocol) disabled.

In direct routing, it is direct in the sense that all the income traffic is routed by the load balancer however all the outgoing traffic direct reaches the client which makes it super fast load balancing configuration.

**Tunnel or a IP tunneling** often looks like Direct routing where response is directly sent to client however the traffic between the router and the server can be routed.

In this, client sends the request to the virtual IP of load balancer which further encapsulates the IP packets, keeps a hast table and distributes it to the different servers as per the configured load balancing technique.

When the server is getting back the response, it decapsulates it and send back to the client directly according to the hash table which it has stored. This record is eventually removed from hash table when the connection is closed or there is a timeout.

#### Layer7 Hardware Load Balancing
---

This type of load balancers makes the decision according to the **actual content of the message** (URLs, cookies, scripts) since HTTP exists on the layer7.

These layer7 hardware actually form a **ADN (Application delivery network)** and they pass-on request to the servers as per the type of the content.

For example, the request for image will go to an image server, request for PHP scripts may to another server, HTML, js and css like static content may go to another one and request to any media content may go to yet another server.

So, here a load balancing effect is achieved by distributing load according to the type to content requested.

![layer7-load-balance](https://static.thegeekstuff.com/wp-content/uploads/2016/01/4-layer7-load-balancer.png)

Layer 7 load balancing uses the following three techniques:

* **URL parsing:** From this they come to know about different type of contents.

* **Cookie sniffing:** This helps them for a session aware routing.
* **HTTP reading:** This method looks for http header information.

#### Hardware Load Balancer Examples
---

* F5 BIG-IP load balancer (Setup HTTPS load balance on F5)
* CISCO system catalyst
* Barracuda load balancer
* Coytepoint load balancer

## Some other load balancing algorithms

**Random:** 

This load balancing method randomly distributes load across the servers available, picking one via random number generation and sending the current connection to it. While it is available on many load balancing products, its usefulness is questionable except where uptime is concerned – and then only if you detect down machines. Far from an elegant solution, and most often found in large software packages that have thrown load balancing in as a feature.

**Weighted Round Robin (called Ratio somewhere else):**

With this method, the number of connections that each machine receives over time is proportionate to a ratio weight you define for each machine. This is an improvement over Round Robin because you can say “Machine 3 can handle 2x the load of machines 1 and 2”, and the load balancer will send two requests to machine #3 for each request to the others. The system makes multiple entries in the Round Robin circular queue for servers with larger ratios. So if you set ratios at 3:2:1:1 for your four servers, that’s what the queue would look like – 3 entries for the first server, two for the second, one each for the third and fourth. In this version, the weights are set when the load balancing is configured for your application and never change, so the system will just keep looping through that circular queue.

**Dynamic Round Robin (Called Dynamic Ratio somewhere else):**

is similar to Weighted Round Robin, however, weights are based on continuous monitoring of the servers and are therefore continually changing. This is a dynamic load balancing method, distributing connections based on various aspects of real-time server performance analysis, such as the current number of connections per node or the fastest node response time. This Application Delivery Controller method is rarely available in a simple load balancer.

**Fastest:**

The Fastest method passes a new connection based on the fastest response time of all servers. This method may be particularly useful in environments where servers are distributed across different logical networks. On the BIG-IP, only servers that are active will be selected. Can lead to congestion because response time right now won’t necessarily be response time in 1 second or two seconds.

**Observed:**

The Observed method uses a combination of the logic used in the Least Connections and Fastest algorithms to load balance connections to servers being load-balanced. With this method, servers are ranked based on a combination of the number of current connections and the response time. Servers that have a better balance of fewest connections and fastest response time receive a greater proportion of the connections. This Application Delivery Controller method is rarely available in a simple load balancer.

**Predictive:**

The Predictive method uses the ranking method used by the Observed method, however, with the Predictive method, the system analyzes the trend of the ranking over time, determining whether a servers performance is currently improving or declining. The servers in the specified pool with better performance rankings that are currently improving, rather than declining, receive a higher proportion of the connections. The Predictive methods work well in any environment. This Application Delivery Controller method is rarely available in a simple load balancer.

# Monitoring

Just as the heart monitor in a hospital that is making sure that a patient’s heart is beating and at the right beat, software monitoring will watch computer metrics, record them, and emit an alert if something is unusual or that could make the computer not work properly happens.

Web stack monitoring can be broken down into 2 categories:

* **Application monitoring:** getting data about your running software and making sure it is behaving as expected

* **Server monitoring:** getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)

# App server, Web server: What's the difference?

A Web server exclusively handles HTTP requests, whereas an application server serves business logic to application programs through any number of protocols.

The Web server doesn't provide any functionality beyond simply providing an environment in which the server-side program can execute and pass back the generated responses. The server-side program usually provides for itself such functions as transaction processing, database connectivity, and messaging.

While a Web server may not itself support transactions or database connection pooling, it may employ various strategies for fault tolerance and scalability such as load balancing, caching, and clustering—features oftentimes erroneously assigned as features reserved only for application servers.

As for the application server, an application server exposes business logic to client applications through various protocols, possibly including HTTP.

Such application server clients can include GUIs (graphical user interface) running on a PC, a Web server, or even other application servers. The information traveling back and forth between an application server and its client is not restricted to simple display markup. Instead, the information is program logic. Since the logic takes the form of data and method calls and not static HTML, the client can employ the exposed business logic however it wants.

In most cases, the server exposes this business logic through a component API. Moreover, the application server manages its own resources. Such gate-keeping duties include security, transaction processing, resource pooling, and messaging. Like a Web server, an application server may also employ various scalability and fault-tolerance techniques.

Additionally, most application servers also contain a Web server, meaning you can consider a Web server a subset of an application server.

# Single Point of Failure

![SPOF](https://avinetworks.com/wp-content/uploads/2020/09/single-point-of-failure-diagram.png)

A SPOF or single point of failure is any non-redundant part of a system that, if dysfunctional, would cause the entire system to fail. A single point of failure is antithetical to the goal of high availability in a computing system or network, a software application, a business practice, or any other industrial system.

A single point of failure (SPOF) is essentially a flaw in the design, configuration, or implementation of a system, circuit, or component that poses a potential risk because it could lead to a situation in which just one malfunction or fault causes the whole system to stop working.

## How to Eliminate Single Points of Failure

First identify potential risk posed by conducting a single point of failure risk assessment across three main areas: hardware, software/providers/services, and people. Create a single point of failure analysis checklist detailing the general areas for assessment.

Each individual server within a high-availability server cluster may achieve redundancy by having multiple hard drives, power supplies, and other components.

At the system level, ensure high availability for the server cluster with a load balancer. Spare servers can also deploy in case of failure to achieve system level redundancy.

At the personnel level, a single point of failure person has access to something no one else does, or conducts business critical tasks that no one else can handle.

Packet switching, used by “survivable communications networks” such as the internet and ARPANET, is designed to have no single point of failure. It works by allowing multiple routes between any two destinations on the network. This enables users to communicate as the packets “route around” damage even when nodes in between them fail.

Microservices architecture can also reduce the risk of potential SPOFs, in that this type of structure distributes the functionality of a system in many places. This prevents the entire system from failing when a part of it stops working.

Network protocols intended to avoid single points of failure include:

* Intermediate System to Intermediate System
* Open Shortest Path First
* Shortest Path Bridging

#### Threat Protection and Load Balancer Single Point of Failure
---

Almost any tool can be a SPOF hazard, including security tools. Advanced threat protection tools such as web application firewalls (WAF), load balancers, intrusion prevention systems (IPS), and advanced threat protection (ATP) solutions are at risk during link or NIC failure, during power failures, or when they either block good traffic or pass bad traffic. During these times they are vulnerable to both common threats such as brute force attacks and more complex threats such as cross-site request forgery or implementing XML external entities.

There are ways to configure WAF security architecture that minimize the frequency and effectiveness of various attacks and avoid single points of failure. For example, although basic secure single-tier or two-tier web application architectures are useful during project development, they introduce a SPOF.

Instead, a multi-tier or N-tier architecture offers compartmentalization, separating different application components according to their functions into multiple tiers. With each tier running on a different system, there is no single point of failure. In this sense, multiple, properly configured load balancers can be a single point of failure solutions rather than a source of the problem.

# How do you update your production codebase/database schema without causing downtime?

presume that you've got a single load balancer, 2 web servers (A & B) and 2 database servers (M & N - usually DB servers are linked via logshipping - at least in the SQL Server world)

    1. Webserver A to be disconnected from load balancer (so all incoming traffic goes to B).

    2. Log shipping is stopped (DB Server M is going to get updated first).

    3. Update Webserver A. Point the configuration to DB Server M.

    4. Test and verify that the update worked (usually folks are hitting the IP address directly).

    5. Set the load balancer so that existing sessions continue to go to B. New sessions go to A.

    6. Wait for all sessions on B expire (might be a half hour or more, usually we watch traffic and have a 1 hour break scheduled).

    7. Update B and N.

    8. Test and verify that the update worked.

    9. Set up log shipping again and test it works.

    10. Set the load balancer to regular operation.

In a very complicated web applications, what is described as steps 1-5 might take all night and be a 50 page Excel spreadsheet with times and emergency contact numbers. In such situations, updating half the system is scheduled for 6pm to 6am while leaving the system available to users. Handling the update for the DR site is usually scheduled for the following night - just hope nothing breaks the first day.

Where uptime is a requirement, patches are tested first on the QA environment, which ideally is the same hardware as production. If they show no disruption, they can then be applied on the regular schedule, which is usually on the weekend.

# High availability cluster (active-active/active-passive)

High availability refers to the ability of users to access a system without loss of service. Deploying a high availability system minimizes the time when the system is down, or unavailable and maximizes the time when it is running, or available.

Mission critical computer systems need to be available 24 hours a day, 7 days a week, and 365 days a year. However, part or all of the system may be down during planned or unplanned downtime. A system's availability is measured by the percentage of time that it is providing service in the total time since it is deployed.

High availability solutions can be categorized into local high availability solutions that provide high availability in a single data center deployment, and disaster recovery solutions, which are usually geographically distributed deployments that protect your applications from disasters such as floods or regional network outages.

Amongst possible types of failures, process, node, and media failures as well as human errors can be protected by local high availability solutions. Local physical disasters that affect an entire data center can be protected by geographically distributed disaster recovery solutions.

To solve the high availability problem, The most important mechanism is redundancy. High availability comes from redundant systems and components. You can categorize local high availability solutions by their level of redundancy, into active-active solutions and active-passive solutions.

![active-active & active-passive](https://docs.oracle.com/cd/E17904_01/core.1111/e10106/img/ashia027.gif)

* **Active-active** solutions deploy two or more active system instances and can be used to improve scalability as well as provide high availability. In active-active deployments, all instances handle requests concurrently.

* **Active-passive** solutions deploy an active instance that handles requests and a passive instance that is on standby. In addition, a heartbeat mechanism is set up between these two instances. This mechanism is provided and managed through operating system vendor-specific clusterware. Generally, vendor-specific cluster agents are also available to automatically monitor and failover between cluster nodes, so that when the active instance fails, an agent shuts down the active instance completely, brings up the passive instance, and application services can successfully resume processing. As a result, the active-passive roles are now switched. The same procedure can be done manually for planned or unplanned downtime. Active-passive solutions are also generally referred to as cold failover clusters.

In addition to architectural redundancies, the following local high availability technologies are also necessary in a comprehensive high availability system:

* **Process death detection and automatic restart**

    Processes may die unexpectedly due to configuration or software problems. A proper process monitoring and restart system should monitor all system processes constantly and restart them should problems appear.

    A system process should also maintain the number of restarts within a specified time interval. This is also important since continually restarting within short time periods may lead to additional faults or failures. Therefore a maximum number of restarts or retries within a specified time interval should also be designed as well.

* **Clustering**

    Clustering components of a system together allows the components to be viewed functionally as a single entity from the perspective of a client for runtime processing and manageability. A cluster is a set of processes running on single or multiple computers that share the same workload. There is a close correlation between clustering and redundancy. A cluster provides redundancy for a system.

    If failover occurs during a transaction in a clustered environment, the session data is retained as long as there is at least one surviving instance available in the cluster.

* **State replication and routing**

    For stateful applications, client state can be replicated to enable stateful failover of requests in the event that processes servicing these requests fail.

* **Failover**

    With a load-balancing mechanism in place, the instances are redundant. If any of the instances fail, requests to the failed instance can be sent to the surviving instances.

* **Server load balancing**

    When multiple instances of identical server components are available, client requests to these components can be load balanced to ensure that the instances have roughly the same workload.

* **Server Migration**

    Some services can only have one instance running at any given point of time. If the active instance becomes unavailable, the service is automatically started on a different cluster member. Alternatively, the whole server process can be automatically started on a different system in the cluster.

* **Integrated High Availability**

    Components depend on other components to provide services. The component should be able to recover from dependent component failures without any service interruption.

* **Rolling Patching**

    Patching product binaries often requires down time. Patching a running cluster in a rolling fashion can avoid downtime. Patches can be uninstalled in a rolling fashion as well.

* **Configuration management**

    A clustered group of similar components often need to share common configuration. Proper configuration management ensures that components provide the same reply to the same incoming request, allows these components to synchronize their configurations, and provides high availability configuration management for less administration downtime.

* **Backup and Recovery**

    User errors may cause a system to malfunction. In certain circumstances, a component or system failure may not be repairable. A backup and recovery facility should be available to back up the system at certain intervals and restore a backup when an unrepairable failure occurs.

## Disaster Recovery

![disaster recovery](https://docs.oracle.com/cd/E17904_01/core.1111/e10106/img/ashia026.gif)

Disaster recovery solutions typically set up two homogeneous sites, one active and one passive. Each site is a self-contained system. The active site is generally called the production site, and the passive site is called the standby site. During normal operation, the production site services requests; in the event of a site failover or switchover, the standby site takes over the production role and all requests are routed to that site. To maintain the standby site for failover, not only must the standby site contain homogeneous installations and applications, data and configurations must also be synchronized constantly from the production site to the standby site.

# HTTPS


![https](https://www.instantssl.com/images/http-vs-https.png)

Hyper Text Transfer Protocol Secure (HTTPS) is the secure version of HTTP, the protocol over which data is sent between your browser and the website that you are connected to.

## How Does HTTPS Work?

HTTPS pages typically use one of two secure protocols to encrypt communications - **SSL (Secure Sockets Layer)** or **TLS (Transport Layer Security)**. Both the TLS and SSL protocols use what is known as an 'asymmetric' **Public Key Infrastructure (PKI)** system. An asymmetric system uses two 'keys' to encrypt communications, a 'public' key and a 'private' key. Anything encrypted with the public key can only be decrypted by the private key and vice-versa.

As the names suggest, the 'private' key should be kept strictly protected and should only be accessible the owner of the private key. In the case of a website, the private key remains securely ensconced on the web server. Conversely, the public key is intended to be distributed to anybody and everybody that needs to be able to decrypt information that was encrypted with the private key.

## What is a HTTPS certificate?

When you request a HTTPS connection to a webpage, the website will initially send its SSL certificate to your browser. This certificate contains the public key needed to begin the secure session. Based on this initial exchange, your browser and the website then initiate the 'SSL handshake'. The SSL handshake involves the generation of shared secrets to establish a uniquely secure connection between yourself and the website.

When a trusted SSL Digital Certificate is used during a HTTPS connection, users will see a padlock icon in the browser address bar. When an Extended Validation Certificate is installed on a web site, the address bar will turn green.

## Why Is an SSL Certificate Required?

All communications sent over regular HTTP connections are in 'plain text' and can be read by any hacker that manages to break into the connection between your browser and the website. This presents a clear danger if the 'communication' is on an order form and includes your credit card details or social security number. With a HTTPS connection, all communications are securely encrypted. This means that even if somebody managed to break into the connection, they would not be able decrypt any of the data which passes between you and the website.

## Benefits of Hypertext Transfer Protocol Secure

* Customer information, like credit card numbers, is encrypted and cannot be intercepted

* Visitors can verify you are a registered business and that you own the domain

* Customers are more likely to trust and complete purchases from sites that use HTTPS

# Firewall

A firewall is a division between a **private network** and an **outer network**, often the internet, that manages traffic passing between the two networks. It’s implemented through either **hardware or software**. Firewalls allow, limit, and block network traffic based on preconfigured rules in the hardware or software, analyzing data packets that request entry to the network. In addition to limiting access to computers and networks, a firewall is also useful for allowing remote access to a private network through secure authentication certificates and logins.

Firewalls are both **networking and security** technology. They are often considered the **bare minimum** and standard for network security.

## Hardware Vs. Software Firewalls

A hardware firewall protects **your entire network from the external environment** with a single physical device. While a stand-alone product can be purchased, most hardware firewall devices are installed between the computer network and the internet. This device monitors packets of data as they are transmitted and then blocks or transfers the data according to predefined rules. Because of this hardware firewalls are typically used by larger businesses where security is a big concern.

A software firewall is installed on a user’s computer and protects that **single device**. This provides internal protection to a network. It’s customizable, allowing users some control over its function and protection features, such as being able to block access to certain websites on the network. Because software firewalls are easier to install, they are used by many home and small business users.

A firewall can also be a **component of a computer’s operating system (OS)**. For example, any Windows OS newer than XP includes Windows Firewall, a free software firewall. It notifies users of any suspicious activity and detects and blocks viruses, worms, and hackers.

## Types of Firewalls

* **Packet filtering firewalls** perform basic data packet filtering, analyzing IP and port addresses to determine whether the packets can pass. This filtering is based on user-defined configuration. Packet filtering is fairly effective and transparent to users, but it is difficult to configure. In addition, it is susceptible to IP spoofing.

* **Proxy firewalls** serve as the gateway from one network to another for a specific application. They create a new network session based on the information on the initial request, almost an imitation. This makes it more difficult for attackers to understand data from the transmission. Proxy firewalls only inspect Internet traffic from specific protocols. Proxy servers can provide additional functionality by preventing direct connections from outside the network.

* **Network address translation (NAT) firewalls** allow multiple devices with independent network addresses to connect to the internet with a single IP address, allowing individuals’ private IP addresses to remain hidden. NAT firewalls are similar to proxy firewalls in that they act as an intermediary between a group of computers and outside traffic.

* **Cloud firewalls (or cloud-based firewalls)** are available through the web rather than being installed directly between two networks on hardware. They’re flexible, and users can pass through the firewall and access the network from any location with internet access. Some cloud firewalls are intended for a small private network. Enterprise-grade cloud firewalls are often implemented at the network perimeter of cloud infrastructure.

* **Stateful inspection firewalls** permit or drop packets based on the state of an attempted network connection. Bits in the packet (or network connection) label its state, and the firewall analyzes details about the attempted connection, such as the address it comes from or its size. Stateful inspection firewalls perform more detailed packet inspection than other firewalls, which is useful for better preventing malicious traffic. But they can also be slower, because the inspection takes more time.

* **Unified threat management (UTM) firewalls** are less a type of firewall than a larger security solution. Firewalls are just one feature of UTM. Unified threat management may also include machine learning for better threat intelligence, endpoint security, and intrusion prevention systems, which recognize attackers’ patterns. (Mmm... sounds sophisticated)

* **Network segmentation firewalls** limit access between areas of one private network. These can also be understood as sub-firewalls for a sub-network (subnet). They can be a good method of containing network traffic and limiting breaches, but they’re difficult to set up and expensive as well.

* **Next-generation firewalls (NGFW)** are currently being used by enterprises to provide better network security. They are typically a comprehensive perimeter solution, providing additional security and monitoring features. These features differ by vendor, but they can include deep packet inspection, UTM, IPS, threat intelligence, and machine learning capabilities. More on next-gen firewalls will come later.
