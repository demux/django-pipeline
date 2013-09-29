from __future__ import unicode_literals

from pipeline.conf import settings
from pipeline.compilers import SubProcessCompiler

import os


class SwigCompiler(SubProcessCompiler):
    output_extension = 'js'

    def match_file(self, filename):
        return filename.endswith('.html') or filename.endswith('.jinja')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return  # File doesn't need to be recompiled

        name = infile.split('/')[-1].split('.')[0]

        command = ' '.join(filter(None, [
            settings.PIPELINE_SWIG_BINARY,
            'compile %s' % infile,
            settings.PIPELINE_SWIG_ARGUMENTS,
            '--wrap-start="var _swig_%s = "' % name,
            '> %s' % outfile,
        ]))

        return self.execute_command(command, cwd=os.path.dirname(infile))
