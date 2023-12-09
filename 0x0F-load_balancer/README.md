# Load balancer

![loadbalancer](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png)

## Introduction to load-balancing and HAproxy

**HAProxy**, which stands for **High Availability Proxy**, is a popular open source software TCP/HTTP Load Balancer and proxying solution which can be run on Linux, macOS, and FreeBSD. Its most common use is to improve the performance and reliability of a server environment by distributing the workload across multiple servers (e.g. web, application, database). It is used in many high-profile environments, including: GitHub, Imgur, Instagram, and Twitter.

### HAProxy Terminology

**Access Control List (ACL)**

ACLs are used to test some condition and perform an action (e.g. select a server, or block a request) based on the test result. Use of ACLs allows flexible network traffic forwarding based on a variety of factors like pattern-matching and the number of connections to a backend, for example.

Example of an ACL:

```
acl url_blog path_beg /blog
```

This ACL is matched if the path of a user’s request begins with /blog. This would match a request of ```http://yourdomain.com/blog/blog-entry-1```, for example.

**Backend**

A backend is a set of servers that receives forwarded requests. Backends are defined in the ```backend``` section of the HAProxy configuration. In its most basic form, a backend can be defined by:

* which load balance algorithm to use
* a list of servers and ports

A backend can contain one or many servers in it. Generally speaking, adding more servers to your backend will increase your potential load capacity by spreading the load over multiple servers. Increased reliability is also achieved through this manner, in case some of your backend servers become unavailable.

Here is an example of a two backend configuration, ```web-backend``` and ```blog-backend``` with two web servers in each, listening on port 80:

```
backend web-backend
   balance roundrobin
   server web1 web1.yourdomain.com:80 check
   server web2 web2.yourdomain.com:80 check
   
backend blog-backend
   balance roundrobin
   mode http
   server blog1 blog1.yourdomain.com:80 check
   server blog1 blog1.yourdomain.com:80 check
```

```balance roundrobin``` line specifies the load balancing algorithm.

```mode http``` specifies that layer 7 proxying will be used.

The ```check``` option at the end of the ```server``` directives specifies that health checks should be performed on those backend servers.

**Frontend**

A frontend defines how requests should be forwarded to backends. Frontends are defined in the ```frontend``` section of the HAProxy configuration. Their definitions are composed of the following components:

* a set of IP addresses and a port (e.g. 10.1.1.7:80, *:443, etc.)
* ACLs
* ```use_backend``` rules, which define which backends to use depending on which ACL conditions are matched, and/or a default_backend rule that handles every other case.

A frontend can be configured to various types of network traffic.

### Types of Load Balancing

**No Load Balancing**

![noloadbalance](https://assets.digitalocean.com/articles/HAProxy/web_server.png)

**Layer 4 Load Balancing**

The simplest way to load balance network traffic to multiple servers is to use layer 4 (transport layer) load balancing. Load balancing this way will forward user traffic based on **IP range and port** (i.e. if a request comes in for ```http://yourdomain.com/anything,``` the traffic will be forwarded to the backend that handles all the requests for ```yourdomain.com``` on port 80).

![layer4](https://assets.digitalocean.com/articles/HAProxy/layer_4_load_balancing.png)

The user accesses the load balancer, which forwards the user’s request to the web-backend group of backend servers. Whichever backend server is selected will respond directly to the user’s request. Generally, all of the servers in the web-backend should be serving identical content–otherwise the user might receive inconsistent content. Note that both web servers connect to the same database server.

**Layer 7 Load Balancing**

Another, more complex way to load balance network traffic is to use layer 7 (application layer) load balancing. Using layer 7 allows the load balancer to forward requests to different backend servers based on the **content of the user’s request**. This mode of load balancing allows you to run multiple web application servers under the same domain and port.

![layer7](https://assets.digitalocean.com/articles/HAProxy/layer_7_load_balancing.png)

In this example, if a user requests ```yourdomain.com/blog```, they are forwarded to the blog backend, which is a set of servers that run a blog application. Other requests are forwarded to web-backend, which might be running another application. Both backends use the same database server, in this example.

A snippet of the example frontend configuration would look like this:

```
frontend http
  bind *:80
  mode http

  acl url_blog path_beg /blog
  use_backend blog-backend if url_blog
 
  default_backend web-backend
```

This configures a frontend named ```http```, which handles all incoming traffic on port 80.

```acl url_blog path_beg /blog``` matches a request if the path of the user’s request begins with ```/blog```.

```use_backend blog-backend if url_blog``` uses the ACL to proxy the traffic to ```blog-backend```.

```default_backend web-backend``` specifies that all other traffic will be forwarded to ```web-backend```.

### Sticky Sessions

Some applications require that a user continues to connect to the same backend server. This can be achieved through sticky sessions, using the ```appsession``` parameter in the backend that requires it.


