#!/usr/bin/python3
import subprocess as sp
import shutil as sh
from pathlib import Path

sp.check_call(['cargo', 'build', '--package', 'rlib'])
sh.copy(Path('target/debug/librlib.rlib'), Path("main/rlibdir/"))
sp.check_call(['cargo', 'run', '--bin', 'main', '--verbose'])
