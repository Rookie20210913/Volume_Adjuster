import subprocess
import os

# subprocess.run(['start','cmd','/k','.\\audio_testenv\\Scripts\\activate','python','-m','controller'],shell=True)

os.system('start cmd.exe cmd /k "cd .. && audio_testenv\\Scripts\\activate && python -m controller"')
# os.system('cmd /k "python -m controller"')