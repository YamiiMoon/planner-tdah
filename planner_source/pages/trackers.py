# -*- coding: utf-8 -*-
"""Secao 7: Trackers (paginas 64-77)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers import page_wrap, checkbox, write_lines, field


def get_pages():
    pages = []
    days_header = ''.join([f'<div class="tracker-day-num">{i}</div>' for i in range(1,32)])

    # P64: Habit Tracker Mensal
    habits = ["","","","","","","","","","","",""]
    rows = ""
    for i in range(12):
        cells = ''.join(['<div class="tracker-cell"></div>' for _ in range(31)])
        rows += f'<div class="tracker-row"><div class="habit-name"></div>{cells}</div>\n'
    content = f'''<h1 class="page-title">Rastreador de Hábitos</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <div class="tracker-container" style="margin-top:14px;">
      <div class="tracker-header"><div class="habit-name" style="font-weight:600;">Hábito</div>{days_header}</div>
      {rows}
    </div>
    <div class="tip-box" style="margin-top:12px;">
      <strong>Dica:</strong> Comece com no máximo 3 hábitos. Adicione novos somente quando os primeiros estiverem automáticos.
    </div>'''
    pages.append(page_wrap(64, content, "Trackers", "64"))

    # P65: Habit Tracker Semanal (layout diferente)
    dias = ["Seg","Ter","Qua","Qui","Sex","Sáb","Dom"]
    habit_rows = ""
    for i in range(8):
        cells = ''.join([f'<td><div class="tracker-cell-lg"></div></td>' for _ in range(7)])
        habit_rows += f'<tr><td class="habit-name-cell"></td>{cells}</tr>'
    header_cells = ''.join([f'<th>{d}</th>' for d in dias])
    content = f'''<h1 class="page-title">Hábitos da Semana</h1>
    <div class="week-field"><label class="field-label-inline">Semana de:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <table class="table tracker-weekly" style="margin-top:14px;">
      <thead><tr><th style="width:22%;">Hábito</th>{header_cells}</tr></thead>
      <tbody>{habit_rows}</tbody>
    </table>
    <div style="margin-top:16px;">
      <div class="subsection-title">Reflexão</div>
      <div class="grid-2">
        <div><label class="field-label-inline">Hábito mais difícil:</label><div class="write-line"></div></div>
        <div><label class="field-label-inline">Hábito mais fácil:</label><div class="write-line"></div></div>
      </div>
      <div style="margin-top:8px;"><label class="field-label-inline">O que posso ajustar?</label><div class="write-line"></div></div>
    </div>'''
    pages.append(page_wrap(65, content, "Trackers", "65"))

    # P66: Mood Tracker
    mood_rows = ''.join([f'''<div class="mood-row">
      <div class="mood-day">{i}</div>
      <div class="mood-scale">
        <div class="mood-dot" title="Péssimo"></div>
        <div class="mood-dot" title="Ruim"></div>
        <div class="mood-dot" title="Neutro"></div>
        <div class="mood-dot" title="Bom"></div>
        <div class="mood-dot" title="Ótimo"></div>
      </div>
      <div class="mood-note"><div class="write-line"></div></div>
    </div>''' for i in range(1, 32)])
    content = f'''<h1 class="page-title">Rastreador de Humor</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <div class="mood-legend" style="margin-top:10px;">
      <span class="mood-legend-item">● Péssimo</span>
      <span class="mood-legend-item">● Ruim</span>
      <span class="mood-legend-item">● Neutro</span>
      <span class="mood-legend-item">● Bom</span>
      <span class="mood-legend-item">● Ótimo</span>
    </div>
    <div class="mood-tracker" style="margin-top:10px;">
      <div class="mood-header"><div class="mood-day" style="font-weight:600;">Dia</div><div class="mood-scale" style="font-weight:600;">Humor</div><div class="mood-note" style="font-weight:600;">Nota / Gatilho</div></div>
      {mood_rows}
    </div>'''
    pages.append(page_wrap(66, content, "Trackers", "66"))

    # P67: Energy Tracker
    energy_bars = ''.join([f'''<div class="energy-row">
      <div class="energy-day">{i}</div>
      <div class="energy-bar-container">
        <div class="energy-bar-bg"></div>
      </div>
    </div>''' for i in range(1, 32)])
    content = f'''<h1 class="page-title">Rastreador de Energia</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <p class="page-subtitle" style="margin-top:8px;">Preencha a barra até o nível de energia do dia (1-10). Identifique padrões.</p>
    <div class="energy-scale-header" style="margin-top:10px;">
      <span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span><span>9</span><span>10</span>
    </div>
    <div class="energy-tracker">{energy_bars}</div>
    <div style="margin-top:12px;">
      <div class="subsection-title">Padrões que percebi:</div>
      ''' + write_lines(2) + '''
    </div>'''
    pages.append(page_wrap(67, content, "Trackers", "67"))

    # P68: Sleep Tracker
    sleep_rows = ''.join([f'''<tr>
      <td>{i}</td><td><div class="write-line"></div></td><td><div class="write-line"></div></td>
      <td><div class="write-line"></div></td><td><div class="sleep-quality"><div class="sq-dot"></div><div class="sq-dot"></div><div class="sq-dot"></div><div class="sq-dot"></div><div class="sq-dot"></div></div></td>
    </tr>''' for i in range(1, 32)])
    content = f'''<h1 class="page-title">Rastreador de Sono</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <table class="table sleep-table" style="margin-top:12px;">
      <thead><tr><th>Dia</th><th>Dormi</th><th>Acordei</th><th>Horas</th><th>Qualidade (1-5)</th></tr></thead>
      <tbody>{sleep_rows}</tbody>
    </table>'''
    pages.append(page_wrap(68, content, "Trackers", "68"))

    # P69: Water Tracker
    water_days = ''.join([f'''<div class="water-day">
      <div class="water-day-num">{i}</div>
      <div class="water-glasses">''' + ''.join(['<div class="water-glass"></div>' for _ in range(8)]) + '''</div>
    </div>''' for i in range(1, 32)])
    content = f'''<h1 class="page-title">Rastreador de Hidratação</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <p class="page-subtitle" style="margin-top:8px;">Meta: 8 copos por dia (≈ 2L). Preencha cada copo ao beber.</p>
    <div class="water-tracker" style="margin-top:12px;">{water_days}</div>
    <div class="tip-box" style="margin-top:12px;">
      <strong>Dica TDAH:</strong> Deixe uma garrafa visível no seu campo de visão. Se não vê, esquece.
    </div>'''
    pages.append(page_wrap(69, content, "Trackers", "69"))

    # P70: Medication Tracker
    med_rows = ''.join([f'<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="checkbox" style="margin:auto;"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(10)])
    content = f'''<h1 class="page-title">Controle de Medicamentos</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <div class="subsection-title" style="margin-top:14px;">Medicamentos Atuais</div>
    <table class="table" style="margin-top:8px;">
      <thead><tr><th>Medicamento</th><th>Dose</th><th>Horário</th><th>Tomei</th><th>Observação</th></tr></thead>
      <tbody>{med_rows}</tbody>
    </table>
    <div style="margin-top:16px;">
      <div class="subsection-title">Efeitos Observados</div>
      ''' + write_lines(3) + '''
    </div>
    <div style="margin-top:12px;">
      <div class="subsection-title">Próxima Consulta</div>
      <div class="grid-3">
        <div><label class="field-label">Data</label><div class="write-line"></div></div>
        <div><label class="field-label">Médico</label><div class="write-line"></div></div>
        <div><label class="field-label">Perguntar</label><div class="write-line"></div></div>
      </div>
    </div>'''
    pages.append(page_wrap(70, content, "Trackers", "70"))

    # P71: Exercise Tracker
    ex_rows = ''.join([f'''<tr>
      <td>{i}</td><td><div class="write-line"></div></td><td><div class="write-line"></div></td>
      <td><div class="write-line"></div></td><td><div class="mood-scale-mini"><div class="sq-dot"></div><div class="sq-dot"></div><div class="sq-dot"></div><div class="sq-dot"></div><div class="sq-dot"></div></div></td>
    </tr>''' for i in range(1, 32)])
    content = f'''<h1 class="page-title">Rastreador de Exercícios</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <table class="table" style="margin-top:12px;font-size:9pt;">
      <thead><tr><th>Dia</th><th>Atividade</th><th>Duração</th><th>Intensidade</th><th>Como me senti</th></tr></thead>
      <tbody>{ex_rows}</tbody>
    </table>
    <div style="margin-top:12px;">
      <div class="subsection-title">Meta do Mês</div>
      <div class="grid-2">
        <div><label class="field-label-inline">Frequência:</label><div class="write-line"></div></div>
        <div><label class="field-label-inline">Tipo preferido:</label><div class="write-line"></div></div>
      </div>
    </div>'''
    pages.append(page_wrap(71, content, "Trackers", "71"))

    # P72: Habit Tracker Minimalista (3o modelo)
    content = '''<h1 class="page-title">30 Dias de Um Hábito</h1>
    <p class="page-subtitle">Foque em UM hábito por 30 dias. Um de cada vez é como se constroem mudanças duradouras.</p>
    <div class="single-habit">
      <div class="field-group"><label class="field-label">Meu hábito:</label><div class="write-line"></div></div>
      <div class="grid-3" style="margin-top:8px;">
        <div><label class="field-label-inline">Gatilho:</label><div class="write-line"></div></div>
        <div><label class="field-label-inline">Recompensa:</label><div class="write-line"></div></div>
        <div><label class="field-label-inline">Início:</label><div class="write-line"></div></div>
      </div>
    </div>
    <div class="thirty-day-grid" style="margin-top:16px;">''' + ''.join([f'''
      <div class="day-circle"><span class="day-num">{i}</span></div>''' for i in range(1, 31)]) + '''
    </div>
    <div style="margin-top:16px;">
      <div class="grid-2">
        <div>
          <div class="subsection-title">Semana 1 - Como foi?</div>
          ''' + write_lines(2) + '''
        </div>
        <div>
          <div class="subsection-title">Semana 2 - Ajustes</div>
          ''' + write_lines(2) + '''
        </div>
      </div>
      <div class="grid-2" style="margin-top:12px;">
        <div>
          <div class="subsection-title">Semana 3 - Padrões</div>
          ''' + write_lines(2) + '''
        </div>
        <div>
          <div class="subsection-title">Semana 4 - Resultado</div>
          ''' + write_lines(2) + '''
        </div>
      </div>
    </div>'''
    pages.append(page_wrap(72, content, "Trackers", "72"))

    # P73-77: Additional trackers will continue in next sections
    # P73: Tracker de Leitura Mensal
    book_rows = ''.join([f'<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="progress-bar-empty"></div></td></tr>' for _ in range(8)])
    content = f'''<h1 class="page-title">Rastreador de Leitura</h1>
    <div class="month-field"><label class="field-label-inline">Mês / Período:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <table class="table" style="margin-top:14px;">
      <thead><tr><th style="width:35%">Título</th><th style="width:25%">Autor</th><th style="width:15%">Páginas</th><th style="width:25%">Progresso</th></tr></thead>
      <tbody>{book_rows}</tbody>
    </table>
    <div style="margin-top:16px;">
      <div class="subsection-title">Lista de Próximas Leituras</div>
      ''' + '\n'.join([checkbox("_" * 50) for _ in range(5)]) + '''
    </div>
    <div style="margin-top:12px;">
      <div class="subsection-title">Anotações / Citações</div>
      ''' + write_lines(4, dotted=True) + '''
    </div>'''
    pages.append(page_wrap(73, content, "Trackers", "73"))

    # P74: Alimentacao Tracker
    content = '''<h1 class="page-title">Registro Alimentar</h1>
    <div class="daily-header-fields"><label class="field-label-inline">Data:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <div class="meals-grid" style="margin-top:14px;">
      <div class="meal-card">
        <div class="meal-header">☀ Café da Manhã</div>
        <div class="grid-2"><div><label class="field-label-inline">Hora:</label><div class="write-line"></div></div><div><label class="field-label-inline">Fome (1-5):</label><div class="write-line"></div></div></div>
        ''' + write_lines(2, dotted=True) + '''
      </div>
      <div class="meal-card">
        <div class="meal-header">☼ Almoço</div>
        <div class="grid-2"><div><label class="field-label-inline">Hora:</label><div class="write-line"></div></div><div><label class="field-label-inline">Fome (1-5):</label><div class="write-line"></div></div></div>
        ''' + write_lines(2, dotted=True) + '''
      </div>
      <div class="meal-card">
        <div class="meal-header">◑ Lanche</div>
        <div class="grid-2"><div><label class="field-label-inline">Hora:</label><div class="write-line"></div></div><div><label class="field-label-inline">Fome (1-5):</label><div class="write-line"></div></div></div>
        ''' + write_lines(2, dotted=True) + '''
      </div>
      <div class="meal-card">
        <div class="meal-header">☾ Jantar</div>
        <div class="grid-2"><div><label class="field-label-inline">Hora:</label><div class="write-line"></div></div><div><label class="field-label-inline">Fome (1-5):</label><div class="write-line"></div></div></div>
        ''' + write_lines(2, dotted=True) + '''
      </div>
    </div>
    <div style="margin-top:12px;">
      <div class="grid-2">
        <div><label class="field-label-inline">Água (copos):</label><div class="write-line"></div></div>
        <div><label class="field-label-inline">Energia pós-refeição:</label><div class="write-line"></div></div>
      </div>
    </div>'''
    pages.append(page_wrap(74, content, "Trackers", "74"))

    # P75: Tracker Tela / Digital
    content = '''<h1 class="page-title">Tempo de Tela</h1>
    <p class="page-subtitle">Monitore quanto tempo gasta em cada app. TDAH e scrolling infinito não combinam bem.</p>
    <div class="month-field"><label class="field-label-inline">Semana:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <table class="table" style="margin-top:14px;">
      <thead><tr><th style="width:25%">App/Site</th><th>Seg</th><th>Ter</th><th>Qua</th><th>Qui</th><th>Sex</th><th>Sáb</th><th>Dom</th><th>Total</th></tr></thead>
      <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td>' + ''.join(['<td><div class="write-line"></div></td>' for _ in range(8)]) + '</tr>' for _ in range(7)]) + '''
      </tbody>
    </table>
    <div style="margin-top:12px;">
      <div class="grid-2">
        <div><label class="field-label-inline">Limite diário ideal:</label><div class="write-line"></div></div>
        <div><label class="field-label-inline">App mais problemático:</label><div class="write-line"></div></div>
      </div>
      <div style="margin-top:8px;"><label class="field-label-inline">Estratégia para reduzir:</label><div class="write-line"></div></div>
    </div>'''
    pages.append(page_wrap(75, content, "Trackers", "75"))

    # P76: Tracker Menstrual / Ciclo (inclusivo)
    content = '''<h1 class="page-title">Rastreador de Ciclo</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <p class="page-subtitle" style="margin-top:6px;">Hormônios influenciam diretamente foco e energia. Conhecer seu ciclo ajuda a planejar melhor.</p>
    <div class="cycle-grid" style="margin-top:12px;">''' + ''.join([f'''
      <div class="cycle-day"><div class="cycle-num">{i}</div><div class="cycle-mark"></div></div>''' for i in range(1, 32)]) + '''
    </div>
    <div class="grid-2" style="margin-top:16px;gap:16px;">
      <div>
        <div class="subsection-title">Sintomas Físicos</div>
        ''' + '\n'.join([checkbox(s) for s in ["Cólica","Dor de cabeça","Fadiga","Inchaço","Insônia"]]) + '''
      </div>
      <div>
        <div class="subsection-title">Sintomas Emocionais</div>
        ''' + '\n'.join([checkbox(s) for s in ["Irritabilidade","Ansiedade","Choro fácil","Baixa motivação","Hiperfoco intenso"]]) + '''
      </div>
    </div>
    <div style="margin-top:12px;"><label class="field-label-inline">Notas:</label>''' + write_lines(2) + '''</div>'''
    pages.append(page_wrap(76, content, "Trackers", "76"))

    # P77: Gratitude Tracker
    content = '''<h1 class="page-title">Gratidão Diária</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <p class="page-subtitle" style="margin-top:6px;">3 coisas por dia. Pode ser pequeno. Pode ser simples. Apenas perceba.</p>
    <div class="gratitude-grid" style="margin-top:10px;">''' + ''.join([f'''
      <div class="gratitude-row">
        <div class="gratitude-day">{i}</div>
        <div class="gratitude-items">
          <div class="write-line-dotted"></div>
          <div class="write-line-dotted"></div>
          <div class="write-line-dotted"></div>
        </div>
      </div>''' for i in range(1, 16)]) + '''
    </div>'''
    pages.append(page_wrap(77, content, "Trackers", "77"))

    return pages
