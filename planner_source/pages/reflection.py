# -*- coding: utf-8 -*-
"""Secao 11: Reflexao e Diario (paginas 108-117)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers import page_wrap, checkbox, write_lines, field


def get_pages():
    pages = []

    # P108: Diario Guiado
    content = '''<h1 class="page-title">Diário Guiado</h1>
    <div class="daily-header-fields"><label class="field-label-inline">Data:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <div class="journal-sections" style="margin-top:16px;">
      <div class="journal-prompt">
        <div class="subsection-title">Como estou me sentindo agora?</div>
        ''' + write_lines(3, dotted=True) + '''
      </div>
      <div class="journal-prompt" style="margin-top:14px;">
        <div class="subsection-title">O que está ocupando minha mente?</div>
        ''' + write_lines(3, dotted=True) + '''
      </div>
      <div class="journal-prompt" style="margin-top:14px;">
        <div class="subsection-title">Uma coisa que fiz bem hoje</div>
        ''' + write_lines(2, dotted=True) + '''
      </div>
      <div class="journal-prompt" style="margin-top:14px;">
        <div class="subsection-title">O que preciso soltar / aceitar?</div>
        ''' + write_lines(2, dotted=True) + '''
      </div>
      <div class="journal-prompt" style="margin-top:14px;">
        <div class="subsection-title">Amanhã quero...</div>
        ''' + write_lines(2, dotted=True) + '''
      </div>
    </div>'''
    pages.append(page_wrap(108, content, "Reflexão", "108"))

    # P109: Gratidao
    content = '''<h1 class="page-title">Diário de Gratidão</h1>
    <p class="page-subtitle">Gratidão reconecta o cérebro com o positivo — especialmente nos dias em que tudo parece dar errado.</p>
    <div class="gratitude-grid">''' + ''.join([f'''
      <div class="gratitude-day">
        <div class="gratitude-header">Dia <span class="gratitude-num">{i}</span></div>
        <div class="gratitude-lines">
          <div class="gratitude-item">1. <div class="write-line-dotted" style="display:inline-block;width:85%;"></div></div>
          <div class="gratitude-item">2. <div class="write-line-dotted" style="display:inline-block;width:85%;"></div></div>
          <div class="gratitude-item">3. <div class="write-line-dotted" style="display:inline-block;width:85%;"></div></div>
        </div>
      </div>''' for i in range(1, 8)]) + '''
    </div>'''
    pages.append(page_wrap(109, content, "Reflexão", "109"))

    # P110: Gratidao Mensal
    content = '''<h1 class="page-title">Gratidão do Mês</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:150px;display:inline-block;"></div></div>
    <div class="gratitude-monthly" style="margin-top:12px;">''' + ''.join([f'''
      <div class="gm-row"><div class="gm-day">{i:02d}</div><div class="write-line-dotted" style="flex:1;"></div></div>''' for i in range(1, 32)]) + '''
    </div>'''
    pages.append(page_wrap(110, content, "Reflexão", "110"))

    # P111: Reflexoes Profundas
    content = '''<h1 class="page-title">Reflexões</h1>
    <p class="page-subtitle">Reserve um momento de calma para responder. Não existe resposta certa.</p>
    <div class="reflection-questions">
      <div class="rq-item">
        <div class="rq-question">O que eu faria se não tivesse medo de falhar?</div>
        ''' + write_lines(3, dotted=True) + '''
      </div>
      <div class="rq-item">
        <div class="rq-question">Qual hábito, se eu construísse, mudaria tudo?</div>
        ''' + write_lines(3, dotted=True) + '''
      </div>
      <div class="rq-item">
        <div class="rq-question">O que estou tolerando que não deveria?</div>
        ''' + write_lines(3, dotted=True) + '''
      </div>
      <div class="rq-item">
        <div class="rq-question">Como posso ser mais gentil comigo mesmo esta semana?</div>
        ''' + write_lines(3, dotted=True) + '''
      </div>
    </div>'''
    pages.append(page_wrap(111, content, "Reflexão", "111"))

    # P112: Brain Dump
    content = '''<h1 class="page-title">Brain Dump</h1>
    <p class="page-subtitle">Tire TUDO da cabeça. Sem filtro, sem ordem, sem julgamento. Organize depois.</p>
    <div class="braindump-area">
      ''' + write_lines(28, dotted=True) + '''
    </div>'''
    pages.append(page_wrap(112, content, "Reflexão", "112"))

    # P113: Captura Rapida de Ideias
    content = '''<h1 class="page-title">Captura Rápida</h1>
    <p class="page-subtitle">Ideias, tarefas, pensamentos aleatórios — anote aqui antes que desapareçam.</p>
    <div class="capture-grid">''' + ''.join([f'''
      <div class="capture-card">
        <div class="capture-num">{i:02d}</div>
        <div class="write-line-dotted" style="flex:1;"></div>
        <div class="capture-type">
          <span class="ct-option">□ Tarefa</span>
          <span class="ct-option">□ Ideia</span>
          <span class="ct-option">□ Lembrete</span>
        </div>
      </div>''' for i in range(1, 21)]) + '''
    </div>'''
    pages.append(page_wrap(113, content, "Reflexão", "113"))

    # P114: Planejamento de Projeto
    content = '''<h1 class="page-title">Planejamento de Projeto</h1>
    <div class="project-header" style="margin-bottom:16px;">
      <div class="grid-2">
        <div>''' + field("Nome do Projeto") + field("Objetivo Final") + '''</div>
        <div>''' + field("Prazo") + field("Por que isso importa?") + '''</div>
      </div>
    </div>
    <div class="project-steps">
      <div class="subsection-title">Etapas (quebre em partes pequenas)</div>
      <table class="table">
        <thead><tr><th style="width:5%;">#</th><th style="width:40%;">Etapa</th><th style="width:20%;">Prazo</th><th style="width:20%;">Depende de</th><th style="width:15%;">Status</th></tr></thead>
        <tbody>''' + ''.join([f'<tr><td>{i}</td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="checkbox" style="margin:auto;"></div></td></tr>' for i in range(1, 11)]) + '''
        </tbody>
      </table>
    </div>
    <div style="margin-top:12px;">
      <div class="subsection-title">Possíveis obstáculos e soluções</div>
      <div class="grid-2">
        <div><label class="field-label">Obstáculo</label>''' + write_lines(3) + '''</div>
        <div><label class="field-label">Solução</label>''' + write_lines(3) + '''</div>
      </div>
    </div>'''
    pages.append(page_wrap(114, content, "Reflexão", "114"))

    # P115: Revisao Semanal Profunda
    content = '''<h1 class="page-title">Revisão Semanal</h1>
    <div class="week-field"><label class="field-label-inline">Semana de:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <div class="review-deep" style="margin-top:16px;">
      <div class="grid-2" style="gap:16px;">
        <div class="card">
          <div class="card-header">Conquistas</div>
          <p style="font-size:9pt;color:#64748B;">O que concluí, por menor que seja</p>
          ''' + write_lines(4, dotted=True) + '''
        </div>
        <div class="card">
          <div class="card-header">Desafios</div>
          <p style="font-size:9pt;color:#64748B;">O que foi difícil e por quê</p>
          ''' + write_lines(4, dotted=True) + '''
        </div>
      </div>
      <div class="card" style="margin-top:12px;">
        <div class="card-header">Lições</div>
        <p style="font-size:9pt;color:#64748B;">O que aprendi sobre mim e meu funcionamento</p>
        ''' + write_lines(3, dotted=True) + '''
      </div>
      <div class="grid-2" style="gap:16px;margin-top:12px;">
        <div>
          <div class="subsection-title">Manter na próxima semana</div>
          ''' + '\n'.join([checkbox("_"*35) for _ in range(3)]) + '''
        </div>
        <div>
          <div class="subsection-title">Ajustar na próxima semana</div>
          ''' + '\n'.join([checkbox("_"*35) for _ in range(3)]) + '''
        </div>
      </div>
    </div>'''
    pages.append(page_wrap(115, content, "Reflexão", "115"))

    # P116: Revisao Mensal
    content = '''<h1 class="page-title">Revisão do Mês</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:150px;display:inline-block;"></div></div>
    <div class="monthly-review" style="margin-top:14px;">
      <div class="card card-blue">
        <div class="card-header">Resumo do Mês em 3 Palavras</div>
        <div class="grid-3" style="text-align:center;margin-top:8px;">
          <div class="write-line"></div>
          <div class="write-line"></div>
          <div class="write-line"></div>
        </div>
      </div>
      <div class="grid-2" style="gap:16px;margin-top:14px;">
        <div>
          <div class="subsection-title">Metas alcançadas</div>
          ''' + '\n'.join([checkbox("_"*35) for _ in range(4)]) + '''
        </div>
        <div>
          <div class="subsection-title">Metas não alcançadas (e por quê)</div>
          ''' + write_lines(4) + '''
        </div>
      </div>
      <div style="margin-top:14px;">
        <div class="subsection-title">Melhor momento do mês</div>
        ''' + write_lines(2, dotted=True) + '''
      </div>
      <div style="margin-top:10px;">
        <div class="subsection-title">O que preciso mudar</div>
        ''' + write_lines(2, dotted=True) + '''
      </div>
      <div style="margin-top:10px;">
        <div class="subsection-title">Nota para meu eu do próximo mês</div>
        ''' + write_lines(3, dotted=True) + '''
      </div>
    </div>'''
    pages.append(page_wrap(116, content, "Reflexão", "116"))

    # P117: Vitorias
    content = '''<h1 class="page-title">Minhas Vitórias</h1>
    <p class="page-subtitle">Registre conquistas de todos os tamanhos. Com TDAH, a gente esquece o quanto já avançou.</p>
    <div class="victories-list">''' + ''.join([f'''
      <div class="victory-row">
        <div class="victory-num">{i:02d}</div>
        <div class="victory-content">
          <div class="write-line-dotted"></div>
          <div class="victory-meta"><label class="field-label-inline">Data:</label><div class="write-line" style="width:80px;display:inline-block;"></div></div>
        </div>
      </div>''' for i in range(1, 16)]) + '''
    </div>'''
    pages.append(page_wrap(117, content, "Reflexão", "117"))

    return pages
