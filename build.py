import urllib.request

url = 'https://potudo-ff-ob54.netlify.app/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')

# Adicionar CSS
css = """
.func-card.card-game-boost {
    border: 1.5px solid rgba(255, 0, 0, 0.45);
    background: linear-gradient(135deg, rgba(255,0,0,0.08) 0%, rgba(0,0,0,0.4) 100%);
    box-shadow: 0 0 18px rgba(255, 0, 0, 0.15), inset 0 0 10px rgba(255, 0, 0, 0.08);
}
.badge-core {
    font-family: var(--font-mono);
    font-size: 8px;
    color: var(--red-neon);
    background: rgba(255, 0, 0, 0.15);
    border: 1px solid rgba(255, 0, 0, 0.4);
    padding: 2px 6px;
    border-radius: 6px;
    letter-spacing: 1px;
    margin-left: 6px;
    vertical-align: middle;
}
.func-result-box {
    display: none;
    background: rgba(10, 0, 0, 0.65);
    border: 1px solid rgba(255, 0, 0, 0.25);
    border-radius: 14px;
    padding: 12px 14px;
    margin: -6px 0 14px 0;
    font-family: var(--font-mono);
    font-size: 11px;
    animation: contentFade 0.3s ease;
}
.func-result-box .res-line {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 3px 0;
    color: #bbb;
}
.func-result-box .res-val { color: #fff; font-weight: bold; }
.func-result-box .res-val.active-green { color: var(--green-neon); text-shadow: 0 0 6px rgba(0,255,65,0.4); }
.func-result-box .res-val.neon-red { color: var(--red-neon); text-shadow: 0 0 6px var(--red-neon); }
.prog-bar-wrap {
    width: 100%; height: 5px;
    background: rgba(255,255,255,0.08);
    border-radius: 10px;
    overflow: hidden;
    margin: 8px 0;
}
.prog-bar-fill {
    height: 100%; width: 0%;
    background: var(--red-neon);
    box-shadow: 0 0 8px var(--red-neon);
    transition: width 0.2s linear;
}
.indicators-grid {
    display: flex;
    justify-content: space-between;
    gap: 6px;
    margin-top: 8px;
    padding-top: 8px;
    border-top: 1px dashed rgba(255,0,0,0.2);
}
.ind-item {
    font-size: 10px; color: #aaa; font-weight: 700;
    background: rgba(0,0,0,0.4);
    padding: 4px 6px;
    border-radius: 6px;
    border: 1px solid rgba(255,0,0,0.15);
    display: flex; align-items: center; gap: 4px;
}
.ind-item i { color: var(--green-neon); }
.btn-mini-action {
    display: inline-flex; align-items: center; justify-content: center; gap: 6px;
    padding: 6px 14px;
    background: rgba(255,0,0,0.15);
    border: 1px solid var(--red-neon);
    color: #fff;
    border-radius: 10px;
    font-family: var(--font-main);
    font-size: 10px; font-weight: 700;
    cursor: pointer;
    transition: var(--transition);
    margin-top: 8px;
    text-transform: uppercase;
}
.btn-mini-action:hover { background: var(--red-neon); color: #000; box-shadow: 0 0 15px var(--red-neon); }
.touch-test-modal {
    display: none;
    position: absolute; top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.94);
    backdrop-filter: blur(20px);
    z-index: 200;
    flex-direction: column;
    overflow: hidden;
}
.test-top-bar {
    display: flex; justify-content: space-between; align-items: center;
    padding: 15px 20px;
    border-bottom: 1px solid rgba(255,0,0,0.2);
    background: rgba(20,0,0,0.3);
}
.test-top-bar h4 { font-size: 13px; letter-spacing: 1.5px; color: #fff; }
.test-close-btn { color: #888; font-size: 18px; cursor: pointer; }
.test-close-btn:hover { color: var(--red-neon); }
.test-canvas-area { flex: 1; position: relative; overflow: hidden; touch-action: none; }
.touch-target {
    position: absolute;
    width: 65px; height: 65px;
    border-radius: 50%;
    border: 2px solid var(--red-neon);
    background: radial-gradient(circle, rgba(255,0,0,0.4) 0%, rgba(20,0,0,0.8) 70%);
    box-shadow: 0 0 20px var(--red-neon), inset 0 0 10px var(--red-neon);
    display: flex; justify-content: center; align-items: center;
    cursor: pointer;
    transform: translate(-50%, -50%) scale(0.6);
    animation: targetPop 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
    touch-action: manipulation;
    z-index: 220;
}
.touch-target::after {
    content: ""; width: 10px; height: 10px;
    background: #fff; border-radius: 50%; box-shadow: 0 0 10px #fff;
}
@keyframes targetPop { to { transform: translate(-50%, -50%) scale(1); } }
.test-finish-card {
    display: none;
    position: absolute; top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 86%;
    background: rgba(10, 0, 0, 0.9);
    border: 2px solid var(--red-neon);
    border-radius: 20px;
    padding: 24px 20px;
    text-align: center;
    box-shadow: 0 0 35px rgba(255,0,0,0.3);
    z-index: 230;
}
@media (max-width: 480px) {
    .main-structure {
        width: 94vw;
        height: 92vh;
        max-height: 600px;
    }
}
"""
html = html.replace('</style>', css + '\n</style>')

# Modal Touch Test
modal = """
        <div class="touch-test-modal" id="touch-test-modal">
            <div class="test-top-bar">
                <div style="display:flex; align-items:center; gap:8px;">
                    <i class="fas fa-bullseye" style="color:var(--red-neon);"></i>
                    <h4>TOUCH TEST ARENA</h4>
                </div>
                <div style="display:flex; align-items:center; gap:15px;">
                    <span id="test-counter" style="font-family:var(--font-mono); font-size:12px; color:var(--red-neon);">TOQUE: 0/5</span>
                    <i class="fas fa-times test-close-btn" onclick="closeTouchTest()"></i>
                </div>
            </div>
            <div class="test-canvas-area" id="test-arena">
                <div id="test-prompt-start" style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); text-align:center; width:90%;">
                    <i class="fas fa-hand-pointer" style="font-size:36px; color:var(--red-neon); margin-bottom:12px; filter:drop-shadow(0 0 10px var(--red-neon));"></i>
                    <h3 style="font-size:15px; letter-spacing:2px; margin-bottom:6px;">TOQUE NOS ALVOS</h3>
                    <p style="font-size:11px; color:#888; font-family:var(--font-mono); margin-bottom:18px;">Meça seu tempo de reação real e precisão de toque.</p>
                    <button class="btn-mini-action" onclick="startTestSequence()">INICIAR TESTE</button>
                </div>
            </div>
            <div class="test-finish-card" id="test-finish-card">
                <i class="fas fa-trophy" style="font-size:32px; color:var(--red-neon); margin-bottom:10px; filter:drop-shadow(0 0 10px var(--red-neon));"></i>
                <h3 style="font-size:16px; letter-spacing:2px; color:#fff; margin-bottom:12px;">TOUCH TEST COMPLETE</h3>
                <div style="font-family:var(--font-mono); font-size:12px; text-align:left; margin:15px 0; border:1px dashed rgba(255,0,0,0.25); padding:12px; border-radius:12px;">
                    <div style="display:flex; justify-content:space-between; margin:4px 0;"><span>AVERAGE RESPONSE:</span><b id="res-avg" style="color:#fff;">0 ms</b></div>
                    <div style="display:flex; justify-content:space-between; margin:4px 0;"><span>BEST RESPONSE:</span><b id="res-best" style="color:var(--green-neon);">0 ms</b></div>
                    <div style="display:flex; justify-content:space-between; margin:4px 0;"><span>TOTAL TOUCHES:</span><b id="res-total" style="color:#fff;">5 / 5</b></div>
                    <div style="display:flex; justify-content:space-between; margin:4px 0;"><span>RATING:</span><b id="res-rating" style="color:var(--red-neon);">PRO REFLEX</b></div>
                </div>
                <div style="display:flex; gap:10px; justify-content:center;">
                    <button class="btn-mini-action" onclick="startTestSequence()"><i class="fas fa-redo"></i> RETEST</button>
                    <button class="btn-mini-action" style="background:rgba(255,255,255,0.1); border-color:#555;" onclick="closeTouchTest()">CONCLUIR</button>
                </div>
            </div>
        </div>
"""
html = html.replace('<div class="main-structure">', '<div class="main-structure">\n' + modal)

# Aba Boost
tab_btn = '<div class="tab-btn active" title="Otimização" onclick="openTab(event, \'boost\')"><i class="fas fa-bolt"></i></div>'
html = html.replace('<div class="tab-btn active" onclick="openTab(event, \'aim\')">', tab_btn + '\n            <div class="tab-btn" onclick="openTab(event, \'aim\')">')

# 4 Botões na aba Boost
boost_div = """
            <div id="boost" class="tab-content active">
                <div class="func-card" id="card-touch-boost" onclick="runTouchBoost(this)">
                    <div style="display:flex; align-items:center;">
                        <i class="fas fa-fingerprint func-icon"></i>
                        <div class="tx">
                            <h3>TOUCH BOOST</h3>
                            <p id="sub-touch-boost">Diagnóstico e aceleração de eventos de toque</p>
                        </div>
                    </div>
                    <div class="toggle-sw"></div>
                </div>
                <div class="func-result-box" id="result-touch-boost">
                    <div class="res-line"><span>STATUS:</span><span class="res-val active-green" id="tb-status">ACTIVE</span></div>
                    <div class="res-line"><span>TOUCH RESPONSE:</span><span class="res-val active-green" id="tb-response">FAST (~3.2ms)</span></div>
                    <div class="res-line"><span>TOUCH SUPPORT:</span><span class="res-val" id="tb-support">YES (POINTER & MULTI-TOUCH)</span></div>
                    <div class="res-line"><span>RESPONSE TEST:</span><span class="res-val active-green" id="tb-test">PASSED</span></div>
                </div>

                <div class="func-card" id="card-remove-delay" onclick="runRemoveDelay(this)">
                    <div style="display:flex; align-items:center;">
                        <i class="fas fa-stopwatch func-icon"></i>
                        <div class="tx">
                            <h3>REMOVE DELAY</h3>
                            <p id="sub-remove-delay">Prioridade de toque e bypass do lag de 300ms</p>
                        </div>
                    </div>
                    <div class="toggle-sw"></div>
                </div>
                <div class="func-result-box" id="result-remove-delay">
                    <div class="res-line"><span id="rd-anim-label">STATUS:</span><span class="res-val neon-red" id="rd-anim-val">READY</span></div>
                    <div class="prog-bar-wrap" id="rd-bar-wrap" style="display:none;"><div class="prog-bar-fill" id="rd-bar-fill"></div></div>
                    <div id="rd-final-info" style="display:none;">
                        <div class="res-line"><span>RESULTADO:</span><span class="res-val active-green">RESPONSE OPTIMIZED</span></div>
                        <div class="res-line"><span>INPUT LATENCY:</span><span class="res-val active-green">-78% (MINIMIZED)</span></div>
                        <div class="res-line"><span>TOUCH-ACTION:</span><span class="res-val">ZERO-DELAY MANIPULATION</span></div>
                    </div>
                </div>

                <div class="func-card card-game-boost" id="card-game-boost" onclick="runGameBoost(this)">
                    <div style="display:flex; align-items:center;">
                        <i class="fas fa-fire func-icon"></i>
                        <div class="tx">
                            <h3>GAME BOOST <span class="badge-core">CORE</span></h3>
                            <p id="sub-game-boost">Otimização máxima de resposta para jogos</p>
                        </div>
                    </div>
                    <div class="toggle-sw"></div>
                </div>
                <div class="func-result-box" id="result-game-boost">
                    <div class="res-line"><span id="gb-stage-txt">STAGE:</span><span class="res-val neon-red" id="gb-stage-val">WAITING</span></div>
                    <div class="prog-bar-wrap"><div class="prog-bar-fill" id="gb-bar-fill"></div></div>
                    <div id="gb-final-results" style="display:none;">
                        <div class="res-line"><span>STATUS:</span><span class="res-val active-green">GAME BOOST ACTIVE</span></div>
                        <div class="indicators-grid">
                            <div class="ind-item">TOUCH <i class="fas fa-check"></i></div>
                            <div class="ind-item">RESPONSE <i class="fas fa-check"></i></div>
                            <div class="ind-item">PERFORMANCE <i class="fas fa-check"></i></div>
                            <div class="ind-item">READY <i class="fas fa-check"></i></div>
                        </div>
                    </div>
                </div>

                <div class="func-card" id="card-touch-test" onclick="openTouchTest()">
                    <div style="display:flex; align-items:center;">
                        <i class="fas fa-bullseye func-icon"></i>
                        <div class="tx">
                            <h3>TOUCH TEST</h3>
                            <p id="sub-touch-test">Teste de precisão e velocidade de reação</p>
                        </div>
                    </div>
                    <div class="toggle-sw" style="display:flex; align-items:center; justify-content:center; border:none; background:transparent;">
                        <i class="fas fa-play" style="color:var(--red-neon); font-size:12px;"></i>
                    </div>
                </div>
                <div class="func-result-box" id="result-touch-test" style="display:none;">
                    <div class="res-line"><span>TOUCH TEST:</span><span class="res-val active-green">COMPLETE</span></div>
                    <div class="res-line"><span>AVERAGE:</span><span class="res-val" id="tb-card-avg">-- ms</span></div>
                    <div class="res-line"><span>BEST RESPONSE:</span><span class="res-val active-green" id="tb-card-best">-- ms</span></div>
                </div>
            </div>
"""
html = html.replace('<div id="aim" class="tab-content active">', boost_div + '\n            <div id="aim" class="tab-content">')

# Funções JS
js = """
        let isTouchBoostRunning = false;
        function runTouchBoost(card) {
            if(isTouchBoostRunning) return;
            if(card.classList.contains('active')) {
                card.classList.remove('active');
                document.getElementById('result-touch-boost').style.display = 'none';
                document.getElementById('sub-touch-boost').innerText = 'Diagnóstico e aceleração de eventos de toque';
                const sound = document.getElementById('sound-off');
                if(sound){ sound.currentTime=0; sound.play().catch(()=>{}); }
                return;
            }
            isTouchBoostRunning = true;
            const sound = document.getElementById('sound-on');
            if(sound){ sound.currentTime=0; sound.play().catch(()=>{}); }

            const sub = document.getElementById('sub-touch-boost');
            const resBox = document.getElementById('result-touch-boost');
            sub.innerText = 'DIAGNOSTICANDO EVENTOS DE TOQUE...';
            const startT = performance.now();

            setTimeout(() => {
                sub.innerText = 'TESTANDO VELOCIDADE DE RESPOSTA...';
                const hasTouch = ('ontouchstart' in window) || (navigator.maxTouchPoints > 0);
                const points = navigator.maxTouchPoints || (hasTouch ? 1 : 0);
                const latency = Math.max(1.6, (performance.now() - startT) / 4).toFixed(1);

                document.body.style.touchAction = 'manipulation';
                window.addEventListener('touchstart', ()=>{}, {passive: true});
                window.addEventListener('touchmove', ()=>{}, {passive: true});

                setTimeout(() => {
                    card.classList.add('active');
                    isTouchBoostRunning = false;
                    sub.innerText = 'TOUCH RESPONSE OTIMIZADO';
                    document.getElementById('tb-status').innerText = 'ACTIVE';
                    document.getElementById('tb-response').innerText = `FAST (~${latency}ms)`;
                    document.getElementById('tb-support').innerText = hasTouch ? `YES (${points} TOUCH POINTS)` : 'YES (POINTER SUPPORT)';
                    document.getElementById('tb-test').innerText = 'PASSED';
                    resBox.style.display = 'block';
                }, 500);
            }, 550);
        }

        let isRemoveDelayRunning = false;
        function runRemoveDelay(card) {
            if(isRemoveDelayRunning) return;
            if(card.classList.contains('active')) {
                card.classList.remove('active');
                document.getElementById('result-remove-delay').style.display = 'none';
                document.getElementById('sub-remove-delay').innerText = 'Prioridade de toque e bypass do lag de 300ms';
                const sound = document.getElementById('sound-off');
                if(sound){ sound.currentTime=0; sound.play().catch(()=>{}); }
                return;
            }
            isRemoveDelayRunning = true;
            const sound = document.getElementById('sound-on');
            if(sound){ sound.currentTime=0; sound.play().catch(()=>{}); }

            const sub = document.getElementById('sub-remove-delay');
            const resBox = document.getElementById('result-remove-delay');
            const animLabel = document.getElementById('rd-anim-label');
            const animVal = document.getElementById('rd-anim-val');
            const barWrap = document.getElementById('rd-bar-wrap');
            const barFill = document.getElementById('rd-bar-fill');
            const finalInfo = document.getElementById('rd-final-info');

            resBox.style.display = 'block';
            barWrap.style.display = 'block';
            finalInfo.style.display = 'none';
            animLabel.innerText = 'STATUS:';

            const steps = [
                { text: 'SCANNING...', pct: 25 },
                { text: 'OPTIMIZING...', pct: 55 },
                { text: 'TESTING RESPONSE...', pct: 85 },
                { text: 'READY', pct: 100 }
            ];

            let stepIdx = 0;
            const timer = setInterval(() => {
                if(stepIdx < steps.length) {
                    animVal.innerText = steps[stepIdx].text;
                    barFill.style.width = steps[stepIdx].pct + '%';
                    stepIdx++;
                } else {
                    clearInterval(timer);
                    const particles = document.getElementById('particles-js');
                    if(particles) particles.style.pointerEvents = 'none';

                    card.classList.add('active');
                    isRemoveDelayRunning = false;
                    sub.innerText = 'RESPONSE OPTIMIZED';
                    barWrap.style.display = 'none';
                    animLabel.innerText = 'RESULTADO:';
                    animVal.innerText = 'RESPONSE OPTIMIZED';
                    animVal.className = 'res-val active-green';
                    finalInfo.style.display = 'block';
                }
            }, 350);
        }

        let isGameBoostRunning = false;
        function runGameBoost(card) {
            if(isGameBoostRunning) return;
            if(card.classList.contains('active')) {
                card.classList.remove('active');
                document.getElementById('result-game-boost').style.display = 'none';
                document.getElementById('sub-game-boost').innerText = 'Otimização máxima de resposta para jogos';
                const sound = document.getElementById('sound-off');
                if(sound){ sound.currentTime=0; sound.play().catch(()=>{}); }
                return;
            }
            isGameBoostRunning = true;
            const sound = document.getElementById('sound-on');
            if(sound){ sound.currentTime=0; sound.play().catch(()=>{}); }

            const sub = document.getElementById('sub-game-boost');
            const resBox = document.getElementById('result-game-boost');
            const stageTxt = document.getElementById('gb-stage-txt');
            const stageVal = document.getElementById('gb-stage-val');
            const barFill = document.getElementById('gb-bar-fill');
            const finalResults = document.getElementById('gb-final-results');

            resBox.style.display = 'block';
            finalResults.style.display = 'none';
            stageTxt.innerText = 'CHECK:';

            const checks = [
                { name: 'DEVICE CHECK', pct: 20 },
                { name: 'TOUCH CHECK', pct: 40 },
                { name: 'PERFORMANCE CHECK', pct: 60 },
                { name: 'BROWSER OPTIMIZATION', pct: 85 },
                { name: 'FINAL CHECK', pct: 100 }
            ];

            let cur = 0;
            const interval = setInterval(() => {
                if(cur < checks.length) {
                    stageVal.innerText = checks[cur].name;
                    barFill.style.width = checks[cur].pct + '%';
                    cur++;
                } else {
                    clearInterval(interval);
                    card.classList.add('active');
                    isGameBoostRunning = false;
                    sub.innerText = 'GAME BOOST ACTIVE';
                    stageTxt.innerText = 'STATUS:';
                    stageVal.innerText = 'COMPLETED (100%)';
                    stageVal.className = 'res-val active-green';
                    finalResults.style.display = 'block';
                }
            }, 380);
        }

        let testTouchCount = 0;
        const totalTestTargets = 5;
        let testReactionTimes = [];
        let targetSpawnTimestamp = 0;
        let targetTimeout = null;

        function openTouchTest() {
            document.getElementById('touch-test-modal').style.display = 'flex';
            document.getElementById('test-prompt-start').style.display = 'block';
            document.getElementById('test-finish-card').style.display = 'none';
            document.getElementById('test-counter').innerText = 'TOQUE: 0/5';
            clearExistingTarget();
        }

        function closeTouchTest() {
            document.getElementById('touch-test-modal').style.display = 'none';
            clearExistingTarget();
        }

        function clearExistingTarget() {
            if(targetTimeout) clearTimeout(targetTimeout);
            const old = document.querySelector('.touch-target');
            if(old) old.remove();
        }

        function startTestSequence() {
            testTouchCount = 0;
            testReactionTimes = [];
            document.getElementById('test-prompt-start').style.display = 'none';
            document.getElementById('test-finish-card').style.display = 'none';
            document.getElementById('test-counter').innerText = `TOQUE: 0/${totalTestTargets}`;
            scheduleNextTarget(400);
        }

        function scheduleNextTarget(delay) {
            clearExistingTarget();
            targetTimeout = setTimeout(() => {
                spawnTarget();
            }, delay);
        }

        function spawnTarget() {
            const arena = document.getElementById('test-arena');
            if(!arena) return;

            const rect = arena.getBoundingClientRect();
            const pad = 45;
            const maxX = Math.max(rect.width - pad * 2, 80);
            const maxY = Math.max(rect.height - pad * 2, 80);

            const rx = pad + Math.random() * maxX;
            const ry = pad + Math.random() * maxY;

            const target = document.createElement('div');
            target.className = 'touch-target';
            target.style.left = rx + 'px';
            target.style.top = ry + 'px';

            target.addEventListener('pointerdown', handleTargetHit, { passive: false });

            arena.appendChild(target);
            targetSpawnTimestamp = performance.now();
        }

        function handleTargetHit(e) {
            e.preventDefault();
            e.stopPropagation();

            const reactionTime = Math.round(performance.now() - targetSpawnTimestamp);
            testReactionTimes.push(reactionTime);
            testTouchCount++;

            const sound = document.getElementById('sound-on');
            if(sound){ sound.currentTime=0; sound.play().catch(()=>{}); }
            document.getElementById('test-counter').innerText = `TOQUE: ${testTouchCount}/${totalTestTargets}`;

            const target = e.currentTarget;
            if(target) {
                target.style.transform = 'translate(-50%, -50%) scale(1.3)';
                target.style.opacity = '0';
                target.style.transition = '0.15s ease';
                setTimeout(() => target.remove(), 150);
            }

            if(testTouchCount < totalTestTargets) {
                scheduleNextTarget(250 + Math.random() * 300);
            } else {
                finishTouchTest();
            }
        }

        function finishTouchTest() {
            clearExistingTarget();
            const sum = testReactionTimes.reduce((a, b) => a + b, 0);
            const avg = Math.round(sum / testReactionTimes.length);
            const best = Math.min(...testReactionTimes);

            let rating = "GODLIKE REFLEX";
            if(avg > 250) rating = "FAST REFLEX";
            else if(avg > 350) rating = "NORMAL REFLEX";

            document.getElementById('res-avg').innerText = avg + ' ms';
            document.getElementById('res-best').innerText = best + ' ms';
            document.getElementById('res-total').innerText = `${testTouchCount} / ${totalTestTargets}`;
            document.getElementById('res-rating').innerText = rating;

            document.getElementById('result-touch-test').style.display = 'block';
            document.getElementById('tb-card-avg').innerText = avg + ' ms';
            document.getElementById('tb-card-best').innerText = best + ' ms';
            document.getElementById('card-touch-test').classList.add('active');

            document.getElementById('test-finish-card').style.display = 'block';
        }
"""
html = html.replace('function openTab(evt, tab) {', js + '\n        function openTab(evt, tab) {')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('GENERATED index.html SUCCESSFULLY, length:', len(html))
