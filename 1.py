import json

def merge_libraries(library1, library2):
    merged_data = {
        "libraries": [library1, library2]
    }
    return merged_data

def main():
    # 读取第一个 JSON 文件
    with open("test.json", "r", encoding="utf-8") as file1:
        library1 = json.load(file1)

    # 读取第二个 JSON 文件
    with open("apps.json", "r", encoding="utf-8") as file2:
        library2 = json.load(file2)

    # 合并两个 IPA 库
    merged_library = merge_libraries(library1, library2)

    # 将合并后的数据写入新的 JSON 文件
    with open("merged_library.json", "w", encoding="utf-8") as output_file:
        json.dump(merged_library, output_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
