#!/usr/bin/env python3
import os
import glob
import yaml
import argparse


def main():
    parser = argparse.ArgumentParser(description='Convert nested YAMLs to list format for all languages except en.')
    parser.add_argument('input_dir', help='Directory with input YAML files (downloaded from tx)')
    parser.add_argument('output_dir', help='Directory to save converted YAML files')
    parser.add_argument('--skip', default='en', help='Language code to skip (default: en)')
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    for path in glob.glob(os.path.join(args.input_dir, '*.yml')):
        lang = os.path.splitext(os.path.basename(path))[0]
        if lang == args.skip:
            continue

        with open(path, encoding='utf-8') as f:
            data = yaml.safe_load(f)

        # If there's a root like {'ru': {...}}, extract the inner dictionary
        if isinstance(data, dict) and lang in data and isinstance(data[lang], dict):
            mapping = data[lang]
        elif isinstance(data, dict):
            mapping = data
        else:
            print(f"Skipping {path}: unexpected format")
            continue

        # Build a list of objects [{id, translation}, …]
        items = [{'id': key, 'translation': mapping[key]} for key in sorted(mapping)]
        out_path = os.path.join(args.output_dir, f'{lang}.yml')
        with open(out_path, 'w', encoding='utf-8') as f:
            yaml.dump(items, f, allow_unicode=True)

        print(f"✔ Converted {path} → {out_path}")

if __name__ == '__main__':
    main()