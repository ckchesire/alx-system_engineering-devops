# 0x05. Processes and signals

A Process ID (PID) is a unique non-negative integer automatically assigned to 
each process when it is created on Unix-like operating systems. The process 
init always has PID 1 and is the ancestor of all other processes. While the 
default maximum PID is 32,767, this value can be adjusted up to approximately 
four million. PIDs are not immediately reused to prevent potential errors, so 
a high PID number does not necessarily indicate a large number of processes. 
The /proc filesystem stores real-time information about current processes, with
each process having a numbered directory containing files with details about 
its execution. Users can retrieve process information using commands like 
 - ps, 
 - pstree, 
 - top, and 
 - pidof, 

and can terminate misbehaving programs using the kill command by referencing 
their specific PID.
