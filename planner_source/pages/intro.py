# -*- coding: utf-8 -*-
"""Secao 1: Introducao (paginas 1-7)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers import header, footer, page_wrap, checkbox, write_lines, field


def get_pages():
    pages = []

    # P1: Capa
    pages.append('''<section class="page page-cover" id="page-1">
  <div class="cover-content">
    <div class="cover-badge">SISTEMA DE ORGANIZAÇÃO PARA TDAH</div>
    <h1 class="cover-title">Planner<br>TDAH<br>Produtivo</h1>
    <div class="cover-line"></div>
    <p class="cover-tagline">Seu cérebro funciona diferente.<br>Sua organização também pode.</p>
    <div class="cover-brand">
      <svg class="cover-logo" width="32" height="32" viewBox="0 0 32 32" fill="none">
        <rect width="32" height="32" rx="6" fill="#fff" fill-opacity="0.15"/>
        <path d="M8 16h4l3-6 4 12 3-6h4" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <span>CATreport</span>
    </div>
  </div>
</section>''')

    # P2: Pertence a
    pages.append('''<section class="page" id="page-2">
  <div class="page-content" style="display:flex;align-items:center;justify-content:center;">
    <div style="width:100%;max-width:320px;text-align:center;">
      <svg width="40" height="40" viewBox="0 0 40 40" fill="none" style="margin-bottom:24px;">
        <circle cx="20" cy="14" r="8" stroke="#2563EB" stroke-width="1.5" fill="none"/>
        <path d="M6 36c0-8 6-14 14-14s14 6 14 14" stroke="#2563EB" stroke-width="1.5" fill="none"/>
      </svg>
      <h2 style="font-size:14pt;font-weight:600;color:#1E3A8A;margin-bottom:32px;">Este planner pertence a</h2>
      <div class="field-group"><label class="field-label">Nome</label><div class="write-line"></div></div>
      <div class="field-group"><label class="field-label">E-mail</label><div class="write-line"></div></div>
      <div class="field-group"><label class="field-label">Telefone</label><div class="write-line"></div></div>
      <div class="field-group"><label class="field-label">Data de início</label><div class="write-line"></div></div>
      <div class="field-group"><label class="field-label">Minha motivação</label><div class="write-area" style="min-height:60px;"></div></div>
    </div>
  </div>
</section>''')

    # P3: Apresentacao
    content = '''<h1 class="page-title">Sobre este Planner</h1>
    <div style="max-width:145mm;line-height:1.9;color:#475569;font-size:10.5pt;">
      <p style="margin-bottom:14px;">Este não é um planner comum. Foi projetado especificamente para o cérebro que pensa rápido demais, esquece facilmente e precisa de estrutura sem rigidez.</p>
      <p style="margin-bottom:14px;">Se você tem TDAH, já sabe que agendas tradicionais não funcionam. Elas pressupõem uma memória de trabalho que não temos, uma linearidade que não é natural para nós e uma consistência que parece impossível nos dias difíceis.</p>
      <p style="margin-bottom:14px;">O <strong>Planner TDAH Produtivo</strong> foi criado para ser:</p>
      <ul class="feature-list">
        <li><strong>Flexível</strong> — use na ordem que quiser, pule páginas, volte quando precisar</li>
        <li><strong>Visual</strong> — informações organizadas de forma clara, sem sobrecarga</li>
        <li><strong>Gentil</strong> — sem culpa por dias improdutivos, sem pressão por perfeição</li>
        <li><strong>Prático</strong> — ferramentas que funcionam com o seu cérebro, não contra ele</li>
      </ul>
      <p style="margin-top:14px;">Você não precisa usar tudo. Comece por uma página que faça sentido hoje. Amanhã, escolha outra. O progresso não precisa ser linear para ser real.</p>
    </div>'''
    pages.append(page_wrap(3, content, "Introdução", "3"))

    # P4: Como Usar
    content = '''<h1 class="page-title">Como utilizar este planner</h1>
    <div class="steps-grid">
      <div class="step-card">
        <div class="step-number">01</div>
        <div class="step-title">Sem ordem fixa</div>
        <p class="step-desc">Abra em qualquer página. Não existe página errada para começar.</p>
      </div>
      <div class="step-card">
        <div class="step-number">02</div>
        <div class="step-title">Uma coisa por vez</div>
        <p class="step-desc">Escolha apenas UMA ferramenta por dia até virar hábito.</p>
      </div>
      <div class="step-card">
        <div class="step-number">03</div>
        <div class="step-title">Imprima o que precisar</div>
        <p class="step-desc">Não precisa imprimir tudo. Imprima as páginas que usar esta semana.</p>
      </div>
      <div class="step-card">
        <div class="step-number">04</div>
        <div class="step-title">Adapte sem culpa</div>
        <p class="step-desc">Risque, reescreva, use de forma diferente. O planner é seu.</p>
      </div>
      <div class="step-card">
        <div class="step-number">05</div>
        <div class="step-title">Celebre o mínimo</div>
        <p class="step-desc">Marcou um checkbox? Isso já é progresso. Reconheça cada passo.</p>
      </div>
      <div class="step-card">
        <div class="step-number">06</div>
        <div class="step-title">Recomece sempre</div>
        <p class="step-desc">Parou de usar? Sem problema. Volte quando quiser, sem julgamento.</p>
      </div>
    </div>'''
    pages.append(page_wrap(4, content, "Introdução", "4"))

    # P5: TDAH e Organizacao
    content = '''<h1 class="page-title">TDAH e Organização</h1>
    <p class="page-subtitle">Entender como seu cérebro funciona é o primeiro passo para trabalhar com ele, não contra ele.</p>
    <div class="info-grid">
      <div class="info-card">
        <div class="info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 2a10 10 0 100 20 10 10 0 000-20z" stroke="#2563EB" stroke-width="1.5"/><path d="M12 6v6l4 2" stroke="#2563EB" stroke-width="1.5" stroke-linecap="round"/></svg></div>
        <h3>Memória de Trabalho</h3>
        <p>Seu cérebro tem dificuldade em reter informações temporárias. Por isso externalize tudo: escreva, anote, registre.</p>
      </div>
      <div class="info-card">
        <div class="info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" stroke="#2563EB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        <h3>Função Executiva</h3>
        <p>Planejar, priorizar e iniciar tarefas é mais difícil. Use estruturas visuais simples para reduzir a carga cognitiva.</p>
      </div>
      <div class="info-card">
        <div class="info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="#2563EB" stroke-width="1.5"/><path d="M8 12h8M12 8v8" stroke="#2563EB" stroke-width="1.5" stroke-linecap="round"/></svg></div>
        <h3>Regulação Emocional</h3>
        <p>Frustração e autocrítica são comuns. Este planner não cobra perfeição. Qualquer progresso conta.</p>
      </div>
      <div class="info-card">
        <div class="info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83" stroke="#2563EB" stroke-width="1.5" stroke-linecap="round"/></svg></div>
        <h3>Hiperfoco vs. Distração</h3>
        <p>Seu foco oscila entre extremos. Use time blocking para canalizar o hiperfoco e pausas para gerenciar distrações.</p>
      </div>
    </div>'''
    pages.append(page_wrap(5, content, "Introdução", "5"))

    # P6: Dicas praticas
    content = '''<h1 class="page-title">Dicas práticas para o dia a dia</h1>
    <p class="page-subtitle">Estratégias baseadas em evidências, adaptadas para o cérebro TDAH.</p>
    <div class="tips-list">
      <div class="tip-item">
        <span class="tip-num">01</span>
        <div><strong>Quebre tarefas grandes em micro-ações</strong><br><span class="tip-detail">Em vez de "organizar a casa", comece com "guardar 5 objetos da mesa".</span></div>
      </div>
      <div class="tip-item">
        <span class="tip-num">02</span>
        <div><strong>Use timers (não confie na noção de tempo)</strong><br><span class="tip-detail">Defina alarmes para tudo: início, pausas, transições, fim do dia.</span></div>
      </div>
      <div class="tip-item">
        <span class="tip-num">03</span>
        <div><strong>Reduza a fricção de iniciar</strong><br><span class="tip-detail">Deixe tudo visível e acessível. Se está guardado, não existe.</span></div>
      </div>
      <div class="tip-item">
        <span class="tip-num">04</span>
        <div><strong>Externalize sua memória</strong><br><span class="tip-detail">Tudo que está na sua cabeça precisa ir para o papel. Agora.</span></div>
      </div>
      <div class="tip-item">
        <span class="tip-num">05</span>
        <div><strong>Recompense cada pequeno progresso</strong><br><span class="tip-detail">Seu cérebro precisa de dopamina. Crie micro-recompensas conscientes.</span></div>
      </div>
      <div class="tip-item">
        <span class="tip-num">06</span>
        <div><strong>Planeje no máximo 3 tarefas principais por dia</strong><br><span class="tip-detail">Menos é mais. Concluir 3 é melhor que começar 10.</span></div>
      </div>
      <div class="tip-item">
        <span class="tip-num">07</span>
        <div><strong>Crie âncoras de rotina (não rotinas rígidas)</strong><br><span class="tip-detail">Associe novos hábitos a ações que já faz: "depois do café, anoto 3 prioridades".</span></div>
      </div>
      <div class="tip-item">
        <span class="tip-num">08</span>
        <div><strong>Aceite dias ruins sem culpa</strong><br><span class="tip-detail">Consistência não é perfeição. É voltar sempre que puder.</span></div>
      </div>
    </div>'''
    pages.append(page_wrap(6, content, "Introdução", "6"))

    # P7: Sumario
    toc_items = [
        ("Introdução", "1–7"),
        ("Métodos de Produtividade", "8–17"),
        ("Metas", "18–29"),
        ("Planejamento Mensal", "30–41"),
        ("Planejamento Semanal", "42–51"),
        ("Planejamento Diário", "52–63"),
        ("Trackers e Controles", "64–79"),
        ("Finanças", "80–89"),
        ("Saúde e Bem-estar", "90–101"),
        ("Estudos e Projetos", "102–109"),
        ("Reflexão e Diário", "110–117"),
        ("Notas", "118–120"),
    ]
    toc_html = ""
    for title, pgs in toc_items:
        toc_html += f'<div class="toc-item"><span class="toc-title">{title}</span><span class="toc-dots"></span><span class="toc-page">{pgs}</span></div>\n'
    content = f'''<h1 class="page-title">Sumário</h1>
    <div class="toc">{toc_html}</div>'''
    pages.append(page_wrap(7, content, "Sumário", "7"))

    return pages
