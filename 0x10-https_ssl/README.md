# 0x10. HTTPS SSL

HTTPS with SSL/TLS has two main roles: encrypting traffic to protect data 
privacy and integrity during transmission, and authenticating the server's
identity to prevent impersonation or attacks. Encrypting traffic ensures
sensitive information remains private, unaltered, and secure from eavesdropping.
SSL termination refers to decrypting SSL/TLS traffic at a designated endpoint
(e.g., load balancer or reverse proxy) to offload encryption processing from
backend servers, simplify certificate management, and improve performance.
However, it can expose plaintext traffic within the internal network unless
end-to-end encryption is implemented.

**AWK** is a text processing tool used to analyze and manipulate structured
text data by operating line-by-line, performing tasks like pattern matching,
text transformation, and report generation. For example, `awk '/error/ {print $2, $5}'
logs.txt` filters lines containing "error" in `logs.txt` and prints the 2nd and 
5th fields. **DIG** (Domain Information Groper) is a command-line tool for querying 
DNS servers to retrieve records such as A, MX, or CNAME, useful for diagnosing 
network issues. For instance, `dig google.com MX` queries DNS servers for Google's
mail exchange records. While AWK handles text processing, DIG specializes in DNS 
troubleshooting.
