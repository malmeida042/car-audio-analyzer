import math

rca = 20 * math.log10(5.0 / 2.0)  # ~7.96 dB

# VW Up! display number to power factor mapping
known = [(0,0),(5,0.03),(10,0.09),(15,0.22),(20,0.50),(25,0.77),(27,0.80),(30,1.00)]

def display_to_power(d):
    if d <= 0: return 0.0001
    if d >= 30: return 1.0
    for i in range(len(known)-1):
        d0, p0 = known[i]
        d1, p1 = known[i+1]
        if d0 <= d <= d1:
            return max(0.0001, p0 + (p1-p0) * (d-d0) / (d1-d0))
    return 1.0

def calc_spl(gF, gS, pf):
    pwrF = 132 * (gF/100)**2
    pwrS = 400 * (gS/100)**2
    if pf < 0.001:
        return 0, 0, 0, 0, 0
    splF = 93 + 10*math.log10(max(0.001, pwrF * pf)) + rca
    splS = 87 + 10*math.log10(max(0.001, pwrS * pf)) + rca
    splFB = splF + 3  # two speakers
    splSC = splS + 8  # cabin boost
    splSys = 10*math.log10(10**(splFB/10) + 10**(splSC/10))
    return splFB, splSC, splSys, pwrF*pf, pwrS*pf

profiles = [
    ("V3 Atual (78/65)", 78, 65),
    ("Versatil (40/30)", 40, 30),
    ("Conforto (30/20)", 30, 20),
    ("Ultra-Low (20/15)", 20, 15),
]

displays = [5, 8, 10, 12, 15, 18, 20, 22, 25, 27, 30]

for name, gF, gS in profiles:
    print(f"\n{'='*60}")
    print(f"  {name}  |  pwrF_max={132*(gF/100)**2:.1f}W  pwrS_max={400*(gS/100)**2:.1f}W")
    print(f"{'='*60}")
    print(f"{'Visor':>5} | {'Pot%':>5} | {'SPL Fr':>7} | {'SPL Sub':>7} | {'SPL Sys':>7} | {'W Fr':>5} | {'W Sub':>5} | Sensacao")
    print("-"*85)
    for d in displays:
        pf = display_to_power(d)
        sFB, sSC, sSys, wF, wS = calc_spl(gF, gS, pf)
        # Describe sensation
        if sSys < 80: s = "Silencioso"
        elif sSys < 90: s = "Fundo musical"
        elif sSys < 100: s = "Volume moderado"
        elif sSys < 105: s = "Confortavel"
        elif sSys < 110: s = "Volume de estrada"
        elif sSys < 115: s = "Empolgado"
        elif sSys < 118: s = "Alto, envolvente"
        elif sSys < 121: s = "Muito alto"
        else: s = "MAXIMO / Cuidado"
        print(f"{d:>5} | {pf*100:>4.0f}% | {sFB:>6.1f} | {sSC:>6.1f} | {sSys:>6.1f} | {wF:>4.1f} | {wS:>4.1f} | {s}")

print("\n\nNOTA: A faixa dinamica do radio (visor 5 a 27) e de ~15 dB.")
print("Isso significa que a diferenca de SPL entre volume minimo util e maximo limpo")
print("e de apenas ~15 dB, independente do ganho do amplificador.")
print(f"RCA 5V boost: +{rca:.1f} dB")
