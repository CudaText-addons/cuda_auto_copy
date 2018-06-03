import os
from cudatext import *
from . import opt

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_auto_copy.ini')

def bool_to_str(v): return '1' if v else '0'
def str_to_bool(s): return s=='1'

PREFIX = '[Auto-Copy] '

class Command:

    def __init__(self):
    
        opt.min_len = int(ini_read(fn_config, 'op', 'min_len', str(opt.min_len)))
        opt.max_len = int(ini_read(fn_config, 'op', 'max_len', str(opt.max_len)))
        opt.copy_to_clp = str_to_bool(ini_read(fn_config, 'op', 'copy_to_clipboard', bool_to_str(opt.copy_to_clp)))
        opt.copy_to_prim = str_to_bool(ini_read(fn_config, 'op', 'copy_to_primary_sel', bool_to_str(opt.copy_to_prim)))

    def config(self):

        ini_write(fn_config, 'op', 'min_len', str(opt.min_len))
        ini_write(fn_config, 'op', 'max_len', str(opt.max_len))
        ini_write(fn_config, 'op', 'copy_to_clipboard', bool_to_str(opt.copy_to_clp))
        ini_write(fn_config, 'op', 'copy_to_primary_sel', bool_to_str(opt.copy_to_prim))
        file_open(fn_config)

    def on_caret(self, ed_self):
    
        carets = ed_self.get_carets()
        if len(carets)>1: return

        s = ed_self.get_text_sel()
        if not s: return
        if len(s)<opt.min_len: return
        if len(s)>opt.max_len: return msg_status(PREFIX+'Too big block')

        if opt.copy_to_clp:
            app_proc(PROC_SET_CLIP, s)
        if opt.copy_to_prim:
            app_proc(PROC_SET_CLIP_ALT, s)

        if len(s)>opt.max_show_len:
            s = s[:opt.max_show_len]+'...'
        kind = '[main/primary] ' if opt.copy_to_clp and opt.copy_to_prim else '[main] ' if opt.copy_to_clp else '[primary] ' if opt.copy_to_prim else ' '
        msg_status(PREFIX+kind+'Copied "%s"'%s)
