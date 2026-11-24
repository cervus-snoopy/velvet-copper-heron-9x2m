import os

LINE = "You finish your homework, you leave for school. I ate it so you stay. I'd do it again tomorrow."

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
os.chmod(out_dir, 0o755)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
os.chmod(path, 0o644)
