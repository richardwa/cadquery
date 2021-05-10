
import re
import sys

from cq_editor import utils
utils.confirm = lambda a, b, c: True


from cq_editor.widgets.editor import Editor
original_load_from_file = Editor.load_from_file


def load_from_file(self, fname):
    original_load_from_file(self, fname)
    self.triggerRerender.emit(True)


Editor.load_from_file = load_from_file

from cq_editor.__main__ import main

if __name__ == '__main__':
    sys.exit(main())
