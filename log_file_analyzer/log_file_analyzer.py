import re
import os
import statistics

def parseAccessLog(log="logs/access.log"):
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

def parseAppLog(log="app.log"):
    pass

def parseErrorLog():
    pass

print(f"Status Codes: {parseAccessLog()[0]}")
print(f"Endpoints: {parseAccessLog()[1]}")
print(f"IP Addresses: {parseAccessLog()[2]}")
print(f"Failed requests: {parseAccessLog()[3]}")
print(f"Failure Rate: {parseAccessLog()[4]}")
print(f"Response size stats: {parseAccessLog()[5]}")
