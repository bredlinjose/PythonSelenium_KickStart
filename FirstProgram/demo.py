import pathlib
from pathlib import Path

import os

print('File name :    ', os.path.basename(__file__))
print('Directory Name:     ', os.path.dirname(__file__))
pathLoc = os.path.join(os.path.dirname(__file__), "file\\dummy.png")
print(pathLoc)

loc = Path(__file__).parent.parent.joinpath("file\\dummy.png")
print(loc)

print(pathlib.Path().absolute())
