/**
 * Amplifier Gain Visual Guide — V5 (SD 800.5 EVO 6)
 * 3 knobs: GAIN SUB (left), GAIN CH3-CH4 (center-right), GAIN CH1-CH2 (right)
 */
(function () {
    'use strict';

    // === KNOB GEOMETRY (% of image dimensions) for SD 800.5 ===
    // 3 gain knobs identified from the photo:
    const KNOB_SUB = { cx: 8.5, cy: 76, r: 6, label: 'SUB' };
    const KNOB_34 = { cx: 72, cy: 76, r: 5.5, label: 'CH3-CH4' };
    const KNOB_12 = { cx: 89.5, cy: 76, r: 5.5, label: 'CH1-CH2' };

    // Rotation: MIN at -135deg (7 o'clock), MAX at +135deg (5 o'clock) = 270deg sweep
    const ANGLE_MIN = -135;
    const ANGLE_MAX = 135;

    // Single bright orange color for ALL presets (high visibility)
    const MARKER_COLOR = '#FF6B00';
    const MARKER_GLOW = '#FF8C00';

    function gainToAngle(gainPercent) {
        return ANGLE_MIN + (gainPercent / 100) * (ANGLE_MAX - ANGLE_MIN);
    }

    function createGuideHTML() {
        return `
        <div class="amp-guide-section" id="ampGuide">
            <h3 style="font-size:12px;font-weight:700;color:var(--accent2);margin-bottom:8px;display:flex;align-items:center;gap:6px">
                <span style="font-size:14px">📸</span> Guia Visual — Posicao dos Ganhos no Modulo SD 800.5 EVO 6
            </h3>
            <p style="font-size:10px;color:var(--text2);margin-bottom:8px;line-height:1.5">
                As marcacoes <strong style="color:${MARKER_COLOR}">laranjas</strong> indicam a <strong style="color:var(--accent2)">posicao exata</strong> de cada potenciometro para o preset selecionado.
                <br>Entrada alta (HI INPUT) — sem conversor RCA.
            </p>
            <div class="amp-img-container" id="ampImgContainer">
                <img src="foto controle de ganhos meu amplificador 800.5.png" alt="SoundDigital 800.5 EVO 6" class="amp-photo" id="ampPhoto">
                <svg class="amp-overlay" id="ampOverlay" viewBox="0 0 1000 410" preserveAspectRatio="none">
                    <defs>
                        <filter id="glowOrange">
                            <feGaussianBlur stdDeviation="4" result="blur"/>
                            <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
                        </filter>
                        <filter id="shadowLabel">
                            <feDropShadow dx="0" dy="1" stdDeviation="3" flood-color="#000" flood-opacity="0.9"/>
                        </filter>
                    </defs>
                    <!-- SUB knob (left) -->
                    <g id="knobSUB" filter="url(#glowOrange)">
                        <circle class="knob-ring" cx="85" cy="312" r="48" fill="none" stroke="${MARKER_COLOR}" stroke-width="3" stroke-dasharray="4 3" opacity="0.6"/>
                        <line id="needleSUB" x1="85" y1="312" x2="85" y2="260" stroke="${MARKER_COLOR}" stroke-width="5" stroke-linecap="round"/>
                        <circle id="dotSUB" cx="85" cy="260" r="8" fill="${MARKER_COLOR}" stroke="#000" stroke-width="2"/>
                    </g>
                    <!-- CH3-CH4 knob (center-right) -->
                    <g id="knobCH34" filter="url(#glowOrange)">
                        <circle class="knob-ring" cx="720" cy="312" r="42" fill="none" stroke="${MARKER_COLOR}" stroke-width="3" stroke-dasharray="4 3" opacity="0.6"/>
                        <line id="needleCH34" x1="720" y1="312" x2="720" y2="266" stroke="${MARKER_COLOR}" stroke-width="5" stroke-linecap="round"/>
                        <circle id="dotCH34" cx="720" cy="266" r="8" fill="${MARKER_COLOR}" stroke="#000" stroke-width="2"/>
                    </g>
                    <!-- CH1-CH2 knob (right) -->
                    <g id="knobCH12" filter="url(#glowOrange)">
                        <circle class="knob-ring" cx="895" cy="312" r="42" fill="none" stroke="${MARKER_COLOR}" stroke-width="3" stroke-dasharray="4 3" opacity="0.6"/>
                        <line id="needleCH12" x1="895" y1="312" x2="895" y2="266" stroke="${MARKER_COLOR}" stroke-width="5" stroke-linecap="round"/>
                        <circle id="dotCH12" cx="895" cy="266" r="8" fill="${MARKER_COLOR}" stroke="#000" stroke-width="2"/>
                    </g>
                    <!-- Labels -->
                    <g filter="url(#shadowLabel)">
                        <rect x="20" y="230" width="130" height="28" rx="6" fill="rgba(0,0,0,0.88)" stroke="${MARKER_COLOR}" stroke-width="1.5"/>
                        <text id="labelSUB" x="85" y="249" text-anchor="middle" fill="${MARKER_COLOR}" font-family="Inter,sans-serif" font-size="13" font-weight="700"></text>
                    </g>
                    <g filter="url(#shadowLabel)">
                        <rect x="655" y="230" width="130" height="28" rx="6" fill="rgba(0,0,0,0.88)" stroke="${MARKER_COLOR}" stroke-width="1.5"/>
                        <text id="labelCH34" x="720" y="249" text-anchor="middle" fill="${MARKER_COLOR}" font-family="Inter,sans-serif" font-size="13" font-weight="700"></text>
                    </g>
                    <g filter="url(#shadowLabel)">
                        <rect x="830" y="230" width="130" height="28" rx="6" fill="rgba(0,0,0,0.88)" stroke="${MARKER_COLOR}" stroke-width="1.5"/>
                        <text id="labelCH12" x="895" y="249" text-anchor="middle" fill="${MARKER_COLOR}" font-family="Inter,sans-serif" font-size="13" font-weight="700"></text>
                    </g>
                </svg>
            </div>
            <div class="amp-guide-note" style="font-size:9px;color:var(--text2);margin-top:6px;text-align:center;opacity:0.7">
                SD 800.5 EVO 6 — Entrada Alta (HI INPUT) • Sem conversor RCA • CH1-CH2 = Front • CH3-CH4 = Livre • SUB = Subwoofer
            </div>
        </div>`;
    }

    function createStyles() {
        const style = document.createElement('style');
        style.textContent = `
            .amp-guide-section { margin-top: 12px; }
            .amp-img-container {
                position: relative; border-radius: 10px; overflow: hidden;
                border: 1px solid var(--border); background: #000;
            }
            .amp-photo { width: 100%; height: auto; display: block; opacity: 0.92; }
            .amp-overlay {
                position: absolute; top: 0; left: 0; width: 100%; height: 100%;
                pointer-events: none;
            }
        `;
        document.head.appendChild(style);
    }

    function updateKnob(id, cx, cy, gainPercent, needleLen) {
        const angle = gainToAngle(gainPercent);
        const rad = (angle - 90) * Math.PI / 180;
        const ex = cx + needleLen * Math.cos(rad);
        const ey = cy + needleLen * Math.sin(rad);

        const needle = document.getElementById('needle' + id);
        const dot = document.getElementById('dot' + id);
        if (needle) { needle.setAttribute('x2', ex.toFixed(1)); needle.setAttribute('y2', ey.toFixed(1)); }
        if (dot) { dot.setAttribute('cx', ex.toFixed(1)); dot.setAttribute('cy', ey.toFixed(1)); }
    }

    function updateAmpGuide() {
        const gF = parseInt(document.getElementById('gainFront').value) || 0;
        const gS = parseInt(document.getElementById('gainSub').value) || 0;

        // SD 800.5: CH1-CH2 = Front, SUB = Sub, CH3-CH4 = same as front (or unused)
        updateKnob('SUB', 85, 312, gS, 52);
        updateKnob('CH34', 720, 312, gF, 46);  // CH3-CH4: show same as CH1-CH2 (unused but visual ref)
        updateKnob('CH12', 895, 312, gF, 46);  // CH1-CH2: front

        // Labels
        const lSub = document.getElementById('labelSUB');
        const l34 = document.getElementById('labelCH34');
        const l12 = document.getElementById('labelCH12');
        if (lSub) lSub.textContent = 'SUB: ' + gS + '%';
        if (l34) l34.textContent = 'CH3-4: MIN';
        if (l12) l12.textContent = 'CH1-2: ' + gF + '%';
    }

    function init() {
        createStyles();
        const allCards = document.querySelectorAll('.card');
        let gainCard = null;
        for (const card of allCards) {
            const h2 = card.querySelector('h2');
            if (h2 && h2.textContent.includes('Controle de Ganho')) { gainCard = card; break; }
        }
        if (gainCard) {
            const guideDiv = document.createElement('div');
            guideDiv.innerHTML = createGuideHTML();
            gainCard.appendChild(guideDiv.firstElementChild);
        }

        const origUpdateAll = window.updateAll;
        window.updateAll = function () { origUpdateAll.apply(this, arguments); updateAmpGuide(); };
        const origSetPreset = window.setPreset;
        window.setPreset = function (id) { origSetPreset.apply(this, arguments); updateAmpGuide(); };
        setTimeout(updateAmpGuide, 200);
    }

    if (document.readyState === 'complete') init();
    else window.addEventListener('load', function () { setTimeout(init, 100); });
})();
