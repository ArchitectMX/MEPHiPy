import re


LOG_PATTERN = re.compile(
    r"^(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"(?P<level>INFO|WARNING|ERROR) "
    r"User (?P<user_id>\d+) "
    r"(?P<message>.+)$"
)


def parse_log(line):
    match = LOG_PATTERN.fullmatch(line)
    return match.groupdict() if match else None


if __name__ == "__main__":
    logs = [
        "2026-09-24 10:15:32 INFO User 123 logged in",
        "2026-09-24 10:16:04 ERROR User 456 authentication failed",
        "2026-09-24 10:17:21 INFO User 123 opened page",
        "2026-09-24 10:18:45 WARNING User 789 too many requests",
        "2026-09-24 10:19:02 ERROR User 123 database connection failed",
    ]

    parsed_logs = []
    for log in logs:
        parsed_log = parse_log(log)
        if parsed_log is not None:
            parsed_logs.append(parsed_log)

    for log in parsed_logs:
        print(log)
