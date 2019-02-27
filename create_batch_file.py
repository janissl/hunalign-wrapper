#!/usr/bin/env python3

import os
import sys
import csv

from config import Config


def write_batch_file(cfg):
    source_text_file_suffix = '_{}.snt'.format(cfg['source_language'])
    target_text_file_suffix = '_{}.snt'.format(cfg['target_language'])

    lang_pair = '{}-{}'.format(cfg['source_language'], cfg['target_language'])
    lang_pair_work_directory = os.path.join(cfg['work_directory'], lang_pair)

    if not os.path.exists(os.path.dirname(cfg['batch_filepath'])):
        os.makedirs(os.path.dirname(cfg['batch_filepath']))

    with open(cfg['batch_filepath'], 'w', encoding='utf-8', newline='\n') as batch:
        writer = csv.writer(batch, dialect=csv.excel_tab)

        for entry in os.scandir(cfg['source_data_directory']):
            if entry.is_file() and entry.name.endswith(source_text_file_suffix):
                pair_title = entry.name[:-len(source_text_file_suffix)]
                target_text_filepath = os.path.join(os.path.dirname(entry.path), (pair_title + target_text_file_suffix))

                if os.path.exists(target_text_filepath):
                    output_name = '{}.{}.aligned'.format(pair_title, lang_pair)
                    output_path = os.path.join(lang_pair_work_directory, output_name)
                    writer.writerow([entry.path, target_text_filepath, output_path])

    if not os.path.exists(lang_pair_work_directory):
        os.makedirs(lang_pair_work_directory)


def main(config_path='io_args.yml'):
    try:
        cfg = Config(config_path).load()
        write_batch_file(cfg)
    except Exception as ex:
        sys.stderr.write(repr(ex))
        return 1


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
