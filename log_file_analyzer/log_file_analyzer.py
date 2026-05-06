import re
import os
import statistics
from datetime import datetime

def parseAccessLog(log="logs/access.log"):
    """Analyze web server access logs and extract:
    - Count requests by HTTP status code
    - Find the most frequently accessed endpoints/paths
    - List all unique IP addresses that made requests
    - Identify failed requests (4xx, 5xx status codes)
    - Calculate response size statistics
    """
    # Extend the regex to capture the response size (last field) which may be '-'.
    pattern = re.compile(r'^([\d\.]+) - - \[[^\]]+\] "[A-Z]+ ([^"\s]+) [^\"]+" (\d{3}) (\d+|-)')

    with open(log, 'r') as handle:
        data = handle.readlines()

        ip_addresses = []
        status_codes = {}
        endpoints = {}
        sizes = []

        for line in data:
            if match := pattern.search(line):
                ip, endpoint, code_str, size_str = match.groups()

                # Collect unique IPs
                if ip not in ip_addresses:
                    ip_addresses.append(ip)

                # Count endpoints and status codes
                endpoints[endpoint] = endpoints.get(endpoint, 0) + 1
                status_codes[code_str] = status_codes.get(code_str, 0) + 1

                # Collect sizes when present
                if size_str != '-':
                    sizes.append(int(size_str))

        # Identify failed requests (4xx and 5xx)
        failed_requests = {
            code: count
            for code, count in status_codes.items()
            if 400 <= int(code) <= 599
        }

        total_requests = sum(status_codes.values())
        failure_rate = (sum(failed_requests.values()) / total_requests) if total_requests else 0

        # Compute response size statistics
        if sizes:
            response_size_stats = {
                "count": len(sizes),
                "total_bytes": sum(sizes),
                "min_bytes": min(sizes),
                "max_bytes": max(sizes),
                "avg_bytes": sum(sizes) / len(sizes),
                "median_bytes": statistics.median(sizes),
            }
        else:
            response_size_stats = {
                "count": 0,
                "total_bytes": 0,
                "min_bytes": None,
                "max_bytes": None,
                "avg_bytes": 0,
                "median_bytes": None,
            }

        return status_codes, endpoints, ip_addresses, failed_requests, failure_rate, response_size_stats

def parseAppLog(log="logs/app.log"):
    """Parse application logs and extract:
    - Count logs by severity level (INFO, DEBUG, ERROR, WARNING)
    - Extract all ERROR messages with exact timestamps, sorted chronologically
    - Calculate the total log duration (days/hours/minutes between first and last entry)
    - Generate a temporal pattern report showing which log entries precede errors
    """
    timestamp_pattern = re.compile(r'\[([\d\-\s:]+)\] (\w+):')
    
    with open(log, 'r') as handle:
        data = handle.readlines()
        
        severity_counts = {}
        error_messages = []
        timestamps = []
        temporal_patterns = []
        
        for idx, line in enumerate(data):
            if match := timestamp_pattern.search(line):
                timestamp_str = match.group(1)
                level = match.group(2)
                
                # Count severity levels
                severity_counts[level] = severity_counts.get(level, 0) + 1
                
                # Parse timestamp
                try:
                    ts = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                    timestamps.append((ts, line.strip()))
                except:
                    pass
                
                # Extract ERROR messages with timestamps
                if level == "ERROR":
                    error_messages.append({
                        "timestamp": timestamp_str,
                        "message": line.strip()
                    })
                    
                    # Collect preceding log entries for temporal pattern
                    if idx > 0:
                        preceding = data[idx-1].strip() if idx > 0 else ""
                        temporal_patterns.append({
                            "preceded_by": preceding,
                            "error": line.strip()
                        })
        
        # Sort error messages chronologically
        error_messages.sort(key=lambda x: x["timestamp"])
        
        # Calculate log duration
        log_duration = None
        if len(timestamps) >= 2:
            first_ts = min(ts for ts, _ in timestamps)
            last_ts = max(ts for ts, _ in timestamps)
            duration = last_ts - first_ts
            
            total_seconds = duration.total_seconds()
            days = duration.days
            hours = (total_seconds % 86400) // 3600
            minutes = (total_seconds % 3600) // 60
            
            log_duration = {
                "start": first_ts.strftime("%Y-%m-%d %H:%M:%S"),
                "end": last_ts.strftime("%Y-%m-%d %H:%M:%S"),
                "days": days,
                "hours": int(hours),
                "minutes": int(minutes)
            }
        
        return severity_counts, error_messages, log_duration, temporal_patterns

def parseErrorLog(log="logs/errors.log"):
    """Parse error logs with stack traces and extract:
    - Count errors by severity level (ERROR, CRITICAL, WARNING)
    - Extract error types and their frequencies
    - Find file locations/line numbers where errors occurred
    - Group errors by source file
    - List all unique error messages
    """
    severity_pattern = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (ERROR|CRITICAL|WARNING):\s*(.*)')
    location_pattern = re.compile(r'([a-zA-Z_]\w*\.(?:java|py|js|cpp|c|go|rs)):\d+')
    
    with open(log, 'r') as handle:
        content = handle.read()
    
    severity_counts = {}
    error_types = {}
    file_locations = {}
    error_messages = set()
    grouped_by_file = {}
    current_error = None
    
    for line in content.split('\n'):
        # Check if this is a new error entry
        if severity_match := severity_pattern.match(line):
            timestamp = severity_match.group(1)
            severity = severity_match.group(2)
            error_desc = severity_match.group(3)
            
            # Count severity levels
            severity_counts[severity] = severity_counts.get(severity, 0) + 1
            
            # Extract error type (first word after severity)
            error_type = error_desc.split(':')[0].strip() if error_desc else "Unknown"
            error_types[error_type] = error_types.get(error_type, 0) + 1
            
            # Add to unique error messages
            error_messages.add(error_desc)
            
            current_error = {
                "timestamp": timestamp,
                "severity": severity,
                "description": error_desc,
                "stack_trace": []
            }
        
        elif current_error and line.strip():
            # This is a continuation of the stack trace
            current_error["stack_trace"].append(line.strip())
            
            # Extract file locations
            if file_match := location_pattern.search(line):
                filename = file_match.group(1)
                file_locations[filename] = file_locations.get(filename, 0) + 1
                
                # Group by source file
                if filename not in grouped_by_file:
                    grouped_by_file[filename] = []
                grouped_by_file[filename].append(current_error)
    
    return severity_counts, error_types, file_locations, grouped_by_file, sorted(error_messages)

# Main output
if __name__ == "__main__":
    print("=" * 80)
    print("LOG FILE ANALYZER - COMPLETE REPORT")
    print("=" * 80)
    
    # ===== ACCESS LOG ANALYSIS =====
    print("\n" + "="*80)
    print("ACCESS LOG ANALYSIS")
    print("="*80)
    status_codes, endpoints, ip_addresses, failed_requests, failure_rate, response_size_stats = parseAccessLog()
    
    print("\n1. Requests by HTTP Status Code:")
    for code in sorted(status_codes.keys()):
        print(f"   {code}: {status_codes[code]} requests")
    
    print("\n2. Most Frequently Accessed Endpoints:")
    for endpoint in sorted(endpoints.items(), key=lambda x: x[1], reverse=True):
        print(f"   {endpoint[0]}: {endpoint[1]} requests")
    
    print("\n3. Unique IP Addresses:")
    for ip in sorted(ip_addresses):
        print(f"   {ip}")
    
    print("\n4. Failed Requests (4xx, 5xx):")
    for code in sorted(failed_requests.keys()):
        print(f"   {code}: {failed_requests[code]} requests")
    print(f"   Failure Rate: {failure_rate:.2%}")
    
    print("\n5. Response Size Statistics:")
    print(f"   Total Responses: {response_size_stats['count']}")
    print(f"   Total Bytes: {response_size_stats['total_bytes']}")
    print(f"   Min Bytes: {response_size_stats['min_bytes']}")
    print(f"   Max Bytes: {response_size_stats['max_bytes']}")
    print(f"   Avg Bytes: {response_size_stats['avg_bytes']:.2f}")
    print(f"   Median Bytes: {response_size_stats['median_bytes']}")
    
    # ===== APP LOG ANALYSIS =====
    print("\n" + "="*80)
    print("APPLICATION LOG ANALYSIS")
    print("="*80)
    severity_counts, error_messages, log_duration, temporal_patterns = parseAppLog()
    
    print("\n1. Logs by Severity Level:")
    for level in sorted(severity_counts.keys()):
        print(f"   {level}: {severity_counts[level]} entries")
    
    print("\n2. ERROR Messages (Chronological):")
    for idx, error in enumerate(error_messages, 1):
        print(f"   [{idx}] {error['timestamp']}: {error['message']}")
    
    print("\n3. Total Log Duration:")
    if log_duration:
        print(f"   Start: {log_duration['start']}")
        print(f"   End: {log_duration['end']}")
        print(f"   Duration: {log_duration['days']} days, {log_duration['hours']} hours, {log_duration['minutes']} minutes")
    
    print("\n4. Temporal Pattern Report (Log Entries Preceding Errors):")
    for idx, pattern in enumerate(temporal_patterns, 1):
        print(f"   [{idx}] Preceded by: {pattern['preceded_by']}")
        print(f"       Error: {pattern['error']}\n")
    
    # ===== ERROR LOG ANALYSIS =====
    print("\n" + "="*80)
    print("ERROR LOG ANALYSIS")
    print("="*80)
    severity_counts_err, error_types, file_locations, grouped_by_file, unique_errors = parseErrorLog()
    
    print("\n1. Errors by Severity Level:")
    for severity in sorted(severity_counts_err.keys()):
        print(f"   {severity}: {severity_counts_err[severity]} errors")
    
    print("\n2. Error Types and Frequencies:")
    for error_type in sorted(error_types.items(), key=lambda x: x[1], reverse=True):
        print(f"   {error_type[0]}: {error_type[1]} occurrences")
    
    print("\n3. File Locations Where Errors Occurred:")
    for filename in sorted(file_locations.keys()):
        print(f"   {filename}: {file_locations[filename]} errors")
    
    print("\n4. Errors Grouped by Source File:")
    for filename in sorted(grouped_by_file.keys()):
        print(f"   {filename}:")
        for error in grouped_by_file[filename]:
            print(f"      - {error['severity']}: {error['description']}")
    
    print("\n5. Unique Error Messages:")
    for idx, msg in enumerate(unique_errors, 1):
        print(f"   [{idx}] {msg}")
    
    print("\n" + "="*80)
    print("END OF REPORT")
    print("="*80)


