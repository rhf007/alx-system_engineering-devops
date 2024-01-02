# API

Oooooookay so today we work with APIs.

Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.

## What Bash scripting should not be used for

When the complexity of your script grows it's time to drop the Bash. With modern tools it can be easy, fast, and fun.

I mean, sure, Bash is cool and all and you can show it off in front of your friends and make them think you're hacking into Rockstar (while you're really just using a bunch of beginner-class commands that have some long useless outputs so that you comfortably show off without messing anything up) but when things get very serious and you're doing real actual work that'll make you cry yourself to sleep, things get serious and you know you need a critical change.

* **Simplest example of things you just can't use bash for** is dealing with things like JSON, XML and the like. I personally have never seen a sane person handling these with Bash.

* **Another simple reason is Graphical User Interfaces (GUIs)**: because if you have the capacity to show off in front of people you do know very well Bash scripting is primarily designed for command-line interfaces. If your task involves creating graphical user interfaces or complex desktop applications, a language with GUI frameworks is absolutely a better choice

* **Performance-Critical Applications:** For applications that require high performance or intensive computation, languages like C, C++, or languages with Just-In-Time (JIT) compilation, such as Java or C#, might be more appropriate. Bash is interpreted and may not be as performant in such scenarios.

* **Cross-Platform Development:** While Bash is available on Unix-like systems, it may not be readily available on Windows without additional tools like Cygwin or WSL (Windows Subsystem for Linux). If cross-platform compatibility is crucial, using a language with broader platform support might be preferable.

* **Task Automation Beyond Shell Commands:** If your automation tasks go beyond simple shell commands and involve more complex logic, file manipulation, or network operations, a higher-level scripting language with richer libraries (e.g., Python, Perl, or Ruby) may offer more capabilities and flexibility.

* **Integration with External APIs:** If your script involves working with external APIs, especially if they require authentication, handling JSON or XML responses, etc., languages with specialized libraries for web requests and data parsing (e.g., Python or Ruby) might be more convenient.

* **Scientific or Data Analysis:** For tasks involving scientific computing, data analysis, or machine learning, languages like Python with libraries such as NumPy, pandas, and scikit-learn are more commonly used due to their extensive ecosystem for these purposes.

## What is an API

It's a software intermediary that allows two applications to talk to each other. APIs are an accessible way to extract and share data within and across organizations.

The term “API” has been generically used to describe connectivity interfaces to an application. However, over the years, the modern API has taken on some unique characteristics that have truly transformed the technology space. First, modern APIs adhere to specific standards (typically HTTP and REST), which enable APIs to be developer-friendly, self-described, easily accessible, and understood broadly.

Additionally, today, APIs are treated more like products than code. They are designed for consumption for specific audiences (e.g. mobile developers), and they are documented and versioned in a way that enables users to have clear expectations of their maintenance and lifecycle.

Because APIs are more standardized, they can be monitored and managed for both performance and scale. And, most importantly, they have a much stronger discipline for security and governance. The way this works in practice is that – going back to the weather phone application example – your phone’s data is never fully exposed to the server and.

Likewise, the server is never fully exposed to your phone. Instead, each communicates with small packets of data –– sharing only that which is absolutely necessary.

And, finally, just like any other piece of software that is productized, the modern API has its own software development lifecycle (SDLC) –– from mocking, designing, and testing to building, managing, and retiring. These APIs are well documented for both consumption and versioning in the process.

Today, APIs have become so valuable that they comprise a large part of many business’ revenue. For example, on average, 35% of organizations’ revenue is now generated by APIs and related implementations. These companies are contributing to a marketplace of thousands of APIs, otherwise referred to as the API economy.

And trust me, [this video](https://youtu.be/s7wmiS2mSXY) is enough to explain that perfectly.

## What is a REST API

**REST (Representational State Transfer):**

REST is an architectural style for designing networked applications. It's not a standard, but a set of principles that outline how web standards, such as HTTP and URLs, should be used. RESTful systems are stateless, meaning each request from a client contains all the information needed to understand and process the request.

**REST API (RESTful API):**

A REST API (or RESTful API) is an API that follows the principles of REST. It is a way for systems to communicate over HTTP, typically used in web services development. RESTful APIs use standard HTTP methods (like GET, POST, PUT, DELETE) and follow the principles of statelessness and resource-based architecture.

[https://www.sitepoint.com/rest-api/](https://www.sitepoint.com/rest-api/)

[https://www.youtube.com/watch?v=qVTAB8Z2VmA](https://www.youtube.com/watch?v=qVTAB8Z2VmA)

## What are microservices

Microservices - also known as the microservice architecture - is an architectural style that structures an application as a collection of services that are:

* Independently deployable
* Loosely coupled

Services are typically organized around business capabilities. Each service is often owned by a single, small team.

The microservice architecture enables an organization to deliver large, complex applications rapidly, frequently, reliably and sustainably - a necessity for competing and winning in today’s world.

This is an [emabarrasinlgy short video](https://www.youtube.com/shorts/oeTdlqO0gdQ) that explains this really well

[another good video by IBM](https://www.youtube.com/watch?v=CdBtNQZH8a4)

## What is the CSV format

Comma-separated values is a text file format that uses commas to separate values. A CSV file stores tabular data in plain text, where each line of the file typically represents one data record. Each record consists of the same number of fields, and these are separated by commas in the CSV file.

## What is the JSON format

JSON(JavaScript Object Notation) is an open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and arrays. It is a common data format with diverse uses in electronic data interchange, including that of web applications with servers.

## Pythonic Package and module name style

Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

When an extension module written in C or C++ has an accompanying Python module that provides a higher level (e.g. more object oriented) interface, the C/C++ module has a leading underscore (e.g. _socket).

## Pythonic Class name style

**Class names should normally use the CapWords convention.**

The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable.

Note that there is a separate convention for builtin names: most builtin names are single words (or two words run together), with the CapWords convention used only for exception names and builtin constants.
 
## Pythonic Function name style and Pythonic Variable name style

Function names should be lowercase, with words separated by underscores as necessary to improve readability.

Variable names follow the same convention as function names.

mixedCase is allowed only in contexts where that’s already the prevailing style (e.g. threading.py), to retain backwards compatibility.

## Pythonic Constant name style

Constants are usually defined on a module level and written in all capital letters with underscores separating words. Examples include MAX_OVERFLOW and TOTAL.

## Significance of CapWords or CamelCase in Python

helps improve the readability of code and makes it easier for developers to distinguish classes from functions and variables
