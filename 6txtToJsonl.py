import re
import json

with open('data2_cef_november.txt', 'r', encoding='utf-8') as file:
    content = file.read()

dialog_pattern = re.compile(r'(human|bot): (.+?)(?=(?:human|bot):|$)')

dialogs = dialog_pattern.findall(content)

jsonl_data = []
for i in range(0, len(dialogs), 2):
    human_input = dialogs[i][1].strip()
    bot_output = dialogs[i + 1][1].strip() if i + 1 < len(dialogs) else ''
    jsonl_data.append(f'{{"input": "{human_input}", "output": "{bot_output}"}}')


with open('output_dialogs_cef_november.jsonl', 'w', encoding='utf-8') as jsonl_file:
    for item in jsonl_data:
        jsonl_file.write(item + '\n')