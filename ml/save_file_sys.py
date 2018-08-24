def save_file():
    import sys, os
    args = sys.argv[1]
    cmd = "mv " + args + " ./TestFiles"
    os.system(cmd)
