# -*- coding: utf-8 -*-
"""Secao 2: Metodos de Produtividade (paginas 8-17)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers import header, footer, page_wrap, checkbox, write_lines, field


def get_pages():
    pages = []

    # P8: Metodo SMART explicacao
    content = '''<h1 class="page-title">Método SMART</h1>
    <p class="page-subtitle">Transforme desejos vagos em metas concretas que seu cérebro TDAH consegue executar.</p>
    <div class="method-grid">
      <div class="method-letter"><span class="letter-highlight">S</span><strong>pecífica</strong><p>O que exatamente quero alcançar? Quanto mais clara, mais fácil de começar.</p></div>
      <div class="method-letter"><span class="letter-highlight">M</span><strong>ensurável</strong><p>Como vou saber que alcancei? Defina um número ou indicador visível.</p></div>
      <div class="method-letter"><span class="letter-highlight">A</span><strong>tingível</strong><p>É realista para mim agora? Considere sua energia e contexto atual.</p></div>
      <div class="method-letter"><span class="letter-highlight">R</span><strong>elevante</strong><p>Por que isso importa pra mim? Conexão emocional mantém a motivação.</p></div>
      <div class="method-letter"><span class="letter-highlight">T</span><strong>emporal</strong><p>Até quando? Prazos criam urgência — e urgência ativa o cérebro TDAH.</p></div>
    </div>
    <div class="tip-box">
      <strong>Dica TDAH:</strong> Metas sem prazo viram "algum dia". E "algum dia" nunca chega. Coloque uma data mesmo que seja aproximada.
    </div>'''
    pages.append(page_wrap(8, content, "Métodos", "8"))

    # P9: SMART worksheet
    content = '''<h1 class="page-title">Minha Meta SMART</h1>
    <div class="smart-worksheet">
      <div class="smart-field">
        <div class="smart-label"><span class="letter-badge">S</span> O que quero alcançar?</div>
        <div class="write-area" style="min-height:45px;"></div>
      </div>
      <div class="smart-field">
        <div class="smart-label"><span class="letter-badge">M</span> Como vou medir meu progresso?</div>
        <div class="write-area" style="min-height:45px;"></div>
      </div>
      <div class="smart-field">
        <div class="smart-label"><span class="letter-badge">A</span> Isso é realista para mim agora? Por quê?</div>
        <div class="write-area" style="min-height:45px;"></div>
      </div>
      <div class="smart-field">
        <div class="smart-label"><span class="letter-badge">R</span> Por que isso é importante pra mim?</div>
        <div class="write-area" style="min-height:45px;"></div>
      </div>
      <div class="smart-field">
        <div class="smart-label"><span class="letter-badge">T</span> Até quando quero alcançar?</div>
        <div class="write-area" style="min-height:45px;"></div>
      </div>
      <div class="smart-field" style="margin-top:12px;">
        <div class="smart-label">Primeiro passo (faça nos próximos 2 minutos):</div>
        ''' + write_lines(2) + '''
      </div>
      <div class="smart-field">
        <div class="smart-label">Minha recompensa ao completar:</div>
        ''' + write_lines(1) + '''
      </div>
    </div>'''
    pages.append(page_wrap(9, content, "Métodos", "9"))

    # P10: Pomodoro explicacao
    content = '''<h1 class="page-title">Técnica Pomodoro</h1>
    <p class="page-subtitle">O timer cria urgência artificial — exatamente o que o cérebro TDAH precisa para entrar em ação.</p>
    <div class="pomodoro-visual">
      <div class="pomo-step">
        <div class="pomo-icon"><svg width="32" height="32" viewBox="0 0 32 32" fill="none"><circle cx="16" cy="17" r="12" stroke="#2563EB" stroke-width="1.5"/><path d="M16 10v7l5 3" stroke="#2563EB" stroke-width="1.5" stroke-linecap="round"/><path d="M13 3h6" stroke="#2563EB" stroke-width="1.5" stroke-linecap="round"/></svg></div>
        <div class="pomo-label">25 min</div>
        <div class="pomo-desc">Foco total em UMA tarefa</div>
      </div>
      <div class="pomo-arrow">→</div>
      <div class="pomo-step">
        <div class="pomo-icon"><svg width="32" height="32" viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="12" stroke="#64748B" stroke-width="1.5"/><path d="M11 16h10M16 11v10" stroke="#64748B" stroke-width="1.5" stroke-linecap="round"/></svg></div>
        <div class="pomo-label">5 min</div>
        <div class="pomo-desc">Pausa curta — levante, beba água</div>
      </div>
      <div class="pomo-arrow">→</div>
      <div class="pomo-step">
        <div class="pomo-icon"><svg width="32" height="32" viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="12" stroke="#2563EB" stroke-width="1.5"/><path d="M10 16h12" stroke="#2563EB" stroke-width="1.5" stroke-linecap="round"/><path d="M12 12l4 4-4 4M16 12l4 4-4 4" stroke="#2563EB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        <div class="pomo-label">Repita 4x</div>
        <div class="pomo-desc">Depois, pausa longa de 15-30 min</div>
      </div>
    </div>
    <div class="variations-box">
      <h3>Variações para TDAH</h3>
      <div class="grid-2" style="gap:12px;margin-top:8px;">
        <div class="var-item"><strong>15/3</strong> — Para dias de baixa energia</div>
        <div class="var-item"><strong>25/5</strong> — O clássico, comece aqui</div>
        <div class="var-item"><strong>45/10</strong> — Quando encontrar o hiperfoco</div>
        <div class="var-item"><strong>50/10</strong> — Para tarefas que exigem imersão</div>
      </div>
    </div>
    <div class="tip-box">
      <strong>Dica:</strong> Não lute contra o hiperfoco. Se ele surgir, aproveite — mas coloque um alarme para não esquecer de comer e beber água.
    </div>'''
    pages.append(page_wrap(10, content, "Métodos", "10"))

    # P11: Pomodoro Tracker
    content = '''<h1 class="page-title">Registro Pomodoro</h1>
    <p class="page-subtitle">Registre suas sessões. Visualizar o progresso ativa a recompensa no cérebro.</p>
    <table class="table">
      <thead>
        <tr><th style="width:30%">Tarefa</th><th style="width:15%">Planejados</th><th style="width:15%">Concluídos</th><th style="width:20%">Duração</th><th style="width:20%">Notas</th></tr>
      </thead>
      <tbody>'''
    for i in range(14):
        content += '''
        <tr><td><div class="write-line" style="height:22px;"></div></td><td><div class="pomo-circles">○○○○</div></td><td><div class="pomo-circles">○○○○</div></td><td><div class="write-line" style="height:22px;"></div></td><td><div class="write-line" style="height:22px;"></div></td></tr>'''
    content += '''
      </tbody>
    </table>
    <div style="margin-top:16px;display:flex;gap:24px;">
      <div><strong>Total de pomodoros hoje:</strong> ______</div>
      <div><strong>Nível de foco (1-10):</strong> ______</div>
    </div>'''
    pages.append(page_wrap(11, content, "Métodos", "11"))

    # P12: Matriz Eisenhower explicacao
    content = '''<h1 class="page-title">Matriz de Eisenhower</h1>
    <p class="page-subtitle">Nem tudo que parece urgente é importante. Separe o que importa do que só faz barulho.</p>
    <div class="eisenhower-explain">
      <div class="grid-2" style="gap:16px;">
        <div class="card card-blue">
          <div class="card-header">1. Urgente + Importante</div>
          <p style="font-size:9pt;color:#475569;">Faça AGORA. Crises, prazos reais, emergências.</p>
          <p style="font-size:8pt;color:#64748B;margin-top:4px;">Ex: consulta médica hoje, conta vencendo</p>
        </div>
        <div class="card" style="border-left:3px solid #059669;">
          <div class="card-header" style="color:#065F46;">2. Importante, Não Urgente</div>
          <p style="font-size:9pt;color:#475569;">PLANEJE. Aqui está o crescimento real.</p>
          <p style="font-size:8pt;color:#64748B;margin-top:4px;">Ex: exercício, estudos, projeto pessoal</p>
        </div>
        <div class="card" style="border-left:3px solid #D97706;">
          <div class="card-header" style="color:#92400E;">3. Urgente, Não Importante</div>
          <p style="font-size:9pt;color:#475569;">DELEGUE ou faça rápido. Interrupções, pedidos dos outros.</p>
          <p style="font-size:8pt;color:#64748B;margin-top:4px;">Ex: responder e-mails, ligações</p>
        </div>
        <div class="card" style="border-left:3px solid #DC2626;">
          <div class="card-header" style="color:#991B1B;">4. Nem Urgente, Nem Importante</div>
          <p style="font-size:9pt;color:#475569;">ELIMINE. Distrações disfarçadas de tarefas.</p>
          <p style="font-size:8pt;color:#64748B;margin-top:4px;">Ex: redes sociais sem propósito, séries por inércia</p>
        </div>
      </div>
    </div>
    <div class="tip-box" style="margin-top:16px;">
      <strong>Dica TDAH:</strong> O quadrante 2 é onde a vida melhora de verdade. Mas o cérebro TDAH é viciado no quadrante 1 (urgência = dopamina). Tente mover pelo menos 1 tarefa do Q2 para "hoje".
    </div>'''
    pages.append(page_wrap(12, content, "Métodos", "12"))

    # P13: Eisenhower Template
    content = '''<h1 class="page-title">Minha Matriz de Eisenhower</h1>
    <p class="page-subtitle">Data: ___/___/___</p>
    <div class="eisenhower-grid">
      <div class="eq eq-1">
        <div class="eq-header">FAZER AGORA</div>
        <div class="eq-label">Urgente + Importante</div>
        ''' + "\n        ".join([f'<div class="write-line-dotted" style="height:24px;"></div>' for _ in range(7)]) + '''
      </div>
      <div class="eq eq-2">
        <div class="eq-header" style="color:#059669;">PLANEJAR</div>
        <div class="eq-label">Importante, Não Urgente</div>
        ''' + "\n        ".join([f'<div class="write-line-dotted" style="height:24px;"></div>' for _ in range(7)]) + '''
      </div>
      <div class="eq eq-3">
        <div class="eq-header" style="color:#D97706;">DELEGAR</div>
        <div class="eq-label">Urgente, Não Importante</div>
        ''' + "\n        ".join([f'<div class="write-line-dotted" style="height:24px;"></div>' for _ in range(7)]) + '''
      </div>
      <div class="eq eq-4">
        <div class="eq-header" style="color:#DC2626;">ELIMINAR</div>
        <div class="eq-label">Nem Urgente, Nem Importante</div>
        ''' + "\n        ".join([f'<div class="write-line-dotted" style="height:24px;"></div>' for _ in range(7)]) + '''
      </div>
    </div>'''
    pages.append(page_wrap(13, content, "Métodos", "13"))

    # P14: Regra dos 2 minutos
    content = '''<h1 class="page-title">Regra dos 2 Minutos</h1>
    <p class="page-subtitle">Se uma tarefa leva menos de 2 minutos, faça agora mesmo. Não anote, não planeje — execute.</p>
    <div class="rule-visual">
      <div class="rule-flow">
        <div class="flow-box">Tarefa apareceu</div>
        <div class="flow-arrow">↓</div>
        <div class="flow-decision">Leva menos de 2 min?</div>
        <div class="flow-branches">
          <div class="flow-yes"><strong>SIM →</strong> Faça agora</div>
          <div class="flow-no"><strong>NÃO →</strong> Anote e planeje</div>
        </div>
      </div>
    </div>
    <h2 class="section-title" style="margin-top:20px;">Lista: Faça Agora (menos de 2 min)</h2>
    <div class="two-min-list">'''
    for i in range(16):
        content += f'\n      <div class="checkbox-line"><div class="checkbox"></div><span class="label" style="flex:1;border-bottom:1px dotted #E2E8F0;padding-bottom:4px;"></span></div>'
    content += '''
    </div>
    <div class="tip-box" style="margin-top:12px;">
      <strong>Por que funciona:</strong> Completar micro-tarefas gera dopamina imediata. Cada checkbox marcado reforça o circuito de recompensa.
    </div>'''
    pages.append(page_wrap(14, content, "Métodos", "14"))

    # P15: Brain Dump
    content = '''<h1 class="page-title">Brain Dump</h1>
    <p class="page-subtitle">Despeje tudo que está na sua cabeça. Sem filtro, sem ordem, sem julgamento. Depois organize.</p>
    <div class="brain-dump-area">
      <div class="dump-section">
        <div class="dump-header"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6" stroke="#2563EB" stroke-width="1.5"/><path d="M8 5v3l2 1" stroke="#2563EB" stroke-width="1.5" stroke-linecap="round"/></svg> Preciso fazer</div>
        ''' + write_lines(8, dotted=True) + '''
      </div>
      <div class="dump-section">
        <div class="dump-header"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M2 14l5-5m0 0l5-5m-5 5l5 5m-5-5L2 4" stroke="#D97706" stroke-width="1.5" stroke-linecap="round"/></svg> Está me preocupando</div>
        ''' + write_lines(5, dotted=True) + '''
      </div>
      <div class="dump-section">
        <div class="dump-header"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 2l2 4 4.5.5-3.5 3 1 4.5L8 12l-4 2.5 1-4.5-3.5-3L6 6z" stroke="#059669" stroke-width="1.5" stroke-linejoin="round"/></svg> Ideias e vontades</div>
        ''' + write_lines(5, dotted=True) + '''
      </div>
    </div>'''
    pages.append(page_wrap(15, content, "Métodos", "15"))

    # P16: GTD Adaptado
    content = '''<h1 class="page-title">GTD Adaptado para TDAH</h1>
    <p class="page-subtitle">Getting Things Done simplificado: capture tudo, decida o próximo passo, execute sem pensar demais.</p>
    <div class="gtd-flow">
      <div class="gtd-step">
        <div class="gtd-num">1</div>
        <div class="gtd-content">
          <strong>CAPTURE</strong>
          <p>Anote TUDO que aparece na mente. Não filtre.</p>
        </div>
      </div>
      <div class="gtd-step">
        <div class="gtd-num">2</div>
        <div class="gtd-content">
          <strong>ESCLAREÇA</strong>
          <p>Para cada item: é acionável? Se sim, qual o próximo passo concreto?</p>
        </div>
      </div>
      <div class="gtd-step">
        <div class="gtd-num">3</div>
        <div class="gtd-content">
          <strong>ORGANIZE</strong>
          <p>Coloque cada item no lugar certo: hoje, esta semana, algum dia, lixo.</p>
        </div>
      </div>
      <div class="gtd-step">
        <div class="gtd-num">4</div>
        <div class="gtd-content">
          <strong>REVISE</strong>
          <p>Uma vez por semana, olhe suas listas. Atualize e ajuste.</p>
        </div>
      </div>
      <div class="gtd-step">
        <div class="gtd-num">5</div>
        <div class="gtd-content">
          <strong>EXECUTE</strong>
          <p>Escolha a tarefa com base em: contexto, energia, tempo disponível.</p>
        </div>
      </div>
    </div>
    <div class="tip-box">
      <strong>Adaptação TDAH:</strong> A revisão semanal é a parte mais difícil — mas é a mais importante. Marque um dia fixo e trate como compromisso não-negociável.
    </div>'''
    pages.append(page_wrap(16, content, "Métodos", "16"))

    # P17: Captura Rapida
    content = '''<h1 class="page-title">Captura Rápida de Ideias</h1>
    <p class="page-subtitle">Anote antes que esqueça. Processe depois. Agora só capture.</p>
    <div class="capture-grid">'''
    for i in range(12):
        content += '''
      <div class="capture-card">
        <div class="capture-top">
          <div class="checkbox"></div>
          <span class="capture-date">___/___</span>
        </div>
        <div class="write-line-dotted" style="height:20px;"></div>
        <div class="write-line-dotted" style="height:20px;"></div>
      </div>'''
    content += '''
    </div>
    <div style="margin-top:12px;font-size:8pt;color:#64748B;">Processamento: ○ Fazer agora ○ Agendar ○ Delegar ○ Algum dia ○ Descartar</div>'''
    pages.append(page_wrap(17, content, "Métodos", "17"))

    return pages
