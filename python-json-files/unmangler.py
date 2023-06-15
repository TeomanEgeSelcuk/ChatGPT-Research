import codecs
import re
import json

def unmangle_utf8(match):
    escaped = match.group(0)                   # '\\u00e2\\u0082\\u00ac'
    hexstr = escaped.replace(r'\u00', '')      # 'e282ac'
    buffer = codecs.decode(hexstr, "hex")      # b'\xe2\x82\xac'

    try:
        return buffer.decode('utf8')           # '€'
    except UnicodeDecodeError:
        print("Could not decode buffer: %s" % buffer)

# Read broken JSON from data.json
with open("data.json", "r", encoding="utf-8") as file:
    broken_json = file.read()

# Unmangle UTF-8 sequences in broken JSON
converted = re.sub(r"(?i)(?:\\u00[0-9a-f]{2})+", unmangle_utf8, broken_json)

# Parse the converted JSON
try:
    parsed_json = json.loads(converted)
    # Print unmangled value pairs
    for key, value in parsed_json.items():
        print(f"{key}: {value}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {str(e)}")
