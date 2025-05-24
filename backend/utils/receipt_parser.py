import re
from datetime import datetime

def parse_receipt_text(text):
    items = []
    lines = text.split('\n')

    for line in lines:
        # Match lines like "Milk 2L - $4.99"
        match = re.match(r"(.*)\s+-?\s*\$?(\d+\.\d{2})", line)
        if match:
            name = match.group(1).strip()
            price = float(match.group(2))
            items.append({"name": name, "price": price})
        
        # Optional: match date line
        if "date" in line.lower():
            try:
                date = re.search(r"\d{4}-\d{2}-\d{2}", line).group(0)
            except:
                date = str(datetime.today().date())
        else:
            date = str(datetime.today().date())

    return items, date
