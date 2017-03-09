from cudatext import *

#Linux gtk2 has 3 buffers:
#  a) clipboard, b) primary selection, c) secondary selection
#You can auto-copy to 1st, 2nd or 1st+2nd
TO_CLIPBOARD = False #True
TO_PRIMARY_SEL = True

#misc options
MIN_LEN = 1
MAX_LEN = 50*1024
MAX_SHOW = 80
PREFIX = '[Auto-Copy] '

if app_api_version()<'1.0.170':
    msg_box('Auto-Copy plugin needs newer app version', MB_OK+MB_ICONERROR)


class Command:
    def on_caret(self, ed_self):
        carets = ed_self.get_carets()
        if len(carets)>1: return

        s = ed_self.get_text_sel()
        if not s: return
        if len(s)<MIN_LEN: return
        if len(s)>MAX_LEN: return msg_status(PREFIX+'Too big block')

        if TO_CLIPBOARD:
            app_proc(PROC_SET_CLIP, s)
        if TO_PRIMARY_SEL:
            app_proc(PROC_SET_CLIP_ALT, s)

        if len(s)>MAX_SHOW:
            s = s[:MAX_SHOW]+'...'
        kind = '[main/primary] ' if TO_CLIPBOARD and TO_PRIMARY_SEL else '[main] ' if TO_CLIPBOARD else '[primary] ' if TO_PRIMARY_SEL else ' '
        msg_status(PREFIX+kind+'Copied "%s"'%s)
