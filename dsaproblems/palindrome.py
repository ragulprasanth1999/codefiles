import cowsay
import sys
if len(sys.argv)==2:
    sys.exit("hello "+sys.argv[1])
elif len(sys.argv)>2:
    sys.exit("Too many argument")
elif len(sys.argv)<2:
    SystemExit.exit("Too less argument")