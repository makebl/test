import json

def merge_json(file1, file2, output_file):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        json1 = json.load(f1)
        json2 = json.load(f2)

    merged_json = {**json1, **json2}

    with open(output_file, 'w', encoding='utf-8') as output_f:
        json.dump(merged_json, output_f, ensure_ascii=False, indent=4)

# 使用示例
merge_json('test.json', 'apps.json', 'output.json')
