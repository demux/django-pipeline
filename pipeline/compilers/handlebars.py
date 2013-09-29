from __future__ import unicode_literals

from pipeline.conf import settings
from pipeline.compilers import SubProcessCompiler

import os


class HandlebarsCompiler(SubProcessCompiler):
    output_extension = 'js'

    def match_file(self, filename):
        return filename.endswith('.hbs') or filename.endswith('.handlebars')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return  # File doesn't need to be recompiled

        command = ' '.join(filter(None, [
            settings.PIPELINE_HANDLEBARS_BINARY,
            infile,
            settings.PIPELINE_HANDLEBARS_ARGUMENTS,
            '-r %s' % os.path.dirname(infile),
            '-f %s' % outfile,
        ]))

        return self.execute_command(command)


class EmberHandlebarsCompiler(HandlebarsCompiler):
    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return  # File doesn't need to be recompiled

        command = ' '.join(filter(None, [
            settings.PIPELINE_EMBER_HANDLEBARS_BINARY,
            infile,
            '-f %s' % outfile
        ]))

        return self.execute_command(command)
