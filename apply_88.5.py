import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
base = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

# 1. Update text "87 dB" to "88.5 dB"
old_text = ">87 dB<"
new_text = ">88.5 dB<"
if old_text in content:
    content = content.replace(old_text, new_text)
    changes += content.count(new_text)
    print("Updated 87 dB -> 88.5 dB in table")

old_text2 = "sub de 87dB"
new_text2 = "sub de 88.5dB"
if old_text2 in content:
    content = content.replace(old_text2, new_text2)
    changes += content.count(new_text2)
    print("Updated 87dB -> 88.5dB in description")

# 2. Update presets with new 0.70 ratio values (88.5dB sensitivity)
# Old: gF=78 gS=65 -> New: gF=89 gS=62 (Maximo)
# Old: gF=49 gS=41 -> New: gF=56 gS=39 (Potente)
# Old: gF=31 gS=26 -> New: gF=36 gS=25 (Media)
# Old: gF=19 gS=16 -> New: gF=23 gS=16 (Natural)
# Old: gF=12 gS=10 -> New: gF=14 gS=10 (Baixo)

presets_replacements = [
    # Máximo
    (r"max:     \{ gF: 78, gS: 65, emoji: '🔥', name: 'Máximo c/ Qualidade', desc: '(.+?)' \}", 
     r"max:     { gF: 89, gS: 62, emoji: '🔥', name: 'Máximo c/ Qualidade', desc: '\1' }"),
    # Potente
    (r"potente: \{ gF: 49, gS: 41, emoji: '💪', name: 'Potente', desc: '(.+?)' \}",
     r"potente: { gF: 56, gS: 39, emoji: '💪', name: 'Potente', desc: '\1' }"),
    # Média
    (r"media:   \{ gF: 31, gS: 26, emoji: '🎵', name: 'Média', desc: '(.+?)' \}",
     r"media:   { gF: 36, gS: 25, emoji: '🎵', name: 'Média', desc: '\1' }"),
    # Natural
    (r"natural: \{ gF: 19, gS: 16, emoji: '🌿', name: 'Volume Natural', desc: '(.+?)' \}",
     r"natural: { gF: 23, gS: 16, emoji: '🌿', name: 'Volume Natural', desc: '\1' }"),
    # Baixo
    (r"baixo:   \{ gF: 12, gS: 10,  emoji: '🔈', name: 'Volume Baixo', desc: '(.+?)' \}",
     r"baixo:   { gF: 14,  gS: 10,  emoji: '🔈', name: 'Volume Baixo', desc: '\1' }"),
    # Backup formats just in case spacing differs
    (r"gF: 78, gS: 65", "gF: 89, gS: 62"),
    (r"gF: 49, gS: 41", "gF: 56, gS: 39"),
    (r"gF: 31, gS: 26", "gF: 36, gS: 25"),
    (r"gF: 19, gS: 16", "gF: 23, gS: 16"),
    (r"gF: 12, gS: 10", "gF: 14, gS: 10"),
    (r"gF: 12,  gS: 10", "gF: 14,  gS: 10")
]

for old_p, new_p in presets_replacements:
    new_content = re.sub(old_p, new_p, content)
    if new_content != content:
        changes += 1
        content = new_content
        print(f"Applied preset regex replacement for {new_p[-20:]}")

# Check if Sub power notation exists and needs updating (169W -> 154W)
if "Sub a 169W" in content:
    content = content.replace("Sub a 169W", "Sub a 154W")
    changes += 1
    print("Updated Sub max power text to 154W")

# Check version
if "V5" in content and "V5.2" not in content:
    content = content.replace("V5", "V5.2", 1) # Only update the title/header
    changes += 1

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Total changes applied: {changes}")

# Verification
with open(index_path, 'r', encoding='utf-8') as f:
    v = f.read()
    
m = re.findall(r'(max|potente|media|natural|baixo):\s*\{\s*gF:\s*(\d+),\s*gS:\s*(\d+).*?~(\d+)dB', v)
print("\nFinal Presets in File:")
for p, gf, gs, spl in m:
    print(f"  {p}: gF={gf} gS={gs} ~{spl}dB")

if ">88.5 dB<" in v:
    print("Table updated OK")
else:
    print("Table NOT UPDATED OR NOT FOUND")
