import os

def main():
    """
    This function gets invoked when the phone gets unlocked. Look into
    the README at the root of this repo.
    
    Since this is just a sample, an ugly os.system(..) will do. ;-)
    """
    os.system("loginctl unlock-session")
