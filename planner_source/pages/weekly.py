# -*- coding: utf-8 -*-
"""Secao 5: Planejamento Semanal (paginas 42-51)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers import page_wrap, checkbox, write_lines, field


def get_pages():
    pages = []
    dias = ["Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]

    # P42: Visao Semanal Completa
    day_cols = ""
    for d in dias:
        day_cols += f'''<div class="week-day-col">
        <div class="week-day-name">{d[:3]}</div>
        <div class="week-day-space">''' + write_lines(5, dotted=True) + '''</div>
      </div>'''
    content = f'''<h1 class="page-title">Visão Semanal</h1>
    <div class="week-field"><label class="field-label-inline">Semana de:</label><div class="write-line" style="width:200px;display:inline-block;"></div></div>
    <div class="week-grid-full">{day_cols}</div>
    <div style="margin-top:12px;">
      <div class="subsection-title">Notas da Semana</div>
      ''' + write_lines(2) + '''
    </div>'''
    pages.append(page_wrap(42, content, "Semanal", "42"))

    # P43: Objetivos da Semana
    content = '''<h1 class="page-title">Objetivos da Semana</h1>
    <div class="week-field"><label class="field-label-inline">Semana:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <div style="margin-top:20px;">
      <div class="priority-section">
        <div class="priority-label high">PRIORIDADE MÁXIMA</div>
        <p style="font-size:9pt;color:#64748B;margin-bottom:8px;">Se eu pudesse fazer apenas UMA coisa esta semana, seria:</p>
        <div class="write-area" style="min-height:40px;"></div>
      </div>
      <div class="priority-section" style="margin-top:16px;">
        <div class="priority-label medium">IMPORTANTES</div>
        ''' + '\n'.join([checkbox(f"{'_'*50}") for _ in range(3)]) + '''
      </div>
      <div class="priority-section" style="margin-top:16px;">
        <div class="priority-label low">SE DER TEMPO</div>
        ''' + '\n'.join([checkbox(f"{'_'*50}") for _ in range(3)]) + '''
      </div>
    </div>
    <div class="tip-box" style="margin-top:16px;">
      <strong>Lembre:</strong> Completar 1 tarefa importante vale mais que começar 10 tarefas pequenas.
    </div>'''
    pages.append(page_wrap(43, content, "Semanal", "43"))

    # P44: Prioridades Semana - Metodo ABC
    content = '''<h1 class="page-title">Prioridades — Método ABC</h1>
    <div class="week-field"><label class="field-label-inline">Semana:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <div class="abc-grid" style="margin-top:16px;">
      <div class="abc-section">
        <div class="abc-badge a">A</div>
        <div class="abc-title">Urgente + Importante</div>
        <p class="abc-desc">Fazer primeiro, sem pensar demais</p>
        ''' + '\n'.join([checkbox(f"{'_'*42}") for _ in range(4)]) + '''
      </div>
      <div class="abc-section">
        <div class="abc-badge b">B</div>
        <div class="abc-title">Importante, não urgente</div>
        <p class="abc-desc">Agendar um horário específico</p>
        ''' + '\n'.join([checkbox(f"{'_'*42}") for _ in range(4)]) + '''
      </div>
      <div class="abc-section">
        <div class="abc-badge c">C</div>
        <div class="abc-title">Urgente, não importante</div>
        <p class="abc-desc">Delegar ou simplificar ao máximo</p>
        ''' + '\n'.join([checkbox(f"{'_'*42}") for _ in range(3)]) + '''
      </div>
    </div>'''
    pages.append(page_wrap(44, content, "Semanal", "44"))

    # P45: Rotina Semanal Fixa
    hours = ["06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00"]
    rows = ""
    for h in hours:
        cells = ''.join([f'<td class="routine-cell"></td>' for _ in range(7)])
        rows += f'<tr><td class="routine-hour">{h}</td>{cells}</tr>'
    header_cells = ''.join([f'<th>{d[:3]}</th>' for d in dias])
    content = f'''<h1 class="page-title">Rotina Semanal Fixa</h1>
    <p class="page-subtitle">Mapeie seus compromissos recorrentes. O que se repete toda semana?</p>
    <table class="table routine-table">
      <thead><tr><th></th>{header_cells}</tr></thead>
      <tbody>{rows}</tbody>
    </table>'''
    pages.append(page_wrap(45, content, "Semanal", "45"))

    # P46: Meal Prep Semanal
    meal_rows = ""
    meals = ["Café","Almoço","Lanche","Jantar"]
    for meal in meals:
        cells = ''.join([f'<td class="meal-cell"></td>' for _ in range(7)])
        meal_rows += f'<tr><td class="meal-name">{meal}</td>{cells}</tr>'
    header_cells = ''.join([f'<th>{d[:3]}</th>' for d in dias])
    content = f'''<h1 class="page-title">Planejamento Alimentar</h1>
    <div class="week-field"><label class="field-label-inline">Semana:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <table class="table meal-table" style="margin-top:14px;">
      <thead><tr><th></th>{header_cells}</tr></thead>
      <tbody>{meal_rows}</tbody>
    </table>
    <div class="grid-2" style="margin-top:16px;gap:20px;">
      <div>
        <div class="subsection-title">Lista de Compras</div>
        ''' + '\n'.join([checkbox(f"{'_'*30}") for _ in range(8)]) + '''
      </div>
      <div>
        <div class="subsection-title">Preparar com Antecedência</div>
        ''' + '\n'.join([checkbox(f"{'_'*30}") for _ in range(5)]) + '''
      </div>
    </div>'''
    pages.append(page_wrap(46, content, "Semanal", "46"))

    # P47: Revisao Semanal
    content = '''<h1 class="page-title">Revisão da Semana</h1>
    <div class="week-field"><label class="field-label-inline">Semana:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <div class="review-grid" style="margin-top:16px;">
      <div class="review-section">
        <div class="subsection-title">O que funcionou esta semana?</div>
        ''' + write_lines(3) + '''
      </div>
      <div class="review-section">
        <div class="subsection-title">O que não funcionou?</div>
        ''' + write_lines(3) + '''
      </div>
      <div class="review-section">
        <div class="subsection-title">O que aprendi sobre mim?</div>
        ''' + write_lines(2) + '''
      </div>
      <div class="grid-3" style="gap:16px;margin-top:12px;">
        <div class="mini-metric">
          <div class="metric-label">Energia Média</div>
          <div class="metric-scale">1 2 3 4 5 6 7 8 9 10</div>
        </div>
        <div class="mini-metric">
          <div class="metric-label">Humor Médio</div>
          <div class="metric-scale">1 2 3 4 5 6 7 8 9 10</div>
        </div>
        <div class="mini-metric">
          <div class="metric-label">Produtividade</div>
          <div class="metric-scale">1 2 3 4 5 6 7 8 9 10</div>
        </div>
      </div>
      <div class="review-section" style="margin-top:14px;">
        <div class="subsection-title">Ajuste para a próxima semana:</div>
        ''' + write_lines(2) + '''
      </div>
    </div>'''
    pages.append(page_wrap(47, content, "Semanal", "47"))

    # P48: Checklist Semanal Casa
    content = '''<h1 class="page-title">Checklist Semanal — Casa</h1>
    <p class="page-subtitle">Distribua tarefas ao longo da semana. Não tente tudo em um dia.</p>
    <div class="house-grid">''' + ''.join([f'''
      <div class="house-day">
        <div class="house-day-name">{d}</div>
        {checkbox("_" * 28)}
        {checkbox("_" * 28)}
        {checkbox("_" * 28)}
      </div>''' for d in dias]) + '''
    </div>'''
    pages.append(page_wrap(48, content, "Semanal", "48"))

    # P49: Tarefas Delegadas
    content = '''<h1 class="page-title">Tarefas Delegadas</h1>
    <p class="page-subtitle">Se você não precisa fazer sozinho, delegue. Acompanhe aqui.</p>
    <table class="table">
      <thead>
        <tr><th style="width:30%">Tarefa</th><th style="width:20%">Para quem</th><th style="width:18%">Prazo</th><th style="width:15%">Status</th><th>Notas</th></tr>
      </thead>
      <tbody>''' + ''.join(['''
        <tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>''' for _ in range(12)]) + '''
      </tbody>
    </table>'''
    pages.append(page_wrap(49, content, "Semanal", "49"))

    # P50: Habitos Semanais - Tracker Mini
    habits = ["Exercício","Meditação","Leitura","Água (2L)","Sono 7h+","Sem celular 1h","Organizar mesa","Cozinhar"]
    habit_rows = ""
    for h in habits:
        cells = ''.join(['<td><div class="tracker-cell-sm"></div></td>' for _ in range(7)])
        habit_rows += f'<tr><td class="habit-name-sm">{h}</td>{cells}</tr>'
    header_cells = ''.join([f'<th>{d[:3]}</th>' for d in dias])
    content = f'''<h1 class="page-title">Hábitos da Semana</h1>
    <div class="week-field"><label class="field-label-inline">Semana:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <table class="table habit-weekly-table" style="margin-top:14px;">
      <thead><tr><th style="width:22%;">Hábito</th>{header_cells}</tr></thead>
      <tbody>{habit_rows}
        <tr><td class="habit-name-sm"><div class="write-line"></div></td>{''.join(['<td><div class="tracker-cell-sm"></div></td>' for _ in range(7)])}</tr>
        <tr><td class="habit-name-sm"><div class="write-line"></div></td>{''.join(['<td><div class="tracker-cell-sm"></div></td>' for _ in range(7)])}</tr>
      </tbody>
    </table>
    <div style="margin-top:16px;">
      <div class="subsection-title">Hábito que mais quero manter:</div>
      <div class="write-line"></div>
      <div style="margin-top:10px;"><div class="subsection-title">Recompensa por manter a semana completa:</div>
      <div class="write-line"></div></div>
    </div>'''
    pages.append(page_wrap(50, content, "Semanal", "50"))

    # P51: Planejamento de Energia Semanal
    content = '''<h1 class="page-title">Energia da Semana</h1>
    <p class="page-subtitle">Planeje atividades de acordo com sua energia prevista. Não agende tarefas pesadas em dias ruins.</p>
    <div class="energy-week">''' + ''.join([f'''
      <div class="energy-day">
        <div class="energy-day-name">{d}</div>
        <div class="energy-bar-container">
          <div class="energy-level">Energia prevista: <span class="energy-dots">○ ○ ○ ○ ○</span></div>
        </div>
        <div class="energy-plan"><label class="field-label-inline">Tarefa principal:</label><div class="write-line"></div></div>
      </div>''' for d in dias]) + '''
    </div>'''
    pages.append(page_wrap(51, content, "Semanal", "51"))

    return pages
