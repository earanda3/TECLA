import os, json
base = '/Users/zen/Desktop/web_TECLA/device_files'
skip_names = {'.DS_Store', 'README.md', '.VolumeIcon.icns', 'boot_out.txt', 'tecla_config.json', 'tecla_icon.png'}
skip_exts  = ['.pyc', '.bak']
files = []
for root, dirs, fnames in os.walk(base):
    dirs[:] = sorted(d for d in dirs if d not in ['__pycache__', '.vscode'] and not d.startswith('.'))
    for f in sorted(fnames):
        if f in skip_names or f.startswith('.') or any(f.endswith(e) for e in skip_exts):
            continue
        rel = os.path.relpath(os.path.join(root, f), base)
        files.append(rel)
out = json.dumps({'files': files}, indent=2)
open('/Users/zen/Desktop/web_TECLA/device_files_manifest.json', 'w').write(out)
print('Generated', len(files), 'files')
