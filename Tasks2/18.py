from pathlib import Path
import json
import logging
import re


def analyze_access(source, destination):
    methods = {}
    urls = {}
    errors = 0
    pattern = re.compile(
        r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} "
        r"(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) (?P<method>[A-Z]+) "
        r"(?P<url>\S+) (?P<status>\d{3})$"
    )
    logging.info("Начало обработки %s", source)
    with open(source, encoding="utf-8") as f:
        for number, line in enumerate(f, 1):
            match = pattern.fullmatch(line.strip())
            if not match:
                logging.warning("Пропущена строка %s", number)
                continue
            request = match.groupdict()
            method = request["method"]
            url = request["url"]
            methods[method] = methods.get(method, 0) + 1
            urls[url] = urls.get(url, 0) + 1
            if 400 <= int(request["status"]) < 500:
                errors += 1
    popular = None
    if urls:
        popular = max(urls, key=urls.get)
    result = {"methods": methods, "errors_4xx": errors, "most_common_url": popular}
    with open(destination, "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)
    logging.info("Обработка завершена")
    return result


base = Path(__file__).resolve().parent
logging.basicConfig(filename=base / "processing.log", level=logging.INFO, encoding="utf-8")
try:
    print(analyze_access(base / "access.log", base / "access_result.json"))
except (OSError, UnicodeError) as error:
    logging.exception("Ошибка обработки файла")
    print("Ошибка:", error)
