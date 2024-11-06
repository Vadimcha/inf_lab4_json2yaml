import json

import yaml

with open('schedule.json', 'r') as file:
    data = str(json.load(file))

def json_yaml(x):
    x = x[1:-1]
    x = x.replace("[]", "ABOBA")
    x = x.replace("{}", "BIBA")

    x = x.replace("\"", "'")

    i = 0
    t = False
    while i < len(x):
        if x[i] == '\'':
            t = not t
        elif x[i] == ',' and t:
            x = x[:i] + "COMA" + x[i + 1:]
        i += 1

    x = x.replace(", ", ",")
    kol = 0     # отвечает за кол-во [ и {
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
    x = x.replace("'", "")
    x = x.replace(']', '')
    x = x.replace('}', '')
    x = x.replace("None", "null")

    x = x.replace("ABOBA", "[]")
    x = x.replace("COMA", ",")
    x = x.replace("BIBA", "{}")
    x = "---\n" + x
    return x


new_data = json_yaml(data)
# with open("result_must_have_task.yaml", "w", encoding="utf-8") as file:
#     file.write(new_data)
print(new_data)
