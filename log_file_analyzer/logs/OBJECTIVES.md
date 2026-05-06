# Log File Analyzer - Objectives

## logs/app.log
**Objective:** Parse application logs and extract:
- Count logs by severity level (INFO, DEBUG, ERROR, WARNING)
- Extract all ERROR messages with exact timestamps, sorted chronologically
- Calculate the total log duration (days/hours/minutes between first and last entry)
- Generate a temporal pattern report showing which log entries precede errors

## logs/access.log
**Objective:** Analyze web server access logs and extract:
- Count requests by HTTP status code (200, 404, 500, etc.)
- Find the most frequently accessed endpoints/paths
- List all unique IP addresses that made requests
- Identify failed requests (4xx, 5xx status codes)
- Calculate response size statistics

## logs/errors.log
**Objective:** Parse error logs with stack traces and extract:
- Count errors by severity level (ERROR, CRITICAL, WARNING)
- Extract error types and their frequencies
- Find file locations/line numbers where errors occurred
- Group errors by source file
- List all unique error messages

---
Feel free to pick one, two, or all three to analyze!
