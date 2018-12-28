#!/usr/bin/env python3

import os
import sys
import subprocess

from config import Config


def main(config_path='io_args.yml'):
    try:
        cfg = Config(config_path).load()

        if not os.path.exists(cfg['output_data_directory']):
            os.makedirs(cfg['output_data_directory'])

        subprocess.run([cfg['hunalign_exe'],
                        '-realign',
                        '-text',
                        '-batch',
                        cfg['hunspell_null_dic'],
                        cfg['batch_filepath']])
    except Exception as ex:
        sys.stderr.write(repr(ex))
        return 1


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
