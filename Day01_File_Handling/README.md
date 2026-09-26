# Day 1 — File Handling for SOC

## 🎯 Objective

Learn how to use Python file handling for basic Security Operations Center (SOC) log analysis.

The main goal was to read a security log, filter authentication events, count failures, and extract source IP addresses.

---

## 📚 Concepts Learned

### 1. Opening a File

Python can open a file using:

```python
with open("security.log", "r") as file:
````

* `open()` is used to open a file.
* `"security.log"` is the log file.
* `"r"` means read mode.
* `with` is used to work with the file safely.

---

### 2. Reading a File Line-by-Line

```python
for line in file:
```

This allows Python to process each log entry one line at a time.

This is useful for SOC log analysis because security logs can contain many entries.

---

### 3. Filtering Security Events

I used:

```python
if "AUTH_FAIL" in line:
```

This checks whether the current log line contains an authentication failure event.

Example:

```text
2026-09-22 09:11:32 AUTH_FAIL user=admin src_ip=192.168.1.50
```

---

### 4. Filtering Specific Users

I also practiced checking multiple conditions:

```python
if "AUTH_FAIL" in line and "user=admin" in line:
```

This allowed me to identify failed authentication attempts targeting the `admin` account.

---

### 5. Counting Security Events

I used a counter to count the number of failed authentication events.

The log contained four `AUTH_FAIL` events.

Result:

```text
4
```

This demonstrates how Python can summarize repetitive security events.

---

### 6. Splitting Log Fields

I used:

```python
parts = line.split()
```

For example:

```text
2026-09-22 09:11:32 AUTH_FAIL user=admin src_ip=192.168.1.50
```

After splitting:

```text
2026-09-22
09:11:32
AUTH_FAIL
user=admin
src_ip=192.168.1.50
```

```markdown
The `src_ip` field was located at index `4`:

```python
parts[4]
````

### 7. Extracting the IP Address

The value:

```text
src_ip=192.168.1.50
```

was split using:

```python
ip_part.split("=")
```

```markdown
This produced a list containing:

```python
["src_ip", "192.168.1.50"]

The IP address was then accessed using:

```python
ip[1]
```

---

# 🧪 Practical Work

I created a sample security log file named:

```text
security.log
```

The log contained authentication success and failure events.

Example:

```text
2026-09-22 09:11:32 AUTH_FAIL user=admin src_ip=192.168.1.50
```

I created a Python script named:

```text
day01.py
```

The script was executed locally on my laptop.

---

# 🔍 Practical Tasks Completed

### Task 1 — Read the Security Log

Read `security.log` line-by-line using Python.

### Task 2 — Filter Authentication Failures

Filtered only:

```text
AUTH_FAIL
```

events.

### Task 3 — Filter Admin Authentication Failures

Identified failed authentication attempts targeting:

```text
user=admin
```

### Task 4 — Count Failed Authentication Attempts

Counted the total number of `AUTH_FAIL` events.

Result:

```text
4
```

### Task 5 — Extract Source IP Addresses

Extracted the `src_ip` from failed authentication events.

Final output:

```text
192.168.1.50
192.168.1.50
192.168.1.50
10.0.0.25
172.16.10.25
```

---

# 💻 Final Python Script

```python
with open("security.log", "r") as file:
    for line in file:
        if "AUTH_FAIL" in line:
            parts = line.split()
            ip_part = parts[4]
            ip = ip_part.split("=")
            print(ip[1])
```

---

# 📊 Example Output

```text
192.168.1.50
192.168.1.50
192.168.1.50
10.0.0.25
172.16.10.25
```

---

# 🛡️ SOC Relevance

SOC analysts frequently work with authentication and security logs.

Python can help automate repetitive tasks such as:

* Filtering security events
* Counting authentication failures
* Identifying targeted usernames
* Extracting source IP addresses
* Preparing data for further investigation

This is a basic example of using Python to turn raw log data into useful investigation information.

---

# 🧠 Key Learning

The main workflow learned today was:

```text
Security Log
     ↓
Open File
     ↓
Read Line-by-Line
     ↓
Filter Event
     ↓
Split Log Fields
     ↓
Extract Useful Information
     ↓
Analyze the Result
```

I also learned that Python can be used to automate repetitive SOC log-analysis tasks.

---

# 🎤 Interview Explanation

### Question:

**How did you use Python for SOC log analysis?**

### My Answer:

> I used Python file handling to read a security log line-by-line. I filtered authentication failure events, counted the failed attempts, and extracted source IP addresses using string splitting. This helped me understand how Python can automate basic SOC log analysis.
