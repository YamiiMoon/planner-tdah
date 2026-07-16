# -*- coding: utf-8 -*-
"""Secao 4: Planejamento Mensal (paginas 30-41)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers import page_wrap, checkbox, write_lines, field


def get_pages():
    pages = []

    # P30: Calendario Anual
    months = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho",
              "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
    month_grids = ""
    for m in months:
        month_grids += f'''<div class="mini-month">
        <div class="mini-month-name">{m}</div>
        <div class="mini-month-header"><span>S</span><span>T</span><span>Q</span><span>Q</span><span>S</span><span>S</span><span>D</span></div>
        <div class="mini-month-grid">''' + ''.join(['<div class="mini-day"></div>' for _ in range(35)]) + '''</div>
      </div>'''
    content = f'''<h1 class="page-title">Calendário Anual</h1>
    <div class="year-calendar">{month_grids}</div>'''
    pages.append(page_wrap(30, content, "Planejamento", "30"))

    # P31: Visao Mensal - Timeline
    content = '''<h1 class="page-title">Visão do Mês</h1>
    <div class="grid-2" style="gap:24px;">
      <div>
        <div class="subsection-title">Foco Principal</div>
        <div class="write-area" style="min-height:40px;"></div>
        <div style="margin-top:16px;">
          <div class="subsection-title">Intenção do Mês</div>
          <div class="write-line"></div>
        </div>
        <div style="margin-top:16px;">
          <div class="subsection-title">Compromissos Fixos</div>
          ''' + '\n'.join([checkbox(f"_{'_'*35}") for _ in range(6)]) + '''
        </div>
      </div>
      <div>
        <div class="subsection-title">Datas Importantes</div>
        <div class="dates-list">''' + ''.join([f'''
          <div class="date-row"><div class="date-box"></div><div class="write-line" style="flex:1;"></div></div>''' for _ in range(8)]) + '''
        </div>
        <div style="margin-top:16px;">
          <div class="subsection-title">Não Esquecer</div>
          ''' + '\n'.join([checkbox(f"_{'_'*35}") for _ in range(4)]) + '''
        </div>
      </div>
    </div>'''
    pages.append(page_wrap(31, content, "Planejamento Mensal", "31"))

    # P32: Calendario Mensal Grade
    days_header = '<div class="cal-header-row">' + ''.join([f'<div class="cal-day-name">{d}</div>' for d in ["SEG","TER","QUA","QUI","SEX","SÁB","DOM"]]) + '</div>'
    days_grid = '<div class="cal-grid">' + ''.join(['<div class="cal-cell"><div class="cal-cell-num"></div><div class="cal-cell-space"></div></div>' for _ in range(35)]) + '</div>'
    content = f'''<h1 class="page-title">Calendário Mensal</h1>
    <div class="month-field"><label class="field-label-inline">Mês / Ano:</label><div class="write-line" style="width:200px;display:inline-block;"></div></div>
    <div class="calendar-full">
      {days_header}
      {days_grid}
    </div>
    <div style="margin-top:12px;">
      <div class="subsection-title">Notas</div>
      ''' + write_lines(3) + '''
    </div>'''
    pages.append(page_wrap(32, content, "Planejamento Mensal", "32"))

    # P33: Metas do Mes
    content = '''<h1 class="page-title">Metas do Mês</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <div class="monthly-goals" style="margin-top:16px;">
      <div class="card card-blue" style="margin-bottom:16px;">
        <div class="card-header">Meta Principal do Mês</div>
        <div class="write-area" style="min-height:35px;"></div>
        <div style="margin-top:10px;"><label class="field-label-inline">Por que isso importa agora?</label><div class="write-line"></div></div>
      </div>
      <div class="grid-2" style="gap:12px;">
        <div class="card">
          <div class="card-header">Meta 2</div>
          <div class="write-line"></div>
          <div style="margin-top:8px;"><label class="field-label-inline">Primeiro passo:</label><div class="write-line"></div></div>
        </div>
        <div class="card">
          <div class="card-header">Meta 3</div>
          <div class="write-line"></div>
          <div style="margin-top:8px;"><label class="field-label-inline">Primeiro passo:</label><div class="write-line"></div></div>
        </div>
      </div>
      <div style="margin-top:16px;">
        <div class="subsection-title">Hábito que quero fortalecer este mês</div>
        <div class="write-line"></div>
      </div>
      <div style="margin-top:12px;">
        <div class="subsection-title">Uma coisa que vou PARAR de fazer</div>
        <div class="write-line"></div>
      </div>
    </div>'''
    pages.append(page_wrap(33, content, "Planejamento Mensal", "33"))

    # P34: Orcamento Mensal
    content = '''<h1 class="page-title">Orçamento Mensal</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:150px;display:inline-block;"></div></div>
    <div class="grid-2" style="gap:20px;margin-top:14px;">
      <div>
        <div class="subsection-title" style="color:#2563EB;">Receitas</div>
        <table class="table">
          <thead><tr><th style="width:65%">Fonte</th><th>Valor</th></tr></thead>
          <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(5)]) + '''
          <tr style="font-weight:600;"><td>TOTAL</td><td><div class="write-line"></div></td></tr>
          </tbody>
        </table>
      </div>
      <div>
        <div class="subsection-title" style="color:#64748B;">Despesas Fixas</div>
        <table class="table">
          <thead><tr><th style="width:65%">Item</th><th>Valor</th></tr></thead>
          <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(7)]) + '''
          <tr style="font-weight:600;"><td>TOTAL</td><td><div class="write-line"></div></td></tr>
          </tbody>
        </table>
      </div>
    </div>
    <div style="margin-top:14px;">
      <div class="grid-3" style="gap:16px;">
        <div class="summary-box"><div class="summary-label">Total Receitas</div><div class="write-line"></div></div>
        <div class="summary-box"><div class="summary-label">Total Despesas</div><div class="write-line"></div></div>
        <div class="summary-box"><div class="summary-label">Saldo</div><div class="write-line"></div></div>
      </div>
    </div>'''
    pages.append(page_wrap(34, content, "Finanças", "34"))

    # P35: Habitos do Mes Tracker
    habits = ["Beber 2L água", "Exercício", "Meditação", "Leitura",
              "Dormir até 23h", "Tomar remédio", "Sem redes 1h", ""]
    tracker_rows = ""
    for h in habits + ["", ""]:
        cells = ''.join(['<div class="tracker-cell"></div>' for _ in range(31)])
        tracker_rows += f'<div class="tracker-row"><div class="habit-name">{h}</div><div class="tracker-cells">{cells}</div></div>\n'
    numbers = '<div class="tracker-numbers"><div class="habit-name"></div><div class="tracker-cells">' + ''.join([f'<div class="tracker-num">{i}</div>' for i in range(1,32)]) + '</div></div>'
    content = f'''<h1 class="page-title">Rastreador de Hábitos</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:150px;display:inline-block;"></div></div>
    <div class="habit-tracker" style="margin-top:12px;">
      {numbers}
      {tracker_rows}
    </div>
    <div class="tip-box" style="margin-top:12px;">
      <strong>Lembrete:</strong> Não tente 10 hábitos novos de uma vez. Comece com 2-3 e adicione mais quando estes estiverem automáticos.
    </div>'''
    pages.append(page_wrap(35, content, "Rastreadores", "35"))

    # P36: Humor do Mes
    content = '''<h1 class="page-title">Humor do Mês</h1>
    <p class="page-subtitle">Marque seu humor dominante a cada dia. Padrões revelam gatilhos e ajudam no autoconhecimento.</p>
    <div class="mood-legend">
      <div class="mood-item"><div class="mood-circle mood-1"></div><span>Péssimo</span></div>
      <div class="mood-item"><div class="mood-circle mood-2"></div><span>Ruim</span></div>
      <div class="mood-item"><div class="mood-circle mood-3"></div><span>Neutro</span></div>
      <div class="mood-item"><div class="mood-circle mood-4"></div><span>Bom</span></div>
      <div class="mood-item"><div class="mood-circle mood-5"></div><span>Ótimo</span></div>
    </div>
    <div class="mood-grid">''' + ''.join([f'<div class="mood-day"><div class="mood-day-num">{i}</div><div class="mood-circle-empty"></div></div>' for i in range(1, 32)]) + '''
    </div>
    <div style="margin-top:16px;">
      <div class="subsection-title">Padrões que percebi</div>
      ''' + write_lines(3) + '''
    </div>'''
    pages.append(page_wrap(36, content, "Rastreadores", "36"))

    # P37: Energia do Mes
    content = '''<h1 class="page-title">Energia do Mês</h1>
    <p class="page-subtitle">Registre seu nível de energia (1-10) a cada dia. Identifique padrões e ajuste sua rotina.</p>
    <div class="energy-chart">
      <div class="energy-y-axis">''' + ''.join([f'<div class="energy-level">{i}</div>' for i in range(10, 0, -1)]) + '''</div>
      <div class="energy-grid">''' + ''.join([f'<div class="energy-col"><div class="energy-bar-space"></div><div class="energy-day-label">{i}</div></div>' for i in range(1, 32)]) + '''</div>
    </div>
    <div class="grid-2" style="margin-top:16px;gap:16px;">
      <div>
        <div class="subsection-title">Dias de alta energia — o que fiz diferente?</div>
        ''' + write_lines(2) + '''
      </div>
      <div>
        <div class="subsection-title">Dias de baixa energia — possíveis causas?</div>
        ''' + write_lines(2) + '''
      </div>
    </div>'''
    pages.append(page_wrap(37, content, "Rastreadores", "37"))

    # P38: Checklist Mensal
    content = '''<h1 class="page-title">Checklist Mensal</h1>
    <div class="grid-3" style="gap:16px;">
      <div>
        <div class="subsection-title" style="color:#2563EB;">Pessoal</div>
        ''' + '\n'.join([checkbox("_"*22) for _ in range(10)]) + '''
      </div>
      <div>
        <div class="subsection-title" style="color:#2563EB;">Trabalho</div>
        ''' + '\n'.join([checkbox("_"*22) for _ in range(10)]) + '''
      </div>
      <div>
        <div class="subsection-title" style="color:#2563EB;">Casa</div>
        ''' + '\n'.join([checkbox("_"*22) for _ in range(10)]) + '''
      </div>
    </div>'''
    pages.append(page_wrap(38, content, "Planejamento Mensal", "38"))

    # P39: Reflexao do Mes
    content = '''<h1 class="page-title">Reflexão do Mês</h1>
    <div class="reflection-questions">
      <div class="reflect-q">
        <div class="reflect-label">O que funcionou este mês?</div>
        <div class="write-area" style="min-height:50px;"></div>
      </div>
      <div class="reflect-q">
        <div class="reflect-label">O que não funcionou — e por quê?</div>
        <div class="write-area" style="min-height:50px;"></div>
      </div>
      <div class="reflect-q">
        <div class="reflect-label">Qual hábito consegui manter?</div>
        <div class="write-line"></div>
      </div>
      <div class="reflect-q">
        <div class="reflect-label">Do que me orgulho?</div>
        <div class="write-area" style="min-height:40px;"></div>
      </div>
      <div class="reflect-q">
        <div class="reflect-label">O que quero levar para o próximo mês?</div>
        ''' + write_lines(2) + '''
      </div>
      <div class="reflect-q">
        <div class="reflect-label">O que quero deixar para trás?</div>
        <div class="write-line"></div>
      </div>
    </div>'''
    pages.append(page_wrap(39, content, "Planejamento Mensal", "39"))

    # P40: Planejamento Proximo Mes
    content = '''<h1 class="page-title">Planejando o Próximo Mês</h1>
    <div class="next-month-plan">
      <div class="card card-blue" style="margin-bottom:14px;">
        <div class="card-header">Tema / Foco do Mês</div>
        <div class="write-line"></div>
      </div>
      <div class="grid-2" style="gap:14px;margin-bottom:14px;">
        <div class="card">
          <div class="card-header">3 Prioridades</div>
          ''' + checkbox("_"*30) + checkbox("_"*30) + checkbox("_"*30) + '''
        </div>
        <div class="card">
          <div class="card-header">Eventos / Datas</div>
          ''' + write_lines(4) + '''
        </div>
      </div>
      <div class="grid-2" style="gap:14px;">
        <div class="card">
          <div class="card-header">Hábito novo para testar</div>
          <div class="write-line"></div>
          <div style="margin-top:6px;"><label class="field-label-inline">Gatilho:</label><div class="write-line"></div></div>
          <div style="margin-top:6px;"><label class="field-label-inline">Recompensa:</label><div class="write-line"></div></div>
        </div>
        <div class="card">
          <div class="card-header">Ajustes na rotina</div>
          ''' + write_lines(4) + '''
        </div>
      </div>
    </div>'''
    pages.append(page_wrap(40, content, "Planejamento Mensal", "40"))

    # P41: Controle de Assinaturas
    content = '''<h1 class="page-title">Controle de Assinaturas</h1>
    <p class="page-subtitle">Serviços recorrentes que debitam automaticamente. Revise mensalmente — cancelar o que não usa é economia instantânea.</p>
    <table class="table" style="margin-top:12px;">
      <thead><tr><th>Serviço</th><th>Valor</th><th>Vencimento</th><th>Uso?</th><th>Manter?</th></tr></thead>
      <tbody>''' + ''.join([f'<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="checkbox" style="margin:auto;"></div></td><td><div class="checkbox" style="margin:auto;"></div></td></tr>' for _ in range(12)]) + '''
      </tbody>
    </table>
    <div class="grid-2" style="margin-top:14px;gap:16px;">
      <div class="summary-box"><div class="summary-label">Total Mensal em Assinaturas</div><div class="write-line"></div></div>
      <div class="summary-box"><div class="summary-label">Economia se cancelar desnecessárias</div><div class="write-line"></div></div>
    </div>'''
    pages.append(page_wrap(41, content, "Finanças", "41"))

    return pages
