# -*- coding: utf-8 -*-
"""Secao 3: Metas (paginas 18-29)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers import page_wrap, checkbox, write_lines, field


def get_pages():
    pages = []

    # P18: Metas Anuais - Visao Geral
    content = '''<h1 class="page-title">Metas Anuais</h1>
    <p class="page-subtitle">Escolha entre 3 e 6 metas para o ano. Menos é mais — especialmente para o cérebro TDAH.</p>
    <div class="goals-list">''' + "".join([f'''
      <div class="goal-row">
        <div class="goal-num">{i}</div>
        <div class="goal-fields">
          <div class="goal-main"><label class="field-label-inline">Meta</label><div class="write-line"></div></div>
          <div class="grid-2">
            <div><label class="field-label-inline">Por quê?</label><div class="write-line"></div></div>
            <div><label class="field-label-inline">Prazo</label><div class="write-line"></div></div>
          </div>
        </div>
      </div>''' for i in range(1, 7)]) + '''
    </div>'''
    pages.append(page_wrap(18, content, "Metas", "18"))

    # P19: Metas por Categoria
    content = '''<h1 class="page-title">Metas por Área da Vida</h1>
    <div class="grid-2" style="gap:20px;">
      <div class="category-card">
        <div class="cat-header"><svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9 1v16M5 5l4-4 4 4" stroke="#2563EB" stroke-width="1.5" stroke-linecap="round"/></svg> Saúde</div>
        ''' + write_lines(4) + '''
      </div>
      <div class="category-card">
        <div class="cat-header"><svg width="18" height="18" viewBox="0 0 18 18" fill="none"><rect x="2" y="4" width="14" height="11" rx="2" stroke="#2563EB" stroke-width="1.5"/><path d="M6 1v4M12 1v4" stroke="#2563EB" stroke-width="1.5" stroke-linecap="round"/></svg> Carreira</div>
        ''' + write_lines(4) + '''
      </div>
      <div class="category-card">
        <div class="cat-header"><svg width="18" height="18" viewBox="0 0 18 18" fill="none"><circle cx="9" cy="9" r="7" stroke="#2563EB" stroke-width="1.5"/><path d="M9 5v4h3" stroke="#2563EB" stroke-width="1.5" stroke-linecap="round"/></svg> Finanças</div>
        ''' + write_lines(4) + '''
      </div>
      <div class="category-card">
        <div class="cat-header"><svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9 2l2 4h4l-3 3 1 4-4-2-4 2 1-4-3-3h4z" stroke="#2563EB" stroke-width="1.5" stroke-linejoin="round"/></svg> Pessoal</div>
        ''' + write_lines(4) + '''
      </div>
    </div>'''
    pages.append(page_wrap(19, content, "Metas", "19"))

    # P20: Metas Trimestrais Q1
    content = '''<h1 class="page-title">Metas — 1º Trimestre</h1>
    <p class="page-subtitle">Janeiro • Fevereiro • Março</p>
    <div class="quarter-goals">
      <div class="q-goal">
        <div class="q-goal-header">Meta Principal</div>
        <div class="write-area" style="min-height:35px;"></div>
        <div class="grid-3" style="margin-top:8px;">
          <div><label class="field-label-inline">Ação Mês 1</label><div class="write-line"></div></div>
          <div><label class="field-label-inline">Ação Mês 2</label><div class="write-line"></div></div>
          <div><label class="field-label-inline">Ação Mês 3</label><div class="write-line"></div></div>
        </div>
      </div>
      <div class="q-goal">
        <div class="q-goal-header">Meta Secundária</div>
        <div class="write-area" style="min-height:35px;"></div>
        <div class="grid-3" style="margin-top:8px;">
          <div><label class="field-label-inline">Ação Mês 1</label><div class="write-line"></div></div>
          <div><label class="field-label-inline">Ação Mês 2</label><div class="write-line"></div></div>
          <div><label class="field-label-inline">Ação Mês 3</label><div class="write-line"></div></div>
        </div>
      </div>
      <div class="q-goal">
        <div class="q-goal-header">Hábito para Construir</div>
        <div class="write-line"></div>
        <div style="margin-top:8px;"><label class="field-label-inline">Frequência:</label><div class="write-line"></div></div>
      </div>
    </div>
    <div class="review-mini" style="margin-top:16px;">
      <div class="subsection-title">Revisão Rápida (preencher no final do trimestre)</div>
      ''' + checkbox("Alcancei a meta principal") + checkbox("Alcancei a meta secundária") + checkbox("Mantive o hábito") + '''
      <div style="margin-top:8px;"><label class="field-label-inline">Ajuste para o próximo trimestre:</label><div class="write-line"></div></div>
    </div>'''
    pages.append(page_wrap(20, content, "Metas", "20"))

    # P21: Metas Trimestrais Q2
    content = '''<h1 class="page-title">Metas — 2º Trimestre</h1>
    <p class="page-subtitle">Abril • Maio • Junho</p>
    <div class="quarter-goals">
      <div class="q-goal card-blue">
        <div class="q-goal-header">Foco do Trimestre</div>
        <div class="write-area" style="min-height:35px;"></div>
      </div>
      <div class="grid-2" style="gap:16px;">
        <div class="q-goal">
          <div class="q-goal-header">Meta 1</div>
          <div class="write-line"></div>
          <div style="margin-top:6px;"><label class="field-label-inline">Indicador de sucesso:</label><div class="write-line"></div></div>
          <div style="margin-top:6px;"><label class="field-label-inline">Primeiro passo:</label><div class="write-line"></div></div>
        </div>
        <div class="q-goal">
          <div class="q-goal-header">Meta 2</div>
          <div class="write-line"></div>
          <div style="margin-top:6px;"><label class="field-label-inline">Indicador de sucesso:</label><div class="write-line"></div></div>
          <div style="margin-top:6px;"><label class="field-label-inline">Primeiro passo:</label><div class="write-line"></div></div>
        </div>
      </div>
      <div class="q-goal" style="margin-top:12px;">
        <div class="q-goal-header">O que quero PARAR de fazer este trimestre</div>
        ''' + write_lines(2) + '''
      </div>
      <div class="q-goal">
        <div class="q-goal-header">O que quero COMEÇAR este trimestre</div>
        ''' + write_lines(2) + '''
      </div>
    </div>'''
    pages.append(page_wrap(21, content, "Metas", "21"))

    # P22: Metas Trimestrais Q3
    content = '''<h1 class="page-title">Metas — 3º Trimestre</h1>
    <p class="page-subtitle">Julho • Agosto • Setembro</p>
    <div class="quarter-review-top card-dark" style="padding:16px;border-radius:8px;margin-bottom:16px;">
      <div class="subsection-title">Revisão do semestre até aqui</div>
      <div class="grid-2">
        <div><label class="field-label-inline">Maior conquista:</label><div class="write-line"></div></div>
        <div><label class="field-label-inline">Maior aprendizado:</label><div class="write-line"></div></div>
      </div>
    </div>
    <div class="quarter-goals">''' + "".join([f'''
      <div class="q-goal-compact">
        <div class="q-goal-num">{i}</div>
        <div class="q-goal-content">
          <div class="write-line"></div>
          <div class="grid-2" style="margin-top:6px;gap:8px;">
            <div><label class="field-label-inline">Prazo:</label><div class="write-line"></div></div>
            <div><label class="field-label-inline">Recompensa:</label><div class="write-line"></div></div>
          </div>
        </div>
      </div>''' for i in range(1, 4)]) + '''
    </div>'''
    pages.append(page_wrap(22, content, "Metas", "22"))

    # P23: Metas Trimestrais Q4
    content = '''<h1 class="page-title">Metas — 4º Trimestre</h1>
    <p class="page-subtitle">Outubro • Novembro • Dezembro</p>
    <div class="quarter-goals">
      <div class="q-goal card-blue">
        <div class="q-goal-header">Como quero terminar o ano?</div>
        <div class="write-area" style="min-height:40px;"></div>
      </div>
      <div class="q-goal">
        <div class="q-goal-header">3 coisas para finalizar antes de 31/12</div>
        ''' + checkbox("") + checkbox("") + checkbox("") + '''
      </div>
      <div class="q-goal">
        <div class="q-goal-header">1 hábito para solidificar</div>
        <div class="write-line"></div>
      </div>
      <div class="q-goal">
        <div class="q-goal-header">Preview do próximo ano</div>
        <div class="grid-2" style="gap:8px;">
          <div><label class="field-label-inline">Palavra do próximo ano:</label><div class="write-line"></div></div>
          <div><label class="field-label-inline">Foco principal:</label><div class="write-line"></div></div>
        </div>
      </div>
    </div>'''
    pages.append(page_wrap(23, content, "Metas", "23"))

    # P24: Metas Mensais Template
    content = '''<h1 class="page-title">Metas do Mês</h1>
    <div class="month-field"><label class="field-label">Mês / Ano:</label><div class="write-line" style="max-width:200px;"></div></div>
    <div class="monthly-goals-layout">
      <div class="mg-main">
        <div class="subsection-title">Metas Principais (máximo 3)</div>
        <div class="mg-item">
          <div class="mg-num">1</div>
          <div class="mg-content">''' + write_lines(1) + '''
            <div class="grid-2" style="margin-top:6px;"><div>''' + field("Ações necessárias") + '''</div><div>''' + field("Como medir") + '''</div></div>
          </div>
        </div>
        <div class="mg-item">
          <div class="mg-num">2</div>
          <div class="mg-content">''' + write_lines(1) + '''
            <div class="grid-2" style="margin-top:6px;"><div>''' + field("Ações necessárias") + '''</div><div>''' + field("Como medir") + '''</div></div>
          </div>
        </div>
        <div class="mg-item">
          <div class="mg-num">3</div>
          <div class="mg-content">''' + write_lines(1) + '''
            <div class="grid-2" style="margin-top:6px;"><div>''' + field("Ações necessárias") + '''</div><div>''' + field("Como medir") + '''</div></div>
          </div>
        </div>
      </div>
      <div class="mg-side card-dark" style="padding:12px;border-radius:8px;">
        <div class="subsection-title">Neste mês quero sentir</div>
        ''' + write_lines(2, dotted=True) + '''
        <div class="subsection-title" style="margin-top:12px;">Palavra do mês</div>
        <div class="write-area" style="min-height:30px;text-align:center;"></div>
      </div>
    </div>'''
    pages.append(page_wrap(24, content, "Metas", "24"))

    # P25: Metas Semanais Template
    content = '''<h1 class="page-title">Metas da Semana</h1>
    <div class="grid-2" style="gap:8px;margin-bottom:12px;">
      <div>''' + field("Semana de") + '''</div>
      <div>''' + field("Até") + '''</div>
    </div>
    <div class="weekly-goals-layout">
      <div class="wg-priority">
        <div class="subsection-title">As 3 coisas mais importantes</div>
        <p style="font-size:9pt;color:#64748B;margin-bottom:8px;">Se eu fizer SÓ estas 3 coisas, a semana foi um sucesso.</p>
        <div class="priority-item"><span class="pri-badge">1</span><div class="write-line" style="flex:1;"></div></div>
        <div class="priority-item"><span class="pri-badge">2</span><div class="write-line" style="flex:1;"></div></div>
        <div class="priority-item"><span class="pri-badge">3</span><div class="write-line" style="flex:1;"></div></div>
      </div>
      <div class="wg-secondary" style="margin-top:16px;">
        <div class="subsection-title">Também quero fazer (se sobrar energia)</div>
        ''' + "\n".join([checkbox("") for _ in range(5)]) + '''
      </div>
      <div class="wg-selfcare" style="margin-top:16px;">
        <div class="subsection-title">Autocuidado da semana</div>
        <div class="grid-2">
          <div>''' + checkbox("Dormir 7h+ por noite") + checkbox("Exercício 3x") + checkbox("Tempo ao ar livre") + '''</div>
          <div>''' + checkbox("Sem telas 1h antes de dormir") + checkbox("Beber 2L água/dia") + checkbox("Momento de lazer") + '''</div>
        </div>
      </div>
    </div>'''
    pages.append(page_wrap(25, content, "Metas", "25"))

    # P26: Metas Diarias
    content = '''<h1 class="page-title">Metas do Dia</h1>
    <div class="grid-2" style="gap:8px;margin-bottom:16px;">
      <div>''' + field("Data") + '''</div>
      <div>''' + field("Energia hoje (1-10)") + '''</div>
    </div>
    <div class="daily-goals">
      <div class="dg-must">
        <div class="subsection-title" style="color:#1E3A8A;">A única coisa que PRECISO fazer hoje</div>
        <div class="write-area" style="min-height:40px;border-color:#2563EB;"></div>
      </div>
      <div class="dg-want" style="margin-top:14px;">
        <div class="subsection-title">Quero fazer (escolha até 3)</div>
        ''' + "\n".join([checkbox("") for _ in range(3)]) + '''
      </div>
      <div class="dg-bonus" style="margin-top:14px;">
        <div class="subsection-title">Bônus (se sobrar tempo e energia)</div>
        ''' + "\n".join([checkbox("") for _ in range(3)]) + '''
      </div>
      <div class="dg-reward" style="margin-top:14px;">
        <div class="grid-2">
          <div>''' + field("Minha recompensa hoje") + '''</div>
          <div>''' + field("Nota do dia (1-10)") + '''</div>
        </div>
      </div>
    </div>'''
    pages.append(page_wrap(26, content, "Metas", "26"))

    # P27: Decomposicao de Meta
    content = '''<h1 class="page-title">Decomposição de Meta</h1>
    <p class="page-subtitle">Metas grandes paralisam. Quebre em pedaços tão pequenos que pareçam ridiculamente fáceis.</p>
    <div class="decomp-layout">
      <div class="decomp-big">
        <label class="field-label">Meta Grande (o destino final)</label>
        <div class="write-area" style="min-height:35px;"></div>
      </div>
      <div class="decomp-arrow">↓</div>
      <div class="decomp-medium">
        <label class="field-label">Etapas Intermediárias (o caminho)</label>
        <div class="grid-2" style="gap:8px;">''' + "".join([f'''
          <div class="decomp-step"><span class="step-num">{i}</span><div class="write-line"></div></div>''' for i in range(1, 5)]) + '''
        </div>
      </div>
      <div class="decomp-arrow">↓</div>
      <div class="decomp-small">
        <label class="field-label">Micro-ações (faça HOJE)</label>
        ''' + "\n".join([checkbox("") for _ in range(4)]) + '''
      </div>
    </div>
    <div class="tip-box" style="margin-top:12px;">
      <strong>Regra de ouro:</strong> Se uma tarefa parece grande demais para começar, quebre mais. A menor ação possível é sempre o melhor começo.
    </div>'''
    pages.append(page_wrap(27, content, "Metas", "27"))

    # P28: Tracker de Progresso
    content = '''<h1 class="page-title">Tracker de Progresso</h1>
    <p class="page-subtitle">Visualize o quanto já caminhou. O progresso visível mantém a motivação.</p>
    <div class="progress-trackers">''' + "".join([f'''
      <div class="progress-item">
        <div class="progress-label"><label class="field-label-inline">Meta:</label><div class="write-line" style="flex:1;"></div></div>
        <div class="progress-bar"><div class="progress-segments">''' + "".join(['<div class="prog-seg"></div>' for _ in range(10)]) + '''</div></div>
        <div class="progress-meta grid-2"><div><label class="field-label-inline">Início:</label><div class="write-line"></div></div><div><label class="field-label-inline">Prazo:</label><div class="write-line"></div></div></div>
      </div>''' for _ in range(5)]) + '''
    </div>
    <div class="tip-box" style="margin-top:8px;">Preencha um segmento a cada 10% concluído. Não precisa ser perfeito — estimativa é suficiente.</div>'''
    pages.append(page_wrap(28, content, "Metas", "28"))

    # P29: Revisao de Metas
    content = '''<h1 class="page-title">Revisão de Metas</h1>
    <p class="page-subtitle">Pause, olhe para trás e ajuste a rota. Revisão não é julgamento — é recalibração.</p>
    <div class="review-layout">
      <div class="review-q">
        <div class="review-label">Quais metas eu ALCANCEI?</div>
        <div class="write-area" style="min-height:50px;"></div>
      </div>
      <div class="review-q">
        <div class="review-label">Quais metas eu AJUSTEI? Por quê?</div>
        <div class="write-area" style="min-height:50px;"></div>
      </div>
      <div class="review-q">
        <div class="review-label">Quais metas eu ABANDONEI? Ainda fazem sentido?</div>
        <div class="write-area" style="min-height:50px;"></div>
      </div>
      <div class="review-q">
        <div class="review-label">O que aprendi sobre mim neste processo?</div>
        <div class="write-area" style="min-height:50px;"></div>
      </div>
      <div class="review-q">
        <div class="review-label">Novas metas que surgiram:</div>
        ''' + write_lines(3) + '''
      </div>
    </div>'''
    pages.append(page_wrap(29, content, "Metas", "29"))

    return pages
