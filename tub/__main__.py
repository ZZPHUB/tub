import sys
from tub import init
from tub import loop


argv_list = sys.argv
tub_info = init.app_info_mode()
loop.argv_progress(argv_list,tub_info)
loop.translate_recur(tub_info)
