from cudatext import *

MAX_LEN=50*1024

class Command:
    def on_caret(self, ed_self):
        carets = ed_self.get_carets()
        if len(carets)>1: return
        x,y,x2,y2 = carets[0]
        if y2!=-1:
            if (y2,x2)<(y,x):
                x,y,x2,y2 = x2,y2,x,y
            text = ed_self.get_text_substr(x,y,x2,y2)
            if len(text)>MAX_LEN:
                msg_status('[Auto-copy to clipboard] Cannot copy such big block')
                return
            app_proc(PROC_SET_CLIP, text)
            msg_status('[Auto-copy to clipboard] Copied "%s"'%(text))

