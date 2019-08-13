import re

def main():
    test_str = '    - std::vector< int >              : GetTokenIds(conat GlobalId& id, std::string name) override'

    print(test_str)

    test_str = re.sub(r'\s*-\s*', r'', test_str)
    print(r'Removed leading chars: ' + test_str)


    test_str = re.sub(r'^(.*)(\s+\w*)(\(.*\)).*', r'\1_\2_\3', test_str)
    tmp = re.split(r'_', test_str)
    print(r'Type:   ' + tmp[0]).strip()
    print(r'Name:   ' + tmp[1]).strip()
    print(r'Params: ' + tmp[2]).strip()


if __name__ == '__main__':
    main()
