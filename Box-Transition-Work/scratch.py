from pathlib import Path
import os
from os import mkdir
projectPath = Path('E:/Users/Lisa Documents/Documents/GitHub/Digital-Mitford-Organization/DM_documentation/Box-Transition-Work')
var = "elisa"
newPath = os.path.join(projectPath, var)
mkdir(newPath)
