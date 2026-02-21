import os

p = os.getcwd()
for fname in ['index_v4.html', 'mobile_v4.html']:
    f = os.path.join(p, fname)
    if not os.path.exists(f):
        print(f"FAIL: {fname} not found")
        continue
    content = open(f, 'r', encoding='utf-8').read()
    checks = {
        'V4 in title': 'V4' in content[:500],
        'presets obj': 'const presets' in content,
        'setPreset fn': 'function setPreset' in content,
        'displayToPower': 'displayToPower' in content,
        'visorDisplay': 'visorDisplay' in content,
        'slider 0-30': 'min="0" max="30"' in content,
        'chartDecomp': 'chartDecomp' in content,
        'rcaBoostDB': 'rcaBoostDB' in content,
        'volSensationTable': 'volSensationTable' in content,
        'Volume Natural': 'Volume Natural' in content,
        'presetMax': 'presetMax' in content,
        'presetPotente': 'presetPotente' in content,
        'presetMedia': 'presetMedia' in content,
        'presetNatural': 'presetNatural' in content,
        'only 1 </html>': content.count('</html>') == 1,
        'only 1 </script>': content.count('</script>') <= 2,
    }
    all_ok = all(checks.values())
    print(f"\n{'='*50}")
    print(f"  {fname}: {'✅ ALL PASS' if all_ok else '❌ ISSUES FOUND'}")
    print(f"  Lines: {content.count(chr(10))+1}")
    print(f"{'='*50}")
    for k, v in checks.items():
        status = '✅' if v else '❌'
        print(f"  {status} {k}")
