import subprocess



proc = subprocess.run(
    ['ping', '127.0.0.1', '-c', '4']
)


