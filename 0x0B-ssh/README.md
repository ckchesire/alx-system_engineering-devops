### SSH and Server Basics

This guide introduces fundamental concepts about servers, SSH, and key management. 
A server is a system that provides resources or services to clients over a network,
often housed in data centers, cloud infrastructure, or on-premises setups. SSH 
(Secure Shell) is a protocol for secure remote access to servers, offering encrypted
communication to ensure data privacy. By generating an SSH RSA key pair using `ssh-keygen`,
users create a private key for secure storage and a public key to be shared with remote
servers for authentication.

Connecting to a remote host with an RSA key pair involves transferring the public key
to the server using `ssh-copy-id` or manually adding it to the `authorized_keys` file.
Using `#!/usr/bin/env bash` in scripts ensures portability and flexibility by dynamically
locating the `bash` interpreter via the system’s `PATH`, making scripts more compatible 
across environments than hardcoding `/bin/bash`. This approach is ideal for users managing
diverse systems where reliability and security are critical.
