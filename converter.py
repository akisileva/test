import json

def jsonl_to_json(jsonl_file, json_file):
    with open(jsonl_file, 'r', encoding='utf-8') as infile:
        jsonl_data = infile.readlines()

    json_data = [json.loads(line.strip()) for line in jsonl_data]

    structured_data = {"train": [], "validation": [], "test": []}

    for example in json_data:
        if "train" in example:
            structured_data["train"].append({"input": example["train"]["input"], "output": example["train"]["output"]})
        elif "validation" in example:
            structured_data["validation"].append({"input": example["validation"]["input"], "output": example["validation"]["output"]})
        elif "test" in example:
            structured_data["test"].append({"input": example["test"]["input"], "output": example["test"]["output"]})

    with open(json_file, 'w', encoding='utf-8') as outfile:
        json.dump(structured_data, outfile, indent=4, ensure_ascii=False)

jsonl_file = 'D://fromtech//cef_december//output_dialogs_cef_december.jsonl'
json_file = 'december_structure.json'

jsonl_to_json(jsonl_file, json_file)