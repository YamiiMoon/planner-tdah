# -*- coding: utf-8 -*-
"""Secao 6: Planejamento Diario (paginas 52-63)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers import page_wrap, checkbox, write_lines, field


def get_pages():
    pages = []

    # P52: Agenda Diaria Completa
    hours_block = ""
    for h in range(6, 23):
        hours_block += f'<div class="time-row"><div class="time-label">{h:02d}:00</div><div class="time-line"></div></div>\n'
    content = f'''<h1 class="page-title">Agenda Diária</h1>
    <div class="daily-header-fields">
      <div class="grid-3">
        <div><label class="field-label">Data</label><div class="write-line"></div></div>
        <div><label class="field-label">Dia da semana</label><div class="write-line"></div></div>
        <div><label class="field-label">Energia hoje (1-10)</label><div class="write-line"></div></div>
      </div>
    </div>
    <div class="daily-schedule" style="margin-top:12px;">
      {hours_block}
    </div>'''
    pages.append(page_wrap(52, content, "Diário", "52"))

    # P53: Planejamento do Dia - Top 3
    content = '''<h1 class="page-title">O Que Importa Hoje</h1>
    <div class="daily-header-fields">
      <div class="grid-2"><div><label class="field-label">Data</label><div class="write-line"></div></div><div><label class="field-label">Humor</label><div class="write-line"></div></div></div>
    </div>
    <div style="margin-top:20px;">
      <div class="top3-section">
        <div class="top3-badge">1</div>
        <div class="top3-content">
          <label class="field-label">A tarefa mais importante de hoje</label>
          <div class="write-area" style="min-height:35px;"></div>
          <div style="margin-top:6px;"><label class="field-label-inline">Por que é prioridade?</label><div class="write-line"></div></div>
        </div>
      </div>
      <div class="top3-section">
        <div class="top3-badge">2</div>
        <div class="top3-content">
          <label class="field-label">Segunda prioridade</label>
          <div class="write-line"></div>
        </div>
      </div>
      <div class="top3-section">
        <div class="top3-badge">3</div>
        <div class="top3-content">
          <label class="field-label">Terceira prioridade</label>
          <div class="write-line"></div>
        </div>
      </div>
    </div>
    <div style="margin-top:20px;">
      <div class="subsection-title">Tarefas Menores (se der tempo)</div>
      ''' + '\n'.join([checkbox("_" * 48) for _ in range(5)]) + '''
    </div>
    <div class="daily-reflection" style="margin-top:16px;">
      <div class="subsection-title">Final do Dia</div>
      <div class="grid-2">
        <div><label class="field-label-inline">Completei?</label><div class="write-line"></div></div>
        <div><label class="field-label-inline">Gratidão:</label><div class="write-line"></div></div>
      </div>
    </div>'''
    pages.append(page_wrap(53, content, "Diário", "53"))

    # P54: Time Blocking
    blocks = ""
    slots = [("06-08","Manhã cedo"),("08-10","Manhã"),("10-12","Meio da manhã"),
             ("12-13","Almoço"),("13-15","Início da tarde"),("15-17","Tarde"),
             ("17-19","Final da tarde"),("19-21","Noite"),("21-23","Noite tardia")]
    for time, label in slots:
        blocks += f'''<div class="time-block">
        <div class="tb-time">{time}</div>
        <div class="tb-label">{label}</div>
        <div class="tb-space"><div class="write-line"></div><div class="write-line"></div></div>
      </div>\n'''
    content = f'''<h1 class="page-title">Time Blocking</h1>
    <p class="page-subtitle">Atribua blocos de tempo para cada tipo de atividade. Não planeje hora a hora — agrupe.</p>
    <div class="daily-header-fields">
      <div><label class="field-label">Data:</label><div class="write-line" style="width:200px;display:inline-block;"></div></div>
    </div>
    <div class="time-blocks" style="margin-top:14px;">
      {blocks}
    </div>
    <div class="tip-box" style="margin-top:10px;">
      <strong>Dica TDAH:</strong> Deixe blocos de "buffer" entre tarefas. Transições levam mais tempo do que imaginamos.
    </div>'''
    pages.append(page_wrap(54, content, "Diário", "54"))

    # P55: Rotina Matinal
    content = '''<h1 class="page-title">Rotina Matinal</h1>
    <p class="page-subtitle">Uma boa manhã não precisa ser perfeita. Precisa ser previsível.</p>
    <div class="routine-builder">
      <div class="subsection-title">Minha Rotina Matinal Ideal</div>
      <table class="table" style="margin-top:8px;">
        <thead><tr><th style="width:15%">Hora</th><th style="width:55%">Ação</th><th style="width:15%">Duração</th><th style="width:15%">Feito</th></tr></thead>
        <tbody>''' + ''.join([f'<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="checkbox" style="margin:auto;"></div></td></tr>' for _ in range(8)]) + '''
        </tbody>
      </table>
    </div>
    <div style="margin-top:16px;">
      <div class="subsection-title">Versão Mínima (para dias difíceis)</div>
      <p style="font-size:9pt;color:#64748B;margin-bottom:8px;">O mínimo que preciso fazer para o dia não desandar:</p>
      ''' + '\n'.join([checkbox("_" * 48) for _ in range(3)]) + '''
    </div>
    <div class="tip-box" style="margin-top:12px;">
      <strong>Lembre:</strong> Nos dias ruins, a versão mínima já é vitória. Não compare com os dias bons.
    </div>'''
    pages.append(page_wrap(55, content, "Diário", "55"))

    # P56: Rotina Noturna
    content = '''<h1 class="page-title">Rotina Noturna</h1>
    <p class="page-subtitle">Prepare o amanhã enquanto ainda tem energia. Seu eu do futuro agradece.</p>
    <div class="routine-builder">
      <div class="subsection-title">Minha Rotina Noturna</div>
      <table class="table" style="margin-top:8px;">
        <thead><tr><th style="width:15%">Hora</th><th style="width:55%">Ação</th><th style="width:15%">Min</th><th style="width:15%">✓</th></tr></thead>
        <tbody>''' + ''.join([f'<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="checkbox" style="margin:auto;"></div></td></tr>' for _ in range(7)]) + '''
        </tbody>
      </table>
    </div>
    <div style="margin-top:16px;">
      <div class="subsection-title">Checklist Antes de Dormir</div>
      ''' + checkbox("Roupa de amanhã separada") + checkbox("Bolsa/mochila pronta") + checkbox("Alarme configurado") + checkbox("Telas desligadas") + checkbox("Copo de água na mesa") + '''
    </div>
    <div style="margin-top:12px;">
      <div class="subsection-title">Preparar para Amanhã</div>
      <div class="grid-2">
        <div><label class="field-label-inline">Prioridade #1:</label><div class="write-line"></div></div>
        <div><label class="field-label-inline">Compromisso:</label><div class="write-line"></div></div>
      </div>
    </div>'''
    pages.append(page_wrap(56, content, "Diário", "56"))

    # P57: Checklist Diario
    content = '''<h1 class="page-title">Checklist Diário</h1>
    <div class="daily-header-fields">
      <div><label class="field-label">Data:</label><div class="write-line" style="width:200px;display:inline-block;"></div></div>
    </div>
    <div class="grid-2" style="margin-top:16px;gap:20px;">
      <div>
        <div class="subsection-title">Autocuidado</div>
        ''' + checkbox("Tomei água suficiente") + checkbox("Comi refeições regulares") + checkbox("Tomei medicação") + checkbox("Dormi bem") + checkbox("Me movimentei") + checkbox("Tive um momento de pausa") + '''
      </div>
      <div>
        <div class="subsection-title">Produtividade</div>
        ''' + checkbox("Defini prioridades do dia") + checkbox("Completei a tarefa #1") + checkbox("Não procrastinei o urgente") + checkbox("Fiz uma pausa entre tarefas") + checkbox("Organizei meu espaço") + checkbox("Planejei o amanhã") + '''
      </div>
    </div>
    <div style="margin-top:16px;">
      <div class="subsection-title">Relacionamentos</div>
      <div class="grid-2">
        ''' + checkbox("Respondi mensagens pendentes") + checkbox("Estive presente em uma conversa") + '''
      </div>
    </div>
    <div style="margin-top:16px;">
      <div class="subsection-title">Como me sinto agora?</div>
      <div class="mood-scale">
        <span>😔</span><div class="mood-circles">''' + ''.join(['<div class="mood-circle"></div>' for _ in range(10)]) + '''</div><span>😊</span>
      </div>
    </div>'''
    pages.append(page_wrap(57, content, "Diário", "57"))

    # P58: Daily Check-in
    content = '''<h1 class="page-title">Check-in Diário</h1>
    <div class="daily-header-fields">
      <div class="grid-3"><div><label class="field-label">Data</label><div class="write-line"></div></div><div><label class="field-label">Hora</label><div class="write-line"></div></div><div><label class="field-label">Clima</label><div class="write-line"></div></div></div>
    </div>
    <div class="checkin-grid" style="margin-top:16px;">
      <div class="checkin-section">
        <div class="subsection-title">Energia</div>
        <div class="scale-bar"><span>Esgotado</span>''' + ''.join(['<div class="scale-dot"></div>' for _ in range(10)]) + '''<span>Máxima</span></div>
      </div>
      <div class="checkin-section">
        <div class="subsection-title">Humor</div>
        <div class="scale-bar"><span>Péssimo</span>''' + ''.join(['<div class="scale-dot"></div>' for _ in range(10)]) + '''<span>Ótimo</span></div>
      </div>
      <div class="checkin-section">
        <div class="subsection-title">Foco</div>
        <div class="scale-bar"><span>Disperso</span>''' + ''.join(['<div class="scale-dot"></div>' for _ in range(10)]) + '''<span>Laser</span></div>
      </div>
      <div class="checkin-section">
        <div class="subsection-title">Ansiedade</div>
        <div class="scale-bar"><span>Calmo</span>''' + ''.join(['<div class="scale-dot"></div>' for _ in range(10)]) + '''<span>Intensa</span></div>
      </div>
    </div>
    <div style="margin-top:16px;">
      <div class="subsection-title">O que está na minha cabeça agora?</div>
      ''' + write_lines(3) + '''
    </div>
    <div style="margin-top:12px;">
      <div class="subsection-title">Uma coisa que posso fazer para melhorar meu dia:</div>
      <div class="write-line"></div>
    </div>'''
    pages.append(page_wrap(58, content, "Diário", "58"))

    # P59: Brain Dump
    content = '''<h1 class="page-title">Brain Dump</h1>
    <p class="page-subtitle">Tire tudo da cabeça. Não organize, não julgue, não priorize. Apenas escreva.</p>
    <div class="brain-dump-area">
      ''' + write_lines(22, dotted=True) + '''
    </div>
    <div class="tip-box" style="margin-top:auto;">
      <strong>Depois:</strong> Circule 3 itens que são realmente importantes. O resto pode esperar ou ser descartado.
    </div>'''
    pages.append(page_wrap(59, content, "Diário", "59"))

    # P60: Captura Rapida de Ideias
    content = '''<h1 class="page-title">Captura Rápida</h1>
    <p class="page-subtitle">Ideias que surgem no meio de outra coisa. Anote aqui para não perder — e não perder o foco.</p>
    <div class="capture-grid">''' + ''.join([f'''
      <div class="capture-card">
        <div class="capture-num">{i}</div>
        <div class="write-line" style="flex:1;"></div>
        <div class="capture-priority">
          <span class="priority-dot high-dot"></span>
          <span class="priority-dot med-dot"></span>
          <span class="priority-dot low-dot"></span>
        </div>
      </div>''' for i in range(1, 16)]) + '''
    </div>
    <div class="legend-inline" style="margin-top:8px;">
      <span><span class="priority-dot high-dot"></span> Urgente</span>
      <span><span class="priority-dot med-dot"></span> Importante</span>
      <span><span class="priority-dot low-dot"></span> Algum dia</span>
    </div>'''
    pages.append(page_wrap(60, content, "Diário", "60"))

    # P61: Dia Produtivo Simplificado
    content = '''<h1 class="page-title">Dia Produtivo</h1>
    <div class="daily-header-fields">
      <div class="grid-2"><div><label class="field-label">Data</label><div class="write-line"></div></div><div><label class="field-label">Nível de energia</label><div class="write-line"></div></div></div>
    </div>
    <div class="productive-day" style="margin-top:16px;">
      <div class="card card-blue">
        <div class="card-header">A ÚNICA coisa que preciso fazer hoje:</div>
        <div class="write-area" style="min-height:40px;"></div>
      </div>
      <div class="grid-2" style="gap:16px;margin-top:12px;">
        <div class="card">
          <div class="card-header">Manhã</div>
          ''' + '\n'.join([checkbox("_" * 28) for _ in range(4)]) + '''
        </div>
        <div class="card">
          <div class="card-header">Tarde</div>
          ''' + '\n'.join([checkbox("_" * 28) for _ in range(4)]) + '''
        </div>
      </div>
      <div class="card" style="margin-top:12px;">
        <div class="card-header">Noite</div>
        ''' + '\n'.join([checkbox("_" * 50) for _ in range(2)]) + '''
      </div>
    </div>
    <div class="grid-2" style="margin-top:12px;gap:16px;">
      <div><label class="field-label-inline">Melhor momento do dia:</label><div class="write-line"></div></div>
      <div><label class="field-label-inline">Nota para amanhã:</label><div class="write-line"></div></div>
    </div>'''
    pages.append(page_wrap(61, content, "Diário", "61"))

    # P62: Planejamento de Projeto
    content = '''<h1 class="page-title">Planejamento de Projeto</h1>
    <div class="project-header">
      <div class="grid-2" style="gap:16px;">
        <div><label class="field-label">Nome do Projeto</label><div class="write-line"></div></div>
        <div><label class="field-label">Prazo Final</label><div class="write-line"></div></div>
      </div>
      <div style="margin-top:10px;"><label class="field-label">Objetivo do Projeto</label><div class="write-area" style="min-height:35px;"></div></div>
    </div>
    <div style="margin-top:14px;">
      <div class="subsection-title">Etapas</div>
      <table class="table">
        <thead><tr><th style="width:5%">#</th><th style="width:50%">Etapa</th><th style="width:20%">Prazo</th><th style="width:15%">Status</th><th style="width:10%">✓</th></tr></thead>
        <tbody>''' + ''.join([f'<tr><td>{i}</td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="checkbox" style="margin:auto;"></div></td></tr>' for i in range(1, 9)]) + '''
        </tbody>
      </table>
    </div>
    <div style="margin-top:12px;">
      <div class="subsection-title">Recursos Necessários</div>
      ''' + write_lines(2) + '''
    </div>
    <div style="margin-top:10px;">
      <div class="subsection-title">Possíveis Obstáculos</div>
      ''' + write_lines(2) + '''
    </div>'''
    pages.append(page_wrap(62, content, "Diário", "62"))

    # P63: Controle de Hiperfoco
    content = '''<h1 class="page-title">Controle de Hiperfoco</h1>
    <p class="page-subtitle">O hiperfoco é um superpoder — mas sem controle, ele consome horas sem você perceber.</p>
    <div class="hyperfocus-log">
      <div class="subsection-title">Registro de Hiperfoco</div>
      <table class="table" style="margin-top:8px;">
        <thead><tr><th style="width:15%">Data</th><th style="width:30%">No que foquei</th><th style="width:15%">Duração</th><th style="width:20%">Era produtivo?</th><th style="width:20%">Consequência</th></tr></thead>
        <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(7)]) + '''
        </tbody>
      </table>
    </div>
    <div style="margin-top:14px;">
      <div class="subsection-title">Estratégias para Usar o Hiperfoco a meu Favor</div>
      ''' + checkbox("Definir alarme antes de começar") + checkbox("Ter lista do que NÃO pode ser adiado") + checkbox("Avisar alguém que vou mergulhar") + checkbox("Colocar água e comida por perto") + '''
    </div>
    <div style="margin-top:12px;">
      <div class="subsection-title">Meus Gatilhos de Hiperfoco</div>
      ''' + write_lines(3) + '''
    </div>'''
    pages.append(page_wrap(63, content, "Diário", "63"))

    return pages
