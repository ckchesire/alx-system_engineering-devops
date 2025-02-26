# 0x18. Webstack monitoring

Summary covering application performance management, server monitoring, and monitoring distributed systems:

*   **Application Performance Management (APM):** APM involves monitoring and managing software application performance and availability, translating IT metrics into business value. It focuses on detecting and diagnosing complex application performance issues to maintain expected service levels.

*   **Key areas within APM** include end-user experience monitoring, application runtime architecture discovery, business transaction profiling, application component monitoring, and application data analytics.

*   **Measuring Application Performance:** APM closely monitors two sets of metrics. The first set is the performance experienced by end-users, such as average response times under peak load, including transaction load and response times. The second set measures the computational resources used by the application, which helps identify performance bottlenecks and establish performance baselines.

*   **Challenges in Implementing APM:** These include instrumenting applications for monitoring and dealing with virtualised applications, which increase measurement variability. Application service management (ASM) can help with the first problem by providing an application-centric approach.

*   **NGINX Logging:** NGINX allows you to configure logging for errors and processed requests. The `error_log` directive sets up logging to a file, `stderr`, or `syslog`, specifying the minimum severity level of messages to log. The `access_log` directive specifies the location and format of the log.

*   **Server Monitoring:** Server monitoring is crucial for maintaining the security, performance, and availability of cloud-based servers. It involves regularly collecting data from servers, tracking KPIs, and setting up alerts for breaches.

*   **Steps for server monitoring** include identifying important KPIs, setting baseline KPI values, configuring data collection and analysis, setting up alerts, and establishing response procedures.

*   **Types of Servers Monitored:** Monitoring software supports various servers, including web servers (tracking uptime, page load time, etc.), application servers (resource usage, latency, etc.), and network servers (connection status, speed, packet loss, etc.).

*   **Monitoring Distributed Systems:** Effective monitoring and alerting systems are built upon basic principles and practices. Monitoring involves collecting, processing, aggregating, and displaying real-time quantitative data about a system.

*   **Key aspects of monitoring systems** include analysing long-term trends, comparing performance over time, alerting when something is broken, building dashboards, and conducting *ad hoc* retrospective analysis.

*   **Golden Signals**: When monitoring a system, it is important to monitor the four golden signals which are, latency, traffic, errors and saturation

*   **Black-box monitoring** tests externally visible behaviour, while **white-box monitoring** uses metrics exposed by the system's internals. Black-box monitoring is symptom-oriented, while white-box monitoring allows detection of imminent problems.

*   **Simplicity in Monitoring:** Monitoring systems should be designed with simplicity in mind to avoid fragility and maintenance burdens. Rules that catch real incidents should be simple and reliable.

*   **Alerting Philosophy:** Rules for monitoring and alerting should detect otherwise undetected conditions that are urgent, actionable, and actively or imminently user-visible. Every page should be actionable and require intelligence.

