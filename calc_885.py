import math

# Target: Sub is exactly 3.4 dB louder than Front at same volume factor
# Front base: 93 (sens) + 3 (pair) = 96 dB @ 1W
# Sub base: 88.5 (sens) + 8 (cabin) = 96.5 dB @ 1W
# F_SPL = 96 + 10*log10(100 * (gF/100)^2)
# S_SPL = 96.5 + 10*log10(400 * (gS/100)^2)
# S_SPL - F_SPL = 3.4 dB

def calcSPL(gF, gS):
    pwrF = 100 * (gF / 100) ** 2
    pwrS = 400 * (gS / 100) ** 2
    splF = 93 + 10 * math.log10(max(0.001, pwrF)) + 3
    splS = 88.5 + 10 * math.log10(max(0.001, pwrS)) + 8
    sSys = 10 * math.log10(10 ** (splF / 10) + 10 ** (splS / 10))
    diff = splS - splF
    return round(sSys, 1), round(pwrF, 1), round(pwrS, 1), round(diff, 2)

targets = {
    'max': 120,
    'potente': 116,
    'media': 112,
    'natural': 108,
    'baixo': 104,
}

print("=== SD 800.5 EVO 6 Preset Calculator (Sub 88.5dB) ===")
print("Front: 100W/ch, Sub: 400W, Ratio: ~0.698 for exactly +3.4dB sub bias\n")

for name, target in targets.items():
    best = None
    for gF in range(1, 101):
        gS = round(gF * 0.698)
        if gS < 1: gS = 1
        if gS > 100: gS = 100
        spl, pF, pS, diff = calcSPL(gF, gS)
        err = abs(spl - target)
        if best is None or err < best[0]:
            best = (err, gF, gS, spl, pF, pS, diff)
    
    err, gF, gS, spl, pF, pS, diff = best
    ratio = gS / gF if gF > 0 else 0
    safe = "OK" if pS <= 200 else "OVER!"
    print(f"  {name:10s}: gF={gF:3d}, gS={gS:3d}, ratio={ratio:.3f}, diff=+{diff}dB, SPL={spl:6.1f}dB, pwrF={pF:6.1f}W, pwrS={pS:6.1f}W {safe}")
