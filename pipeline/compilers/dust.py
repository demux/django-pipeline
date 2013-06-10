from __future__ import unicode_literals

from pipeline.conf import settings
from pipeline.compilers import SubProcessCompiler


class DustCompiler(SubProcessCompiler):
    output_extension = 'js'

    def match_file(self, filename):
        print filename
        return filename.endswith('.dust')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return  # File doesn't need to be recompiled

        command = ' '.join(filter(None, [
            settings.PIPELINE_DUST_BINARY,
            '--name="%s"' % infile.split('/')[-1].split('.')[0],
            infile,
            outfile
        ]))

        return self.execute_command(command)
