plugin for CudaText.
on selection (with mouse, shift+arrows, ctrl+A, etc), copies selected block to clipboard.

wont work with multi-carets.
wont work for too big blocks (default is 50K, you can change constant in source).
wont handle vertical blocks.
handles forward/backward selections.


plugin has options inside __init__.py file
(if boolean, True means "on", False means "off"):
  - TO_CLIPBOARD - auto-copy to usual clipboard (exists in every OS)
  - TO_PRIMARY_SEL - auto-copy to primary-selection (alternate buffer on Linux gtk2, it's used by CudaText on middle-button-click, and by other Linux editors too.)
if you want to disable auto-copy to usual clipboard, set TO_CLIPBOARD to False. this is good, if you don't want to overwrite usual clipboard with Auto-Copy, and want Auto-Copy set only primary-sel buffer. then middle-click-paste will paste from primary-sel buffer, and it's like in Linux apps.


author: Alexey (CudaText)
license: MIT
