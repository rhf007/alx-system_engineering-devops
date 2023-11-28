# Web stack debugging #0

Hmm.... Let's see.

![pic1](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/265/uWLzjc8.jpg)

![pic2](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/45dffb0b1da8dc2ce47e340d7f88b05652c0f486.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231128%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231128T144404Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d99ff4aff28db2b3bb6c9029860d97fc3482ceacef18004812c1c42626230f96)

![pic3](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/bae58c9f066a9668001ef4b4c39778407439d2f9.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231128%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231128T144404Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=386f1fbd959593595555a4c440bf06ccacf65c02f9197ab27e92be55b138d73e)

## Docker

Docker is hotter than hot because it makes it possible to get far more apps running on the same old servers and it also makes it very easy to package and ship programs. Here's what you need to know about it.

![VM_vs_conatiners](https://www.zdnet.com/a/img/resize/c01a339830ff3e65d3dbbf8c73192a7047a605b2/2017/05/08/af178c5a-64dd-4900-8447-3abd739757e3/docker-vm-container.png?auto=webp&width=1280)

### So why does everyone love containers and Docker?

James Bottomley, formerly Parallels' CTO of server virtualization and a leading Linux kernel developer, explained VM hypervisors, such as Hyper-V, KVM, and Xen, all are "based on emulating virtual hardware. That means they're fat in terms of system requirements."

Containers, however, use shared operating systems. This means they are much more efficient than hypervisors in system resource terms. Instead of virtualizing hardware, containers rest on top of a single Linux instance. This means you can "leave behind the useless 99.9 percent VM junk, leaving you with a small, neat capsule containing your application," said Bottomley.

Therefore, according to Bottomley, with a perfectly tuned container system, you can have as many as four-to-six times the number of server application instances as you can using Xen or KVM VMs on the same hardware.

Another reason why containers are popular is they lend themselves to Continuous Integration/Continuous Deployment (CI/CD). This a DevOps methodology designed to encourage developers to integrate their code into a shared repository early and often, and then to deploy the code quickly and efficiently.

Docker enables developers to easily pack, ship, and run any application as a lightweight, portable, self-sufficient container, which can run virtually anywhere. (Instant Application Portability)

Containers do this by enabling developers to isolate code into a single container. This makes it easier to modify and update the program. It also lends itself, as Docker points out, for enterprises to break up big development projects among multiple smaller, Agile teams using Jenkins, an open-source CI/CD program, to automate the delivery of new software in containers.

In addition, Docker containers are easy to deploy in a cloud. As Ben Lloyd Pearson wrote in Opensource.com: "Docker has been designed in a way that it can be incorporated into most DevOps applications, including Puppet, Chef, Vagrant, and Ansible, or it can be used on its own to manage development environments."

Specifically, for CI/CD Docker makes it possible to set up local development environments that are exactly like a live server; run multiple development environments from the same host with unique software, operating systems, and configurations; test projects on new or different servers; and allow anyone to work on the same project with the exact same settings, regardless of the local host environment. This enables developers to run the test suites, which are vital to CI/CD, to quickly see if a newly made change works properly.

---
<br>

**The key difference between containers and VMs is while the hypervisor abstracts an entire device, containers just abstract the operating system kernel.**

This, in turn, means one thing VM hypervisors can do that containers can't is to use different operating systems or kernels. So, for example, you can use Microsoft Azure to run both instances of Windows Server 2012 and SUSE Linux Enterprise Server, at the same time. With Docker, all containers must use the same operating system and kernel.

On the other hand, if all you want to do is get the most server application instances running on the least amount of hardware, you couldn't care less about running multiple operating system VMs. If multiple copies of the same application are what you want, then you'll love containers.

This move can save a data center or cloud provider tens of millions of dollars annually in power and hardware costs. It's no wonder they're rushing to adopt Docker as fast as possible.

---
<br>

you can run Docker containers on essentially any operating system or cloud. This gives it an advantage over the others.

In the level above containers, container orchestration, Docker does has a serious competitor: **Kubernetes**.


