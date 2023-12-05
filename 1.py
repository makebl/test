import json

def merge_libraries(library1, library2):
    apps1 = library1.get('apps', [])
    apps2 = library2.get('apps', [])
    merged_apps = apps1 + apps2
    merged_library = library1.copy()
    merged_library['apps'] = merged_apps
    return merged_library

def main():
    file1_path = 'test.json'
    file2_path = 'apps.json'

    # Ensure test.json exists and is not empty
    try:
        with open(file1_path, 'r', encoding='utf-8') as test_file:
            test_content = json.load(test_file)
            if 'apps' not in test_content:
                test_content['apps'] = []
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading {file1_path}: {e}")
        test_content = {'apps': []}

    try:
        with open(file2_path, 'r', encoding='utf-8') as file2:
            library2 = json.load(file2)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading {file2_path}: {e}")
        library2 = {'apps': []}

    merged_library = merge_libraries(test_content, library2)

    with open('merged_library.json', 'w', encoding='utf-8') as merged_file:
        json.dump(merged_library, merged_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
