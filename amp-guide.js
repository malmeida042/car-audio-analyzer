/**
 * Amplifier Gain Visual Guide — V4.1
 * Overlays colored position markers on the real amp photo
 * showing where each gain knob should be set per preset.
 */
(function () {
    'use strict';

    // === KNOB GEOMETRY (% of image dimensions) ===
    // Left knob GAIN CH1-CH2 (Front)
    const KNOB_L = { cx: 24.2, cy: 73.5, r: 6.5, label: 'CH1-CH2' };
    // Right knob GAIN CH3-CH4 (Sub)
    const KNOB_R = { cx: 79.0, cy: 73.5, r: 6.5, label: 'CH3-CH4' };

    // Rotation: MIN at -135° (7 o'clock), MAX at +135° (5 o'clock) = 270° sweep
    const ANGLE_MIN = -135;
    const ANGLE_MAX = 135;

    // Preset colors
    const PRESET_COLORS = {
        max: '#e17055',
        potente: '#6c5ce7',
        media: '#81ecec',
        natural: '#00b894',
        baixo: '#fdcb6e'
    };

    function gainToAngle(gainPercent) {
        return ANGLE_MIN + (gainPercent / 100) * (ANGLE_MAX - ANGLE_MIN);
    }

    function createGuideHTML() {
        return `
        <div class="amp-guide-section" id="ampGuide">
            <h3 style="font-size:12px;font-weight:700;color:var(--accent2);margin-bottom:8px;display:flex;align-items:center;gap:6px">
                <span style="font-size:14px">📸</span> Guia Visual — Posição dos Ganhos no Módulo
            </h3>
            <p style="font-size:10px;color:var(--text2);margin-bottom:8px;line-height:1.5">
                As marcações coloridas indicam a <strong style="color:var(--accent2)">posição exata</strong> de cada potenciômetro para o preset selecionado.
            </p>
            <div class="amp-img-container" id="ampImgContainer">
                <img src="foto controle de ganhos meu amplificador.png" alt="Amplificador SoundDigital 800.4" class="amp-photo" id="ampPhoto">
                <!-- SVG overlay -->
                <svg class="amp-overlay" id="ampOverlay" viewBox="0 0 1000 520" preserveAspectRatio="none">
                    <defs>
                        <filter id="glow">
                            <feGaussianBlur stdDeviation="3" result="blur"/>
                            <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
                        </filter>
                        <filter id="shadow">
                            <feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="#000" flood-opacity="0.8"/>
                        </filter>
                    </defs>
                    <!-- Left knob marker group -->
                    <g id="knobL" filter="url(#glow)">
                        <circle id="knobLRing" cx="242" cy="382" r="55" fill="none" stroke-width="3" stroke-dasharray="4 3" opacity="0.5"/>
                        <line id="knobLNeedle" x1="242" y1="382" x2="242" y2="322" stroke-width="4" stroke-linecap="round"/>
                        <circle id="knobLDot" cx="242" cy="322" r="7" stroke="#000" stroke-width="1.5"/>
                    </g>
                    <!-- Right knob marker group -->
                    <g id="knobR" filter="url(#glow)">
                        <circle id="knobRRing" cx="790" cy="382" r="55" fill="none" stroke-width="3" stroke-dasharray="4 3" opacity="0.5"/>
                        <line id="knobRNeedle" x1="790" y1="382" x2="790" y2="322" stroke-width="4" stroke-linecap="round"/>
                        <circle id="knobRDot" cx="790" cy="322" r="7" stroke="#000" stroke-width="1.5"/>
                    </g>
                    <!-- Labels -->
                    <g id="knobLLabel" filter="url(#shadow)">
                        <rect x="172" y="280" width="140" height="26" rx="6" fill="rgba(0,0,0,0.85)" stroke-width="1"/>
                        <text id="knobLText" x="242" y="298" text-anchor="middle" fill="#fff" font-family="Inter,sans-serif" font-size="14" font-weight="700"></text>
                    </g>
                    <g id="knobRLabel" filter="url(#shadow)">
                        <rect x="720" y="280" width="140" height="26" rx="6" fill="rgba(0,0,0,0.85)" stroke-width="1"/>
                        <text id="knobRText" x="790" y="298" text-anchor="middle" fill="#fff" font-family="Inter,sans-serif" font-size="14" font-weight="700"></text>
                    </g>
                </svg>
            </div>
            <div class="amp-preset-legend" id="ampPresetLegend"></div>
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
            .amp-photo {
                width: 100%; height: auto; display: block;
                opacity: 0.92;
            }
            .amp-overlay {
                position: absolute; top: 0; left: 0; width: 100%; height: 100%;
                pointer-events: none;
            }
            .amp-preset-legend {
                display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px;
                justify-content: center;
            }
            .amp-legend-item {
                display: flex; align-items: center; gap: 4px;
                font-size: 9px; color: var(--text2);
                padding: 3px 8px; border-radius: 6px;
                background: var(--card2); border: 1px solid var(--border);
            }
            .amp-legend-dot {
                width: 8px; height: 8px; border-radius: 50%;
            }
            .amp-legend-item.active {
                border-color: var(--accent);
                background: rgba(108,92,231,0.15);
                color: var(--accent2);
                font-weight: 600;
            }
        `;
        document.head.appendChild(style);
    }

    function updateKnobMarker(side, gainPercent, color) {
        const angle = gainToAngle(gainPercent);
        const prefix = side === 'L' ? 'knobL' : 'knobR';
        const cx = side === 'L' ? 242 : 790;
        const cy = 382;
        const needleLen = 60;

        // Calculate endpoint
        const rad = (angle - 90) * Math.PI / 180; // -90 because SVG 0° = right, we want 0° = up
        const ex = cx + needleLen * Math.cos(rad);
        const ey = cy + needleLen * Math.sin(rad);

        // Update needle
        const needle = document.getElementById(prefix + 'Needle');
        if (needle) {
            needle.setAttribute('x2', ex.toFixed(1));
            needle.setAttribute('y2', ey.toFixed(1));
            needle.setAttribute('stroke', color);
        }
        // Update dot
        const dot = document.getElementById(prefix + 'Dot');
        if (dot) {
            dot.setAttribute('cx', ex.toFixed(1));
            dot.setAttribute('cy', ey.toFixed(1));
            dot.setAttribute('fill', color);
        }
        // Update ring
        const ring = document.getElementById(prefix + 'Ring');
        if (ring) {
            ring.setAttribute('stroke', color);
        }
        // Update label rect stroke
        const labelGroup = document.getElementById(prefix + 'Label');
        if (labelGroup) {
            const rect = labelGroup.querySelector('rect');
            if (rect) rect.setAttribute('stroke', color);
        }
    }

    function updateLabels(gF, gS, color, presetName) {
        const lText = document.getElementById('knobLText');
        const rText = document.getElementById('knobRText');
        if (lText) lText.textContent = `CH1-CH2: ${gF}%`;
        if (rText) rText.textContent = `CH3-CH4: ${gS}%`;
    }

    function updateLegend() {
        const legend = document.getElementById('ampPresetLegend');
        if (!legend || !window.presets) return;
        let html = '';
        for (const [id, p] of Object.entries(window.presets)) {
            const color = PRESET_COLORS[id] || '#a0a0b0';
            const isActive = window.activePreset === id;
            html += `<div class="amp-legend-item${isActive ? ' active' : ''}" onclick="setPreset('${id}')">
                <div class="amp-legend-dot" style="background:${color}"></div>
                ${p.emoji} ${p.gF}/${p.gS}%
            </div>`;
        }
        legend.innerHTML = html;
    }

    // Main update function — called after each updateAll()
    function updateAmpGuide() {
        const gF = parseInt(document.getElementById('gainFront').value) || 0;
        const gS = parseInt(document.getElementById('gainSub').value) || 0;
        const preset = window.activePreset || 'potente';
        const color = PRESET_COLORS[preset] || '#6c5ce7';

        updateKnobMarker('L', gF, color);
        updateKnobMarker('R', gS, color);
        updateLabels(gF, gS, color);
        updateLegend();
    }

    // Inject into the page
    function init() {
        createStyles();

        // Find the gain control card and insert after it
        const allCards = document.querySelectorAll('.card');
        let gainCard = null;
        for (const card of allCards) {
            const h2 = card.querySelector('h2');
            if (h2 && h2.textContent.includes('Controle de Ganho')) {
                gainCard = card;
                break;
            }
        }

        if (gainCard) {
            // Insert the guide HTML inside the gain card, at the bottom
            const guideDiv = document.createElement('div');
            guideDiv.innerHTML = createGuideHTML();
            gainCard.appendChild(guideDiv.firstElementChild);
        }

        // Hook into updateAll to also update our guide
        const origUpdateAll = window.updateAll;
        window.updateAll = function () {
            origUpdateAll.apply(this, arguments);
            updateAmpGuide();
        };

        // Hook into setPreset for immediate update
        const origSetPreset = window.setPreset;
        window.setPreset = function (id) {
            origSetPreset.apply(this, arguments);
            updateAmpGuide();
        };

        // Initial render
        setTimeout(updateAmpGuide, 200);
    }

    // Wait for page load
    if (document.readyState === 'complete') {
        init();
    } else {
        window.addEventListener('load', function () {
            setTimeout(init, 100);
        });
    }
})();
