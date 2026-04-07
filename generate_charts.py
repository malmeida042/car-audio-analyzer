import urllib.parse
import json
import codecs

speakers = [
    {'name': '1. Curva Alvo Harman (Automotivo)', 'color': 'rgb(139, 92, 246)', 'data': [8.0, 9.0, 6.0, 2.0, 0, 0, 0, -1.0, -2.0, -4.0, -6.0], 'desc': 'A Referência de Ouro. O Bass Shelf levanta forte as regiões sub.'},
    {'name': '2. Monitor Audio Bronze (Sua Casa)', 'color': 'rgb(245, 158, 11)', 'data': [5.0, 7.0, 6.0, 2.0, 0.5, -0.5, 0, 1.0, 2.0, 4.0, 3.0], 'desc': 'Caixas com enorme ataque ("punch") e detalhamento.'},
    {'name': '3. Bowers & Wilkins 801 D4', 'color': 'rgb(59, 130, 246)', 'data': [4.0, 6.0, 4.0, 1.0, 0, 0, 0, -2.0, 1.0, 4.0, 5.0], 'desc': 'Imersivo palco de estúdios. Retira um pouco de energia da faixa de presença (2.5k).'},
    {'name': '4. Focal Grande Utopia EM', 'color': 'rgb(236, 72, 153)', 'data': [6.0, 6.0, 5.0, 1.0, 0, 0.5, 0.5, 1.0, 1.5, 2.0, 2.5], 'desc': 'Excelência francesa. Respostas ultra amplas e rápidas sem nunca ofuscar a beleza da voz.'},
    {'name': '5. Wilson Audio Sasha DAW', 'color': 'rgb(16, 185, 129)', 'data': [6.0, 7.0, 6.0, 2.0, 0.5, -0.5, -0.5, -1.5, 1.0, 2.5, 2.0], 'desc': 'Som de peso monumental (o melhor grave real) com vozes grossas muito orgânicas.'},
    {'name': '6. Devialet Phantom I 108 dB', 'color': 'rgb(217, 70, 239)', 'data': [12.0, 8.0, 4.0, 1.0, 0, 0, 0, 1.0, 2.0, 3.0, 4.0], 'desc': 'Foco brutal no V-Shape com sub-grave na casa do além (via DSP) e agudos que marcam pratos.'},
    {'name': '7. Adam Audio S3V', 'color': 'rgb(251, 191, 36)', 'data': [2.0, 4.0, 2.0, 0, 0, 0, 0, 0.5, 1.0, 3.0, 4.0], 'desc': 'A referência analítica de estúdio. Sem graves babando, som puramente flat na casa da voz.'},
    {'name': '8. Sonus Faber Aida', 'color': 'rgb(56, 189, 248)', 'data': [4.0, 6.0, 5.0, 3.0, 2.0, 1.0, 0, -1.0, -2.0, -3.0, -4.0], 'desc': 'Romântica. Zero fadiga e médios ricos (homens heróicos) perfeitos para dirigir horas.'},
    {'name': '9. Dynaudio Confidence 60', 'color': 'rgb(132, 204, 22)', 'data': [3.0, 5.0, 4.0, 1.5, 0.5, 0, 0, -0.5, 0, 1.0, 1.0], 'desc': 'Velocidade estúpida. Punch tão forte (bumbo a 80hz) que o som parece que vai ser vomitado no rosto mantendo a graciosidade.'},
    {'name': '10. ELAC Concentro / Vela', 'color': 'rgb(168, 85, 247)', 'data': [4.0, 5.0, 3.0, 1.0, 0, 0, 0, 0.5, 2.0, 3.5, 4.0], 'desc': 'Tweeter estendendo as reverberações. Ótima para se ter muitos echos e suspiros das respirações.'},
    {'name': '11. Sonos Five', 'color': 'rgb(232, 121, 249)', 'data': [7.0, 8.0, 5.0, 1.0, 0, -1.0, 0, 2.0, 3.0, 2.0, 1.0], 'desc': 'Volume Big-Room forjado via DSP para inflar o grave como se houvesse múltiplos subs grandes.'},
    {'name': '12. Polk Audio Legend L800', 'color': 'rgb(251, 113, 133)', 'data': [6.0, 8.0, 6.0, 2.5, 1.0, 0.5, 0, 1.5, 2.0, 1.0, 0.5], 'desc': 'Som projetado. Vozes lançadas e calor de show lotado empurrando muito ar sem finezas exageradas.'},
    {'name': '13. KEF Blade One', 'color': 'rgb(186, 230, 253)', 'data': [4.0, 5.0, 3.0, 1.0, 0, 0, 0, 0, -0.5, 0, 1.0], 'desc': 'Som perfeitamente linear e coaxial. Zero picos extras. Útil para Masterização analítica extrema.'},
    {'name': '14. Klipsch Heritage Cornwall', 'color': 'rgb(234, 88, 12)', 'data': [4.0, 6.0, 8.0, 6.0, 4.0, 3.0, 2.0, 4.0, 5.0, 4.0, 2.0], 'desc': 'Uma buzina na cara! Assinatura bruta PA, agressividade direta nas cordas, elevando as guitarras pro topo da caixa.'},
    {'name': '15. Burmester High-End 3D', 'color': 'rgb(148, 163, 184)', 'data': [5.0, 6.0, 4.0, 1.0, 0, 0, 0, 1.0, 2.0, 3.5, 5.0], 'desc': 'Refinamento hiper analítico. Sub controladíssimo e a extensão dos agudos criam o ambiente de luxo.'}
]

html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Referências de EQ Automotivo - Gráficos Garantidos</title>
    <style>
        body { font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background-color: #f8fafc; color: #1e293b; padding: 20px; text-align: center; }
        .card { background-color: white; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin: 30px auto; padding: 30px; max-width: 800px; text-align: left; border-left: 6px solid; }
        h1 { color: #0f172a; font-size: 2.2rem; }
        h2 { margin-top: 0; color: #334155; }
        p { color: #475569; font-size: 1.1rem; line-height: 1.5; }
        img.chart { width: 100%; max-width: 600px; height: auto; display: block; margin: 20px auto; border-radius: 8px; border: 1px solid #e2e8f0; }
        @media print {
            body { background: white; }
            .card { box-shadow: none; border: 1px solid #ccc; break-inside: avoid; margin-bottom: 20px; }
            img.chart { max-width: 500px; }
        }
    </style>
</head>
<body>
    <h1>Referências de Gráficos de EQ - Visualização Estática Otimizada</h1>
    <p>Use "Imprimir (Ctrl+P)" para salvar perfeitamente como PDF. Zero necessidade de scripts, apenas imagens dinâmicas!</p>
"""

for spk in speakers:
    chart_config = {
        "type": "line",
        "data": {
            "labels": ["20", "40", "80", "160", "300", "600", "1k", "2.5k", "5k", "10k", "20k"],
            "datasets": [{
                "label": "Ganhos em dB",
                "borderColor": spk['color'],
                "backgroundColor": spk['color'].replace('rgb', 'rgba').replace(')', ', 0.1)'),
                "borderWidth": 4,
                "pointRadius": 6,
                "pointBackgroundColor": spk['color'],
                "fill": True,
                "tension": 0.4,
                "data": spk['data']
            }]
        },
        "options": {
            "title": {"display": False},
            "legend": {"display": False},
            "scales": {
                "yAxes": [{
                    "ticks": {"min": -10, "max": 15, "stepSize": 5},
                    "scaleLabel": {"display": True, "labelString": "Gain (dB)"}
                }],
                "xAxes": [{
                    "gridLines": {"color": "rgba(0,0,0,0.05)"}
                }]
            }
        }
    }
    
    encoded_c = urllib.parse.quote(json.dumps(chart_config))
    img_url = f"https://quickchart.io/chart?w=600&h=300&c={encoded_c}&bkg=white"
    
    html_content += f"""
    <div class="card" style="border-left-color: {spk['color']};">
        <h2>{spk['name']}</h2>
        <p>{spk['desc']}</p>
        <img class="chart" src="{img_url}" alt="Gráfico de Curva de {spk['name']}"/>
    </div>
    """

html_content += """
</body>
</html>
"""

# Let's write the file and print ok to confirm it ran successfully
filepath = "C:/Users/Usuário/Desktop/car-audio-analyzer/referencias-eq-graficos-estaticos.html"
with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(html_content)

print(f"File strictly written to {filepath}")
