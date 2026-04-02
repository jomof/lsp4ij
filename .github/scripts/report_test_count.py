#!/usr/bin/env python3
import os
import sys
import xml.etree.ElementTree as ET

def main():
    variant = sys.argv[1] if len(sys.argv) > 1 else ""
    title_suffix = f" ({variant})" if variant else ""
    
    total_tests = 0
    dir_path = 'build/test-results/test'
    if os.path.exists(dir_path):
        for filename in os.listdir(dir_path):
            if filename.endswith('.xml'):
                try:
                    tree = ET.parse(os.path.join(dir_path, filename))
                    root = tree.getroot()
                    if root.tag == 'testsuites':
                        total_tests += int(root.get('tests', 0))
                    elif root.tag == 'testsuite':
                        total_tests += int(root.get('tests', 0))
                except Exception:
                    pass
    
    summary_path = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary_path:
        with open(summary_path, 'a') as f:
            f.write(f'## Individual Tests Run{title_suffix}: {total_tests}\n')
    else:
        print(f"Individual Tests Run{title_suffix}: {total_tests}")

if __name__ == "__main__":
    main()
