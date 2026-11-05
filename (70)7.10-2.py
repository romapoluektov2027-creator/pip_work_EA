from pathlib import Path

def get_folder_size(path):
    total = 0
    for p in Path(path).rglob("*"):
        if p.is_file():
            try:
                total += p.stat().st_size
            except OSError:
                pass
    return total

size = get_folder_size("/var/adm/guchi")
print(f"{size} байт")
print(f"{size / 1024 / 1024:.1f} МБ")