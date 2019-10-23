# Packages are a way of structuring Python’s module namespace 
# by using “dotted module names”. For example, the module name 
# A.B designates a submodule named B in a package named A.

"""
    sound/                      Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

"""
# Users of the package can import individual modules from the 
# package, for example:
import sound.effects.echo
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# An alternative way of importing the submodule is:
from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)

# Yet another variation is to import the desired function 
# or variable directly:
from sound.effects.echo import echofilter
echofilter(input, output, delay=0.7, atten=4)


