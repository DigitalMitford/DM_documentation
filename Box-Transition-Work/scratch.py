from pathlib import Path
import os
from os import mkdir
projectPath = Path('E:/Users/Lisa Documents/Documents/GitHub/Digital-Mitford-Organization/DM_documentation/Box-Transition-Work')
newFolder = "elisa"
commentFile = "comment.txt"
Path(projectPath/newFolder).mkdir()
newPath = os.path.join(projectPath, newFolder, commentFile)
commentFile = open(newPath, 'w')
contents = 'Testing to add content to this file.'
commentFile.write(contents)
commentFile.close()
print(commentFile)
