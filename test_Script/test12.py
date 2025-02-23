import os
import signal
import psutil

def find_obs_process():
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'].lower() == 'obs64.exe':  # Windows用。macOSの場合は'observer.app'など。
            return proc
    return None

def kill_process(process):
    try:
        os.kill(process.pid, signal.SIGTERM)
        print(f"Process {process.name()} (PID: {process.pid}) has been terminated.")
    except Exception as e:
        print(f"Failed to terminate the process. Error: {e}")

def main():
    obs_process = find_obs_process()
    if obs_process:
        kill_process(obs_process)
    else:
        print("OBS process not found.")

if __name__ == "__main__":
    main()
