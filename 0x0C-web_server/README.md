# Web Server

![webserver](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png)

**Quote of the day:**

[A good Software Engineer is a lazy Software Engineer.](https://www.techwell.com/techwell-insights/2013/12/why-best-programmers-are-lazy-and-act-dumb)
![SWEquote](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg)

## How The Web Works

[A very nice and quick walkthrough of what happens](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)

## Nginx

Nginx (pronounced "engine x") is a **web server** that can also be used as a **reverse proxy, load balancer, mail proxy and HTTP cache.** The software was created by Russian developer Igor Sysoev and publicly released in 2004. Nginx is **free and open-source software**, released under the terms of the 2-clause BSD license. A large fraction of web servers use Nginx, often as a **load balancer**.

### Features

Nginx is easy to configure in order to serve static **web content** or to act as a **proxy server**.

Nginx can be deployed to also serve **dynamic content** on the network using **FastCGI, SCGI handlers for scripts, WSGI application servers or Phusion Passenger modules**, and can serve as a **software load balancer**.

Nginx uses an **asynchronous event-driven** approach, rather than threads, to handle requests. Nginx's modular event-driven architecture can provide predictable performance under high loads.

**HTTP proxy and Web server features**

* Ability to handle **more than 10,000 simultaneous connections** with a **low memory footprint** (~2.5 MB per 10k inactive **HTTP keep-alive connections**)
* Handling of static files, index files and auto-indexing
* **Reverse proxy** with caching
* **Load balancing** with in-band health checks
* **TLS/SSL** with **SNI** and **OCSP stapling** support, via **OpenSSL**
* **FastCGI, SCGI, uWSGI** support with caching
* **gRPC** support
* Name- and IP address-based virtual servers
* **IPv6**-compatible
* **WebSockets** since 1.3.13, including acting as a reverse proxy and do load balancing of WebSocket applications.
* HTTP/1.1 Upgrade (101 Switching Protocols), HTTP/2 protocol support, HTTP/3 protocol support (experimental since 1.25.0)
* **URL rewriting and redirection**

**Mail proxy features**

* **TLS/SSL** support
* **STARTTLS** support
* **SMTP, POP3, and IMAP proxy**
* Requires authentication using an external HTTP server or by an authentication script

### Nginx in comparison to Apache

Nginx was written with an explicit goal of outperforming the Apache web server. While in the past Nginx used to outperform Apache, since Apache 2.4 they offer similar performance. This former performance boost came at a cost of decreased flexibility, such as the ability to override system-wide access settings on a per-file basis (Apache accomplishes this with an .htaccess file, while Nginx has no such feature built in).

Formerly, adding third-party modules to Nginx required recompiling the application from source with the modules statically linked. This was partially overcome in version 1.9.11 in February 2016, with the addition of dynamic module loading. However, the modules still must be compiled at the same time as Nginx, and not all modules are compatible with this system; some require the older static linking process.

### Nginx Unit

Nginx Unit is an open-source web application server, released in 2017 by NGINX, Inc. to target multi-language microservices-based applications. The initial release supported applications written in **Go, PHP, and Python**. By version 1.11.0, the support was extended to **Java, Node.js, Perl, and Ruby** applications; other features include **dynamic configuration, request routing, and load balancing**.

## Root and sub domain

[Here it is in very simple terms](https://landingi.com/help/domains-vs-subdomains/)

# Redirection

[Another quick and simple read](https://moz.com/learn/seo/redirection)
