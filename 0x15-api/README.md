##  Bash Scripting: What It Should NOT Be Used For
- Complex applications (poor error handling & debugging)
- High-performance computing (slow execution)
- Cross-platform applications (limited Windows support)
- GUI applications (text-based)
- Handling structured data (better tools like Python)

## What is an API?
An **API (Application Programming Interface)** allows software systems to communicate
via defined rules, data formats (JSON, XML), and authentication.

## What is a REST API?
A **REST API (Representational State Transfer API)** follows REST principles:
- **Stateless:** No client state stored on the server.
- **Uses HTTP Methods:** `GET`, `POST`, `PUT`, `DELETE`
- **Resource-based URLs:** `/users/1`
- **Returns Standard HTTP Status Codes:** `200 OK`, `404 Not Found`

## What are Microservices?
A **Microservices** architecture divides applications into small, independent services that:
- Have **specific business logic** (e.g., authentication, payments).
- Communicate via **APIs**.
- Are **independently deployable** and scalable.


## Pythonic Naming Conventions

| Element   | Naming Style       | Example                |
|-----------|--------------------|------------------------|
| **Package** | lowercase, no underscores | `mypackage` |
| **Module** | lowercase, use underscores | `my_module.py` |
| **Class** | `CapWords` (CamelCase) | `class MyClass:` |
| **Variable** | lowercase_with_underscores | `user_age = 25` |
| **Function** | lowercase_with_underscores | `def calculate_total():` |
| **Constant** | UPPERCASE_WITH_UNDERSCORES | `MAX_USERS = 100` |

## Use of CapWords (CamelCase) in Python
- Used for **class names**.
- Distinguishes classes from functions/variables.
- Improves **readability** and ensures consistency.
