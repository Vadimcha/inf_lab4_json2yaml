import json
import re

with open('schedule.json', 'r') as file:
    data = str(json.load(file))


def replacement(match):
    return f"{match.group(1)}COMA{match.group(3)}"

def json_yaml(x):
    x = re.sub(r"\[]", "ABOBA", x)
    x = re.sub(r"\{}", "BIBA", x)
    x = re.sub(r"\"", "'", x)

    def replacerComa(match):
        quoted_string = match.group(1)
        return "'" + re.sub(r',', lambda m: 'COMA', quoted_string) + "'"
    x = re.sub(r"'(.*?)'", replacerComa, x)

    x = re.sub(r", ", ",", x)

    kol = 0
    i = 0
    while i < len(x):
        g = x[i]
        if x[i] == '[' and (i != len(x) - 1 and x[i + 1] == '{'):
            x = x[:i] + "\n" + "  " * kol + "- " + x[i + 2:]
            kol += 1
            i += 1
        elif x[i] == '}' and (i != len(x) - 1 and x[i + 1] == ']'):
            kol -= 1
            i += 1
        elif x[i] == '}' or x[i] == ']':
            kol -= 1
        elif x[i] == '[' or x[i] == '{':
            x = x[:i] + "  " * (kol - 1) + "- " + x[i + 1:]
            kol += 1
        elif x[i] == ',':
            x = x[:i] + "\n" + "  " * kol + x[i + 1:]
        i += 1

    x = re.sub(r"[\'\]}]", '', x)
    x = re.sub(r"None", "null", x)
    x = re.sub(r"ABOBA", "[]", x)
    x = re.sub(r"BIBA", "{}", x)
    x = re.sub(r"COMA", ",", x)

    x = "---\n" + x
    return x

data = data[1:-1]
new_data = json_yaml(data)
# with open("result_dop2.yaml", "w", encoding="utf-8") as file:
#     file.write(new_data)
print(new_data)