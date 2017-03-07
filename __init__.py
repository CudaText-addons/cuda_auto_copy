from cudatext import *

MIN_LEN = 1
MAX_LEN = 50*1024
MAX_SHOW = 80
PRE = '[Auto-Copy] '

class Command:
    def on_caret(self, ed_self):
        carets = ed_self.get_carets()
        if len(carets)>1: return

        s = ed_self.get_text_sel()
        if not s: return
        if len(s)<MIN_LEN: return
        if len(s)>MAX_LEN: return msg_status(PRE+'Too big block')
        app_proc(PROC_SET_CLIP, s)

        if len(s)>MAX_SHOW:
            s = s[:MAX_SHOW]+'...'
        msg_status(PRE+'Copied "%s"'%s)
