def error_print(msg):
    """Print a message in red."""
    
    print(f'\033[91mERROR: {msg}\033[0m')

def success_print(msg):
    """Print a message in green."""
    
    print(f'\033[92mSUCCESS: {msg}\033[0m')
