import re

def main():
    test_str = '    - std::vector< int >               GetTokenIds(const GlobalId& id, std::string name, std::vector< Projectptr > apProject) override'

    print(test_str)

    test_str = re.sub(r'\s*-\s*', r'', test_str)
    print(r'Removed leading chars: ' + test_str)


    test_str = re.sub(r'^(.*)(\s+\w*)(\(.*\)).*', r'\1_\2_\3', test_str)
    tmp = re.split(r'_', test_str)
    params = tmp[2]
    print(r'Type:   ' + tmp[0]).strip()
    print(r'Name:   ' + tmp[1]).strip()
    print(r'Params: ' + tmp[2]).strip()

    param_list = re.split(r',', re.sub(r'\((.*)\)', r'\1', params))
    for item in param_list:
        item = re.sub(r'(const|&)', '', item)
        tmp = re.split(r'_', re.sub(r'^(.*)\s+(\w*)$', r'\1_\2', item))
        print(r'Param type: ' + tmp[0].strip())
        print(r'Param name: ' + tmp[1].strip())



if __name__ == '__main__':
    main()
