#!/usr/bin/env python3
import os
import yaml
import argparse


def main():
    parser = argparse.ArgumentParser(description='Convert flat yml list to nested dict under language root.')
    parser.add_argument('input', help='Path to input YAML file (list of objects)')
    parser.add_argument('output', help='Path to output YAML file (nested under language root)')
    parser.add_argument('--lang', default='en', help='Language code for root key (default: en)')
    args = parser.parse_args()

    # 1) Load your list of objects
    with open(args.input, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    if isinstance(data, list):
        mapping = {item['id']: item['translation'] for item in data}
    else:
        raise RuntimeError(f"Expected a list in {args.input}, got {type(data)}")

    # 2) Package under the language root
    out = {args.lang: mapping}
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        yaml.dump(out, f, allow_unicode=True)
    print(f"✅ Converted {args.input} → {args.output}")

if __name__ == '__main__':
    main()