### README.md

# API Interaction Guide

This guide provides essential tips and code snippets for interacting with APIs using Python.

## Overview
Learn how to:  
- Navigate API documentation  
- Handle API pagination  
- Parse JSON responses  
- Make recursive API calls  
- Sort dictionary data by values  

---

## 1. Reading API Documentation
- Identify **Base URL** and **Authentication Requirements**.  
- Locate **Endpoints** and supported **HTTP Methods**.  
- Understand request parameters and response formats.  
- Check for **Rate Limits** and **Error Codes**.

---

## 2. Using APIs with Pagination
APIs return large datasets in pages. Two common methods:  
- **Offset-based Pagination**: Uses `page` and `limit` parameters.  
- **Cursor-based Pagination**: Uses a token to fetch the next page.  

**Example Code**:
```python
import requests

url = "https://api.example.com/users"
params = {"page": 1, "limit": 10}

while url:
    response = requests.get(url, params=params)
    data = response.json()
    print(data["results"])
    url = data.get("next")
```

---

## 3. Parsing JSON Responses
Extract data from API JSON responses.

**Example**:
```python
import requests

response = requests.get("https://api.example.com/users/1")
data = response.json()
print(data["name"])  # Access "name" field
```

---

## 4. Recursive API Calls
Fetch all paginated data automatically.

**Example**:
```python
def fetch_all_users(url, users=[]):
    response = requests.get(url)
    data = response.json()
    users.extend(data["results"])

    if data.get("next"):
        return fetch_all_users(data["next"], users)

    return users
```

---

## 5. Sorting Dictionary by Value
Sort dictionary items by their values.

**Ascending Order**:
```python
scores = {"Alice": 90, "Bob": 85, "Charlie": 95}
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1]))
print(sorted_scores)
```

**Descending Order**:
```python
sorted_scores_desc = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
print(sorted_scores_desc)
```

---

## Conclusion
This guide equips you with the basics of working with APIs efficiently. Practice with public APIs like GitHub or OpenWeather to solidify your understanding.

---

### What to Do Next
- Try implementing these examples with your own API.
- Add error handling to API requests.
- Explore API rate limiting techniques.
