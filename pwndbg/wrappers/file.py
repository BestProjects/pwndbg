#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import subprocess
import pwndbg.wrappers

@pwndbg.wrappers.OnlyWithCommand
def is_statically_linked():

    local_path = pwndbg.file.get_file(pwndbg.proc.exe)
    cmd = [is_statically_linked.command_path, local_path]
    file_out = subprocess.check_output(cmd).decode('utf-8')

    if "statically" in file_out:
        return True
    else:
        return False
