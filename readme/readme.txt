plugin for CudaText.
on making text selection (with mouse, shift+arrows, ctrl+A, etc), copies selected block to clipboard.

- handles forward/backward selections.
- won't work with multi-carets.
- won't work for too big blocks (limit is 50K, it is option).
- won't handle vertical blocks.

plugin has config file, to call it, use menu item in "Options / Settings-plugins / Auto-Copy to Clipboard".

- min_len: min length of selection to handle.
- max_len: max length of selection to handle (to not freeze on huge block).
- copy_to_clipboard (0 or 1): auto-copy to usual clipboard.
    if you want to disable auto-copy to usual clipboard, set option to 0.
    this is good, if you don't want to overwrite usual clipboard with Auto-Copy, 
    and want Auto-Copy set only primary-sel buffer. then middle-click-paste 
    will paste from primary-sel buffer, and it's like in Linux apps.
- copy_to_primary_sel (0 or 1): auto-copy to primary-selection. 
    (alternate buffer in Linux GTK library, it's used by CudaText on middle-button-click, 
    and by other Linux editors too.)


author: Alexey Torgashin (CudaText)
license: MIT