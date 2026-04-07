import codecs

freqLabels = ['20', '40', '80', '160', '300', '600', '1k', '2.5k', '5k', '10k', '20k']
speakers = [
    {'id': 'harman', 'name': 'Curva Alvo Harman (Automotivo)', 'tags': ['Target Reference', 'Referência Master'], 'color': '#8b5cf6', 'data': [8.0, 9.0, 6.0, 2.0, 0, 0, 0, -1.0, -2.0, -4.0, -6.0], 'desc': 'A Referência de Ouro: Resultado de pesquisas massivas da Harman International para reproduzir um som "natural e prazeroso" no ambiente desafiador do carro. Possui o icônico Bass Shelf (prateleira de graves) com elevação de +6dB a +8dB nos sub-graves para vencer o ruído de rodagem e trazer impacto (peso). Os médios são predominantemente planos (flat) para manter a clareza e fidelidade das vozes, enquanto os agudos iniciam um leve declínio a partir dos 4kHz.'},
    {'id': 'monitor-audio', 'name': 'Monitor Audio Bronze (Sua Casa)', 'tags': ['Punchy Bass', 'Médios Abertos', 'Agudos Brilhantes'], 'color': '#f59e0b', 'data': [5.0, 7.0, 6.0, 2.0, 0.5, -0.5, 0, 1.0, 2.0, 4.0, 3.0], 'desc': 'Seu referencial em casa. A linha de torres da Monitor Audio é conhecida pela enorme "mordida" e vivacidade. O som não é morto; ele tem uma pegada rítmica forte nos médio-graves (punch). Os agudos do tweeter entregam um brilho e uma extensão de ar muito bem definidos.'},
    {'id': 'bw-801d4', 'name': 'Bowers & Wilkins 801 D4', 'tags': ['Palco Imersivo', 'Agudos Diamante', 'V-Shape Suave'], 'color': '#3b82f6', 'data': [4.0, 6.0, 4.0, 1.0, 0, 0, 0, -2.0, 1.0, 4.0, 5.0], 'desc': 'A lenda dos estúdios Abbey Road. A personalidade B&W traz o famoso "BBC dip" reduzindo levemente as frequências de presença (2k-3k) para aumentar a profundidade de palco e afastar um som "gritante".'},
    {'id': 'focal-utopia', 'name': 'Focal Grande Utopia EM', 'tags': ['Dinâmica Absurda', 'Neutro', 'Berílio'], 'color': '#ec4899', 'data': [6.0, 6.0, 5.0, 1.0, 0, 0.5, 0.5, 1.0, 1.5, 2.0, 2.5], 'desc': 'O pináculo do áudio francês. A Utopia é caracterizada por dinâmica e naturalidade extrema. Agudos extensos e sem distorção (tweeter berílio). Médios expressivos mas neutros, e grave avassalador que não ofusca a voz.'},
    {'id': 'wilson-sasha', 'name': 'Wilson Audio Sasha DAW', 'tags': ['Peso Tonal', 'Musicalidade', 'Impacto Físico'], 'color': '#10b981', 'data': [6.0, 7.0, 6.0, 2.0, 0.5, -0.5, -0.5, -1.0, 1.0, 2.5, 2.0], 'desc': 'Caixas com alma rock & roll e excelência orquestral. Conhecidas pelo seu grave monumental e visceral. A região média é riquíssima tonalmente. Excelente para buscar energia e impacto sonoro na resposta de caixa.'},
    {'id': 'devialet-phantom', 'name': 'Devialet Phantom I 108 dB', 'tags': ['Sub-Graves Gigantes', 'DSP Tuned', 'Absurdo'], 'color': '#d946ef', 'data': [12.0, 8.0, 4.0, 1.0, 0, 0, 0, 1.0, 2.0, 3.0, 4.0], 'desc': 'Agressividade tecnológica extrema. Estas caixas usam DSP para forçar sub-graves surreais até 14Hz. Forma um V-Shape com agudos pontudos que projetam toda a percussão maravilhosamente.'},
    {'id': 'adam-s-series', 'name': 'Adam Audio S3V', 'tags': ['Analítico', 'Ribbon Tweeter', 'Cirúrgico'], 'color': '#fbbf24', 'data': [2.0, 4.0, 2.0, 0, 0, 0, 0, 0.5, 1.0, 3.0, 4.0], 'desc': 'O cérebro das mixagens. O som é transparente, neutro no centro e incrivelmente rápido e aveludado nos agudos extremos devido ao tweeter de fita. Graves secos.'},
    {'id': 'sonus-faber', 'name': 'Sonus Faber Aida', 'tags': ['Som Italiano', 'Lush Mids', 'Vintage Warmth'], 'color': '#38bdf8', 'data': [4.0, 6.0, 5.0, 3.0, 2.0, 1.0, 0, -1.0, -2.0, -3.0, -4.0], 'desc': 'O som romântico. Zero fadiga auditiva! Grave super envolvente, médio grave que confere um calor vintage maravilhoso aos vocais, e um roll-off macio dos agudos.'},
    {'id': 'dynaudio-conf', 'name': 'Dynaudio Confidence 60', 'tags': ['Ultra-Neutro', 'Punch Mágico', 'Sedosa'], 'color': '#84cc16', 'data': [3.0, 5.0, 4.0, 1.5, 0.5, 0, 0, -0.5, 0, 1.0, 1.0], 'desc': 'Equilíbrio excepcional. Vocais incrivelmente realistas, "mid-bass kick" lendário por ser percussivo e agudos doces do tweeter Esotar3. Muito neutra mas nunca chata.'},
    {'id': 'elac-vela', 'name': 'ELAC Concentro / Vela', 'tags': ['Médios Ricos', 'Extensão Alta'], 'color': '#a855f7', 'data': [4.0, 5.0, 3.0, 1.0, 0, 0, 0, 0.5, 2.0, 3.5, 4.0], 'desc': 'Brilho com corpo. Tweeter JET dá enormes respiros na ambiência. Excelente para ouvir um espaço acústico muito vasto. Ótima meta de alta definição audiófila.'},
    {'id': 'sonos-five', 'name': 'Sonos Five', 'tags': ['Room Filling', 'Grave Modelado DSP', 'Fácil'], 'color': '#e879f9', 'data': [7.0, 8.0, 5.0, 1.0, 0, -1.0, 0, 2.0, 3.0, 2.0, 1.0], 'desc': 'Engenharia DSP para preencher ambientes. Gravo engrossado artificialmente para soar muito maior. Os médios recebem um pequeno mergulho para evitar som oco/cavernoso.'},
    {'id': 'polk-legend', 'name': 'Polk Audio Legend L800', 'tags': ['Ataque Frontal', 'Vocal Quente', 'Live'], 'color': '#fb7185', 'data': [6.0, 8.0, 6.0, 2.5, 1.0, 0.5, 0, 1.5, 2.0, 1.0, 0.5], 'desc': 'Vigor de show rock. Graves encorpados e amplos e médios vividamente projetados para frente da caixa. Traz as vozes para junto ao seu painel com muito corpo.'},
    {'id': 'kef-blade', 'name': 'KEF Blade One', 'tags': ['Uni-Q', 'Holográfica', 'Linear'], 'color': '#bae6fd', 'data': [4.0, 5.0, 3.0, 1.0, 0, 0, 0, 0, -0.5, 0, 1.0], 'desc': 'A perfeição linear e focal. Resposta quase plana e assustadoramente fiel. Se busca palco holográfico ao centro do painel com zero desvios tonais excessivos.'},
    {'id': 'klipsch-cornwall', 'name': 'Klipsch Heritage Cornwall', 'tags': ['Cornetas', 'Sound de Show', 'Brutal'], 'color': '#ea580c', 'data': [4.0, 6.0, 8.0, 6.0, 4.0, 3.0, 2.0, 4.0, 5.0, 4.0, 2.0], 'desc': 'Cornetões clássicos que entregam volumes monstruosos com impacto direto estilo PA. Punch estúpido de médio-grave. Excelente se gosta de som pra fora e visceral.'},
    {'id': 'burmester-3d', 'name': 'Burmester High-End', 'tags': ['Luxo Alemão', 'Polida', 'Cintilante'], 'color': '#94a3b8', 'data': [5.0, 6.0, 4.0, 1.0, 0, 0, 0, 1.0, 2.0, 3.5, 5.0], 'desc': 'Áudio polido das supermáquinas europeias. Muito focado no refinamento e polimento textural do som nos hiper agudos e um subgrave discreto mas super definido.'}
]

def make_svg(data, color):
    pts_str = []
    for i, val in enumerate(data):
        x = i * 40
        y = 200 - ((val + 10) * 8)
        pts_str.append(f'{x},{y}')
    pts = ' '.join(pts_str)
    
    fill_pts = f'0,200 {pts} 400,200'
    grid = ''
    for y_val, db in [(200, '-10'), (160, '-5'), (120, '0'), (80, '+5'), (40, '+10')]:
        grid += f'<line x1="{0}" y1="{y_val}" x2="{400}" y2="{y_val}" stroke="rgba(255,255,255,0.1)" stroke-width="1" />'
        grid += f'<text x="5" y="{y_val - 5}" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">{db} dB</text>'
    
    for i, lbl in enumerate(freqLabels):
        x = i * 40
        grid += f'<line x1="{x}" y1="0" x2="{x}" y2="200" stroke="rgba(255,255,255,0.05)" stroke-width="1" />'
        if i % 2 == 0:
            grid += f'<text x="{x + 2}" y="195" fill="rgba(255,255,255,0.4)" font-size="10" font-family="sans-serif">{lbl}</text>'

    return f'''
    <svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" style="width:100%; height:100%; overflow: visible; display:block;">
        <defs>
            <linearGradient id="grad_{color.replace('#','')}" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stop-color="{color}" stop-opacity="0.4"/>
                <stop offset="100%" stop-color="{color}" stop-opacity="0.0"/>
            </linearGradient>
        </defs>
        <rect width="400" height="200" fill="transparent" />
        {grid}
        <polygon points="{fill_pts}" fill="url(#grad_{color.replace('#','')})" />
        <polyline points="{pts}" fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
        ''' + ''.join([f'<circle cx="{i*40}" cy="{200 - ((data[i] + 10) * 8)}" r="3" fill="#1e293b" stroke="{color}" stroke-width="2" />' for i in range(len(data))]) + '''
    </svg>
    '''

html = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Referências de EQ Hi-Fi (Estáticas)</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
    <style>
        :root { --bg-dark: #0f172a; --bg-card: #1e293b; --text-main: #f8fafc; --text-muted: #94a3b8; }
        body { margin: 0; padding: 0; background: var(--bg-dark); color: var(--text-main); font-family: 'Inter', sans-serif; min-height: 100vh; }
        header { text-align: center; padding: 3rem 2rem 2rem; }
        h1 { font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem; color: #fff; }
        .subtitle { font-size: 1.1rem; color: var(--text-muted); max-width: 800px; margin: 0 auto; line-height: 1.6; }
        .container { max-width: 1400px; margin: 0 auto; padding: 2rem; }
        .card { background: var(--bg-card); border-radius: 12px; padding: 2rem; margin-bottom: 2rem; border-top: 4px solid var(--card-color); box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
        .card h3 { font-size: 1.6rem; margin-top: 0; color: #fff; display: flex; align-items: center; justify-content: space-between; }
        .tag { background: rgba(255, 255, 255, 0.1); color: #cbd5e1; font-size: 0.8rem; padding: 0.2rem 0.6rem; border-radius: 12px; margin-right: 0.5rem; display: inline-block; margin-bottom: 0.5rem; }
        .chart-container { width: 100%; height: 280px; margin: 1.5rem 0; background: #0b1120; border-radius: 8px; padding: 20px; box-sizing: border-box; }
        .desc { font-size: 1.05rem; color: #cbd5e1; line-height: 1.6; margin-bottom: 0; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(600px, 1fr)); gap: 2rem; }
        @media (max-width: 768px) { .grid { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <header>
        <h1>Referências Hi-Fi & High-End (Offline)</h1>
        <p class="subtitle">Gráficos gerados nativamente em SVG para carregamento instantâneo e total compatibilidade, sem nenhum Javascript necessário.</p>
    </header>
    <div class="container">
'''

first = speakers[0]
html += f'''
<div class="card" style="--card-color: {first['color']}; border-left: 4px solid {first['color']}; border-top: none;">
    <h3>{first['name']}</h3>
    <div style="margin-bottom:1rem;">{''.join([f'<span class="tag">{t}</span>' for t in first['tags']])}</div>
    <div class="chart-container">{make_svg(first['data'], first['color'])}</div>
    <p class="desc">{first['desc']}</p>
</div>
<div class="grid">
'''

for spk in speakers[1:]:
    html += f'''
    <div class="card" style="--card-color: {spk['color']}; border-top: 4px solid {spk['color']};">
        <h3>{spk['name']}</h3>
        <div style="margin-bottom:1rem;">{''.join([f'<span class="tag">{t}</span>' for t in spk['tags']])}</div>
        <div class="chart-container">{make_svg(spk['data'], spk['color'])}</div>
        <p class="desc">{spk['desc']}</p>
    </div>
    '''

html += "</div></div></body></html>"

with codecs.open('c:\\\\Users\\\\Usuário\\\\Desktop\\\\car-audio-analyzer\\\\referencias para eq do processador do meu carro.html', 'w', 'utf-8') as f:
    f.write(html)
