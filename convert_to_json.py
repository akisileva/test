import json
from sklearn.model_selection import train_test_split

def read_jsonl_file(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(json.loads(line))
    return data

def convert_to_structure(data):
    structure = {"train": [], "validation": [], "test": []}
    
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
    validation_data, test_data = train_test_split(test_data, test_size=0.5, random_state=42)
    
    structure["train"] = [{"input": entry["input"], "output": entry["output"]} for entry in train_data]
    structure["validation"] = [{"input": entry["input"], "output": entry["output"]} for entry in validation_data]
    structure["test"] = [{"input": entry["input"], "output": entry["output"]} for entry in test_data]
    
    return structure

def write_json_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

jsonl_file_path = 'D://fromtech//cef_november//november_copy.jsonl'
output_json_file_path = 'mini_data.json'

data = read_jsonl_file(jsonl_file_path)
structured_data = convert_to_structure(data)
write_json_file(structured_data, output_json_file_path)