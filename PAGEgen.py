import subprocess
subprocess.run(["rm","PAGE.md"])
output = subprocess.check_output(["ls", "Wallpapers/"])
text = output.decode().split()
PAGE = open ("PAGE.md", "w")
URL = "https://raw.githubusercontent.com/EnderSpy29/Wacky-Walls/refs/heads/main/Wallpapers/"
for line in text:
    link = URL + line
    PAGE.write(f"<img src={link}>\n")