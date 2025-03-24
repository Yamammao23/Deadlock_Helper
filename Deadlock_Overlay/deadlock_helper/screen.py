from screeninfo import get_monitors

def get_secondary_monitor():
    monitors = get_monitors()
    if len(monitors) < 2:
        print("Only one monitor detected. Using primary.")
        return monitors[0]
    return monitors[1]
