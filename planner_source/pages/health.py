# -*- coding: utf-8 -*-
"""Secao 9: Saude (paginas 88-99)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers import page_wrap, checkbox, write_lines, field


def get_pages():
    pages = []

    # P88: Controle de Medicamentos
    content = '''<h1 class="page-title">Controle de Medicamentos</h1>
    <p class="page-subtitle">Manter a medicação em dia é especialmente desafiador com TDAH. Use esta página como âncora.</p>
    <table class="table" style="margin-top:12px;">
      <thead><tr><th style="width:25%;">Medicamento</th><th style="width:15%;">Dosagem</th><th style="width:15%;">Horário</th><th style="width:15%;">Com quê</th><th style="width:30%;">Observações</th></tr></thead>
      <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(6)]) + '''
      </tbody>
    </table>
    <div style="margin-top:16px;">
      <div class="subsection-title">Registro Mensal — Tomei?</div>
      <div class="med-grid">
        <div class="med-header">''' + ''.join([f'<div class="med-day">{i}</div>' for i in range(1,32)]) + '''</div>
        <div class="med-row"><div class="med-name">Med 1</div>''' + ''.join(['<div class="tracker-cell"></div>' for _ in range(31)]) + '''</div>
        <div class="med-row"><div class="med-name">Med 2</div>''' + ''.join(['<div class="tracker-cell"></div>' for _ in range(31)]) + '''</div>
        <div class="med-row"><div class="med-name">Med 3</div>''' + ''.join(['<div class="tracker-cell"></div>' for _ in range(31)]) + '''</div>
      </div>
    </div>
    <div style="margin-top:12px;">
      <div class="subsection-title">Próxima receita / renovação</div>
      <div class="write-line"></div>
    </div>'''
    pages.append(page_wrap(88, content, "Saúde", "88"))

    # P89: Controle de Consultas
    content = '''<h1 class="page-title">Agenda de Consultas</h1>
    <table class="table" style="margin-top:12px;">
      <thead><tr><th style="width:15%;">Data</th><th style="width:15%;">Hora</th><th style="width:20%;">Profissional</th><th style="width:20%;">Especialidade</th><th style="width:30%;">Observações / Perguntar</th></tr></thead>
      <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(12)]) + '''
      </tbody>
    </table>
    <div style="margin-top:16px;">
      <div class="subsection-title">Antes da Consulta — Preparar</div>
      ''' + '\n'.join([checkbox("_"*48) for _ in range(4)]) + '''
    </div>
    <div style="margin-top:12px;">
      <div class="subsection-title">Informações Importantes</div>
      <div class="grid-2">
        <div>''' + field("Convênio") + field("Número carteirinha") + '''</div>
        <div>''' + field("Farmácia preferida") + field("Contato emergência") + '''</div>
      </div>
    </div>'''
    pages.append(page_wrap(89, content, "Saúde", "89"))

    # P90: Controle de Alimentacao
    content = '''<h1 class="page-title">Registro Alimentar</h1>
    <div class="daily-header-fields"><label class="field-label-inline">Data:</label><div class="write-line" style="width:180px;display:inline-block;"></div></div>
    <div class="meals-grid" style="margin-top:14px;">
      <div class="meal-card">
        <div class="meal-header"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6" stroke="#2563EB" stroke-width="1.2"/><path d="M8 4v4" stroke="#2563EB" stroke-width="1.2" stroke-linecap="round"/></svg> Café da Manhã</div>
        <div><label class="field-label-inline">Hora:</label><div class="write-line" style="width:60px;display:inline-block;"></div></div>
        ''' + write_lines(3, dotted=True) + '''
      </div>
      <div class="meal-card">
        <div class="meal-header"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6" stroke="#2563EB" stroke-width="1.2"/><path d="M8 4v4h3" stroke="#2563EB" stroke-width="1.2" stroke-linecap="round"/></svg> Almoço</div>
        <div><label class="field-label-inline">Hora:</label><div class="write-line" style="width:60px;display:inline-block;"></div></div>
        ''' + write_lines(3, dotted=True) + '''
      </div>
      <div class="meal-card">
        <div class="meal-header"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6" stroke="#2563EB" stroke-width="1.2"/><path d="M5 8h6" stroke="#2563EB" stroke-width="1.2" stroke-linecap="round"/></svg> Lanche</div>
        <div><label class="field-label-inline">Hora:</label><div class="write-line" style="width:60px;display:inline-block;"></div></div>
        ''' + write_lines(2, dotted=True) + '''
      </div>
      <div class="meal-card">
        <div class="meal-header"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6" stroke="#2563EB" stroke-width="1.2"/><path d="M8 12V8h-3" stroke="#2563EB" stroke-width="1.2" stroke-linecap="round"/></svg> Jantar</div>
        <div><label class="field-label-inline">Hora:</label><div class="write-line" style="width:60px;display:inline-block;"></div></div>
        ''' + write_lines(3, dotted=True) + '''
      </div>
    </div>
    <div class="grid-2" style="margin-top:12px;">
      <div><label class="field-label-inline">Água (copos):</label> ○ ○ ○ ○ ○ ○ ○ ○</div>
      <div><label class="field-label-inline">Como me senti:</label><div class="write-line" style="display:inline-block;width:100px;"></div></div>
    </div>'''
    pages.append(page_wrap(90, content, "Saúde", "90"))

    # P91: Water Tracker
    water_rows = ''.join([f'''<div class="water-row">
      <div class="water-day">{i}</div>
      <div class="water-glasses">''' + ''.join(['<div class="water-glass"></div>' for _ in range(10)]) + '''</div>
    </div>''' for i in range(1, 32)])
    content = f'''<h1 class="page-title">Rastreador de Hidratação</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:150px;display:inline-block;"></div></div>
    <p class="page-subtitle" style="margin-top:8px;">Cada ○ = 1 copo (250ml). Meta recomendada: 8 copos/dia. Preencha conforme beber.</p>
    <div class="water-tracker" style="margin-top:10px;">
      <div class="water-header"><div class="water-day" style="font-weight:600;">Dia</div><div class="water-glasses" style="font-weight:600;font-size:8pt;">1 &nbsp; 2 &nbsp; 3 &nbsp; 4 &nbsp; 5 &nbsp; 6 &nbsp; 7 &nbsp; 8 &nbsp; 9 &nbsp; 10</div></div>
      {water_rows}
    </div>'''
    pages.append(page_wrap(91, content, "Saúde", "91"))

    # P92: Exercise Tracker
    content = '''<h1 class="page-title">Registro de Exercícios</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:150px;display:inline-block;"></div></div>
    <table class="table" style="margin-top:12px;">
      <thead><tr><th style="width:10%;">Dia</th><th style="width:30%;">Atividade</th><th style="width:15%;">Duração</th><th style="width:15%;">Intensidade</th><th style="width:30%;">Como me senti depois</th></tr></thead>
      <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(16)]) + '''
      </tbody>
    </table>
    <div class="grid-2" style="margin-top:12px;">
      <div><label class="field-label-inline">Total de dias ativos:</label><div class="write-line" style="width:60px;display:inline-block;"></div></div>
      <div><label class="field-label-inline">Meta do mês:</label><div class="write-line" style="width:60px;display:inline-block;"></div> dias</div>
    </div>'''
    pages.append(page_wrap(92, content, "Saúde", "92"))

    # P93: Registro de Crises
    content = '''<h1 class="page-title">Registro de Crises</h1>
    <p class="page-subtitle">Registrar crises ajuda a identificar padrões e gatilhos. Não para julgar — para entender.</p>
    <div class="crisis-entry" style="margin-top:12px;">
      <div class="grid-3">
        <div>''' + field("Data") + '''</div>
        <div>''' + field("Hora") + '''</div>
        <div>''' + field("Intensidade (1-10)") + '''</div>
      </div>
      <div style="margin-top:10px;">''' + field("O que aconteceu antes (gatilho)") + '''</div>
      <div style="margin-top:8px;">
        <label class="field-label">O que senti (corpo e mente)</label>
        <div class="write-area" style="min-height:40px;"></div>
      </div>
      <div style="margin-top:8px;">
        <label class="field-label">O que fiz para lidar</label>
        <div class="write-area" style="min-height:35px;"></div>
      </div>
      <div style="margin-top:8px;">''' + field("Funcionou? (sim/parcial/não)") + '''</div>
      <div style="margin-top:8px;">''' + field("O que faria diferente na próxima vez") + '''</div>
    </div>
    <div class="divider" style="margin:16px 0;"></div>
    <div class="crisis-entry">
      <div class="grid-3">
        <div>''' + field("Data") + '''</div>
        <div>''' + field("Hora") + '''</div>
        <div>''' + field("Intensidade (1-10)") + '''</div>
      </div>
      <div style="margin-top:10px;">''' + field("Gatilho") + '''</div>
      <div style="margin-top:8px;">
        <label class="field-label">O que senti</label>
        <div class="write-area" style="min-height:35px;"></div>
      </div>
      <div style="margin-top:8px;">''' + field("Estratégia usada") + '''</div>
      <div style="margin-top:8px;">''' + field("Resultado") + '''</div>
    </div>'''
    pages.append(page_wrap(93, content, "Saúde", "93"))

    # P94: Plano Emergencial
    content = '''<h1 class="page-title">Plano para Dias Difíceis</h1>
    <p class="page-subtitle">Preencha esta página quando estiver bem. Consulte quando estiver em crise.</p>
    <div class="emergency-plan">
      <div class="card card-blue" style="margin-bottom:12px;">
        <div class="card-header">Sinais de que estou desregulado(a):</div>
        ''' + '\n'.join([checkbox("_"*46) for _ in range(4)]) + '''
      </div>
      <div class="card" style="margin-bottom:12px;">
        <div class="card-header">Coisas que me acalmam (comprovadas):</div>
        <div class="grid-2">
          <div>''' + '\n'.join([checkbox("_"*20) for _ in range(4)]) + '''</div>
          <div>''' + '\n'.join([checkbox("_"*20) for _ in range(4)]) + '''</div>
        </div>
      </div>
      <div class="card" style="margin-bottom:12px;">
        <div class="card-header">Pessoas que posso ligar:</div>
        <div class="grid-2">''' + ''.join([f'<div>{field("Nome")} {field("Telefone")}</div>' for _ in range(2)]) + '''</div>
      </div>
      <div class="card">
        <div class="card-header">Frase que preciso ouvir de mim mesmo(a):</div>
        <div class="write-area" style="min-height:40px;"></div>
      </div>
    </div>'''
    pages.append(page_wrap(94, content, "Saúde", "94"))

    # P95: Autocuidado
    content = '''<h1 class="page-title">Meu Plano de Autocuidado</h1>
    <div class="selfcare-grid">
      <div class="selfcare-section">
        <div class="subsection-title"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" style="vertical-align:middle;margin-right:4px;"><path d="M7 1l1.5 3h3l-2.5 2 1 3L7 7.5 4 9l1-3-2.5-2h3z" stroke="#2563EB" stroke-width="1" fill="none"/></svg>Corpo</div>
        ''' + '\n'.join([checkbox("_"*36) for _ in range(5)]) + '''
      </div>
      <div class="selfcare-section">
        <div class="subsection-title"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" style="vertical-align:middle;margin-right:4px;"><circle cx="7" cy="7" r="5" stroke="#2563EB" stroke-width="1" fill="none"/><path d="M5 7h4M7 5v4" stroke="#2563EB" stroke-width="1" stroke-linecap="round"/></svg>Mente</div>
        ''' + '\n'.join([checkbox("_"*36) for _ in range(5)]) + '''
      </div>
      <div class="selfcare-section">
        <div class="subsection-title"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" style="vertical-align:middle;margin-right:4px;"><path d="M7 3C5 1 2 2 2 5c0 4 5 6 5 6s5-2 5-6c0-3-3-4-5-2z" stroke="#2563EB" stroke-width="1" fill="none"/></svg>Emocional</div>
        ''' + '\n'.join([checkbox("_"*36) for _ in range(5)]) + '''
      </div>
      <div class="selfcare-section">
        <div class="subsection-title"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" style="vertical-align:middle;margin-right:4px;"><circle cx="7" cy="5" r="3" stroke="#2563EB" stroke-width="1" fill="none"/><path d="M2 13c0-3 2-5 5-5s5 2 5 5" stroke="#2563EB" stroke-width="1" fill="none"/></svg>Social</div>
        ''' + '\n'.join([checkbox("_"*36) for _ in range(5)]) + '''
      </div>
    </div>
    <div style="margin-top:14px;">
      <div class="subsection-title">Meu compromisso comigo esta semana:</div>
      <div class="write-area" style="min-height:40px;"></div>
    </div>'''
    pages.append(page_wrap(95, content, "Saúde", "95"))

    # P96: Registro de Ansiedade
    content = '''<h1 class="page-title">Registro de Ansiedade</h1>
    <p class="page-subtitle">Anotar o que sente reduz a intensidade. O cérebro processa melhor o que é nomeado.</p>
    <div class="anxiety-entries">''' + ''.join([f'''
      <div class="anxiety-entry">
        <div class="grid-4">
          <div><label class="field-label">Data</label><div class="write-line"></div></div>
          <div><label class="field-label">Hora</label><div class="write-line"></div></div>
          <div><label class="field-label">Nível (1-10)</label><div class="write-line"></div></div>
          <div><label class="field-label">Duração</label><div class="write-line"></div></div>
        </div>
        <div class="grid-2" style="margin-top:6px;">
          <div><label class="field-label">Gatilho</label><div class="write-line"></div></div>
          <div><label class="field-label">O que fiz</label><div class="write-line"></div></div>
        </div>
      </div>''' for _ in range(5)]) + '''
    </div>'''
    pages.append(page_wrap(96, content, "Saúde", "96"))

    # P97: Controle de Hiperfoco
    content = '''<h1 class="page-title">Controle de Hiperfoco</h1>
    <p class="page-subtitle">O hiperfoco é um superpoder — mas sem controle, drena energia e atrasa tudo mais.</p>
    <table class="table" style="margin-top:12px;">
      <thead><tr><th style="width:12%;">Data</th><th style="width:25%;">No que hiperfoquei</th><th style="width:12%;">Duração</th><th style="width:20%;">Deixei de fazer</th><th style="width:15%;">Valeu a pena?</th><th style="width:16%;">Próx. vez</th></tr></thead>
      <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(10)]) + '''
      </tbody>
    </table>
    <div class="card card-blue" style="margin-top:14px;">
      <div class="card-header">Estratégias para gerenciar hiperfoco:</div>
      <div class="grid-2" style="margin-top:6px;">
        <div>''' + '\n'.join([checkbox(x) for x in ["Timer de 90 min (alarme alto)","Lembrete visual na mesa","Pedir para alguém me chamar"]]) + '''</div>
        <div>''' + '\n'.join([checkbox(x) for x in ["Anotar e voltar depois","Definir ponto de parada ANTES","Recompensa ao parar no horário"]]) + '''</div>
      </div>
    </div>'''
    pages.append(page_wrap(97, content, "Saúde", "97"))

    # P98: Sintomas TDAH
    content = '''<h1 class="page-title">Registro de Sintomas</h1>
    <p class="page-subtitle">Acompanhe como seus sintomas variam. Leve para sua consulta.</p>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:150px;display:inline-block;"></div></div>
    <table class="table" style="margin-top:12px;font-size:9pt;">
      <thead><tr><th style="width:30%;">Sintoma</th><th colspan="4" style="text-align:center;">Frequência esta semana</th></tr>
      <tr><th></th><th>Sem 1</th><th>Sem 2</th><th>Sem 3</th><th>Sem 4</th></tr></thead>
      <tbody>''' + ''.join([f'<tr><td>{s}</td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for s in [
        "Dificuldade de foco","Esquecimentos","Procrastinação","Impulsividade",
        "Inquietação","Dificuldade para dormir","Desregulação emocional",
        "Hiperfoco não produtivo","Dificuldade em iniciar tarefas","Perda de objetos",
        "Dificuldade em esperar","Interrupção de outros"
    ]]) + '''
      </tbody>
    </table>
    <div style="margin-top:12px;">
      <div class="subsection-title">Observações para o médico:</div>
      ''' + write_lines(3) + '''
    </div>'''
    pages.append(page_wrap(98, content, "Saúde", "98"))

    # P99: Regulacao Emocional
    content = '''<h1 class="page-title">Técnicas de Regulação Emocional</h1>
    <p class="page-subtitle">Quando a emoção vem forte, é difícil pensar. Tenha este repertório pronto.</p>
    <div class="regulation-grid">
      <div class="reg-card">
        <div class="reg-title">Grounding 5-4-3-2-1</div>
        <div class="reg-steps">
          <div>5 coisas que <strong>vejo</strong></div>
          <div>4 coisas que <strong>toco</strong></div>
          <div>3 coisas que <strong>ouço</strong></div>
          <div>2 coisas que <strong>cheiro</strong></div>
          <div>1 coisa que <strong>saboreio</strong></div>
        </div>
      </div>
      <div class="reg-card">
        <div class="reg-title">Respiração 4-7-8</div>
        <div class="reg-steps">
          <div>Inspire por <strong>4</strong> segundos</div>
          <div>Segure por <strong>7</strong> segundos</div>
          <div>Expire por <strong>8</strong> segundos</div>
          <div>Repita <strong>4</strong> vezes</div>
        </div>
      </div>
      <div class="reg-card">
        <div class="reg-title">TIPP (DBT)</div>
        <div class="reg-steps">
          <div><strong>T</strong>emperatura — água gelada no rosto</div>
          <div><strong>I</strong>ntensidade — exercício intenso 5 min</div>
          <div><strong>P</strong>ace — respiração ritmada</div>
          <div><strong>P</strong>rogressive — relaxamento muscular</div>
        </div>
      </div>
      <div class="reg-card">
        <div class="reg-title">Minhas Estratégias</div>
        ''' + write_lines(5, dotted=True) + '''
      </div>
    </div>'''
    pages.append(page_wrap(99, content, "Saúde", "99"))

    return pages
