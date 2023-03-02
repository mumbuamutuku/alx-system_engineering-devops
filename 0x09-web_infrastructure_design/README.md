<H1> Tasks <H1>
  
#0. Simple web stack


A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a LAMP stack.

This a sample design of  a one server web infrastructure that hosts the website that is reachable via www.foobar.com.
Has:
      1 server
      1 web server (Nginx)
      1 application server
      1 application files (your code base)
      1 database (MySQL)
      1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8
      
Explains some specifics about this infrastructure

#1. Distributed web infrastructure

This is a sample design of a three server web infrastructure that hosts the website www.foobar.com
Has:
	2 servers
	1 web server (Nginx)
	1 application server
	1 load-balancer (HAproxy)
	1 set of application files (your code base)
	1 database (MySQL)

#2. Secured and monitored web infrastructure

This is a sample design of a three server web infrastructure that hosts the website www.foobar.com, it's  secured, serves encrypted traffic, and is monitored
Has:
	3 firewalls
	1 SSL certificate to serve www.foobar.com over HTTPS
	3 monitoring clients (data collector for Sumologic or other monitoring services)

#3. Scale up

This is a comparison of an Application server vs web server
Added: 
	1 server
	1 load-balancer (HAproxy) configured as cluster with the other one
	Split components (web server, application server, database) with their own server
