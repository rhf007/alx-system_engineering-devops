# HTTPS SSL

![https_ssl](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/FlhGPEK.png)

![httpsvisualization](https://www.instantssl.com/images/http-vs-https.png)

## What are the 2 main roles of HTTPS SSL?/What is the purpose encrypting traffic?

**SSL Encrypts Sensitive Information**

The primary reason why SSL is used is to keep sensitive information sent across the Internet encrypted so that only the intended recipient can access it. This is important because the information you send on the Internet is passed from computer to computer to get to the destination server. Any computer in between you and the server can see your credit card numbers, usernames and passwords, and other sensitive information if it is not encrypted with an SSL certificate. When an SSL certificate is used, the information becomes unreadable to everyone except for the server you are sending the information to. This protects it from hackers and identity thieves.

**SSL Provides Authentication**

In addition to encryption, a proper SSL certificate also provides authentication. This means you can be sure that you are sending information to the right server and not to an imposter trying to steal your information. Why is this important? The nature of the Internet means that your customers will often be sending information through several computers. Any of these computers could pretend to be your website and trick your users into sending them personal information.  It is only possible to avoid this by getting an SSL Certificate from a trusted SSL provider.

Why are SSL providers important? Trusted SSL providers will only issue an SSL certificate to a verified company that has gone through several identity checks. Certain types of SSL certificates, like EV SSL Certificates, require more validation than others. Web browser manufactures verify that SSL providers are following specific practices and have been audited by a third-party using a standard such as WebTrust.

## What SSL termination means

A **TLS termination proxy** (or **SSL termination proxy**, or **SSL offloading**) is a proxy server that acts as an **intermediary** point between client and server applications, and is used to terminate and/or establish TLS (or DTLS) tunnels by decrypting and/or encrypting communications. This is different to TLS pass-through proxies that forward encrypted (D)TLS traffic between clients and servers without terminating the tunnel.

**Uses:**

* secure plaintext communications over untrusted networks by tunnelling them in (D)TLS.

* allow inspection of encrypted traffic by an intrusion detection system to detect and block malicious activities.

* allow network surveillance and analysis of encrypted traffic.

* enable otherwise unsupported integration with other applications that provide additional capabilities such as content filtering or Hardware security module.

* enable (D)TLS protocol versions, extensions, or capabilities (e.g. OCSP stapling, ALPN, DANE, CT validation, etc.) unsupported by client or server applications to enhance their compatibility and/or security.

* work around buggy/insecure (D)TLS implementations in client or server applications to improve their compatibility and/or security.

* provide additional certificate-based authentication unsupported by server and/or client applications or protocols.

* provide an additional defence-in-depth layer for centralised control and consistent management of (D)TLS configuration and associated security policies.

* reduce the load on the main servers by offloading the cryptographic processing to another machine.


