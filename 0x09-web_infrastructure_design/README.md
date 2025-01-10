# 0x09. Web infrastructure design

A **database** is used to organize data for efficient storage, management, and data
retrieval. It can be relational or non-relational, and serves as the backbone for
applications data storage, which can include both structured and unstructured
data.

A **web server** handles HTTP requests and serves static content(i.e HTML and CSS).
Whereas an **application server** processes dynamic requests and business logic, 
often interacting with the databases or APIs. Modern architectures often blend 
these roles.

For Domain resolution, the DNS(Domain Name System) records maps domain names to IP
addresses, using key types such as A(IPv4), CNAME(alias domain), MX(email routing),
NS records for the authoritative server, TXT(enable authentication).

To ensure reliable systems, Single Point of Failure(SPOF) must be prevented by
implementing mechanisms such as redundancy and failover. In order to minimize downtime
deployment methods such as: blue-green deployments, rolling updates, and canary
testing can be used. We can also use High Availability clusters with clusters being 
either in an active-active state, where all nodes share traffic or active-passive state
where standby nodes take over during failure.

HTTPS protocol is implemented using TLS(Transport Layer Security) which enrypts data
communication between browsers and servers.Firewalls add another layer of defense, 
monitoring and filtering network traffic to prevent unauthorized access.
