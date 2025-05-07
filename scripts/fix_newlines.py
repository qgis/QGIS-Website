#!/usr/bin/env python3
import os
import re
import sys
import glob

def process_po_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all msgid and msgstr blocks
    pattern = r'(msgid\s+".*?")(\s+)(msgstr\s+".*?")'
    blocks = re.findall(pattern, content, re.DOTALL)
    
    modified = False
    for msgid, spacing, msgstr in blocks:
        # Check if there's a newline at the end of msgstr but not in msgid
        msgid_has_newline = msgid.rstrip().endswith('\\n"')
        msgstr_has_newline = msgstr.rstrip().endswith('\\n"')
        
        if not msgid_has_newline and msgstr_has_newline:
            # Remove \n from end of msgstr
            new_msgstr = re.sub(r'\\n"$', '"', msgstr.rstrip())
            # Replace in original content
            content = content.replace(msgstr, new_msgstr)
            modified = True
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed newlines in {file_path}")
    
    return modified

def main():
    # Process all .po files in the translations directory
    po_files = glob.glob('translations/**/*.po', recursive=True)
    fixed_count = 0
    
    for po_file in po_files:
        if process_po_file(po_file):
            fixed_count += 1
    
    print(f"Fixed newlines in {fixed_count} files")

if __name__ == "__main__":
    main() 