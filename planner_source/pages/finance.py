# -*- coding: utf-8 -*-
"""Secao 8: Financeiro (paginas 78-87)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers import page_wrap, checkbox, write_lines, field


def get_pages():
    pages = []

    # P78: Visao Financeira
    content = '''<h1 class="page-title">Visão Financeira</h1>
    <p class="page-subtitle">Comece com clareza. Quanto entra, quanto sai, quanto sobra.</p>
    <div class="grid-2" style="gap:20px;">
      <div class="card card-blue">
        <div class="card-header">Renda Mensal</div>
        <table class="table">
          <thead><tr><th>Fonte</th><th style="width:30%;">Valor</th></tr></thead>
          <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(4)]) + '''
          <tr><td style="font-weight:600;">Total</td><td><div class="write-line"></div></td></tr>
          </tbody></table>
      </div>
      <div class="card">
        <div class="card-header">Gastos Essenciais</div>
        <table class="table">
          <thead><tr><th>Item</th><th style="width:30%;">Valor</th></tr></thead>
          <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(6)]) + '''
          <tr><td style="font-weight:600;">Total</td><td><div class="write-line"></div></td></tr>
          </tbody></table>
      </div>
    </div>
    <div class="card" style="margin-top:16px;">
      <div class="grid-3" style="text-align:center;">
        <div><div class="fin-label">Renda</div><div class="write-line"></div></div>
        <div><div class="fin-label">Gastos</div><div class="write-line"></div></div>
        <div><div class="fin-label">Sobra</div><div class="write-line"></div></div>
      </div>
    </div>'''
    pages.append(page_wrap(78, content, u"Finanças", "78"))

    # P79: Controle de Gastos
    content = '''<h1 class="page-title">Controle de Gastos</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:150px;display:inline-block;"></div></div>
    <table class="table" style="margin-top:12px;">
      <thead><tr><th style="width:10%;">Dia</th><th style="width:35%;">Descrição</th><th style="width:20%;">Categoria</th><th style="width:15%;">Valor</th><th style="width:20%;">Pgto</th></tr></thead>
      <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(20)]) + '''
      </tbody></table>
    <div style="margin-top:10px;text-align:right;"><strong>Total: R$ </strong><div class="write-line" style="width:100px;display:inline-block;"></div></div>'''
    pages.append(page_wrap(79, content, u"Finanças", "79"))

    # P80: Controle de Contas
    content = '''<h1 class="page-title">Controle de Contas</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:150px;display:inline-block;"></div></div>
    <table class="table" style="margin-top:12px;">
      <thead><tr><th>Conta</th><th>Vencimento</th><th>Valor</th><th>Pago</th></tr></thead>
      <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="checkbox" style="margin:auto;"></div></td></tr>' for _ in range(14)]) + '''
      </tbody></table>'''
    pages.append(page_wrap(80, content, u"Finanças", "80"))

    # P81: Assinaturas
    content = '''<h1 class="page-title">Controle de Assinaturas</h1>
    <p class="page-subtitle">Liste todos os serviços recorrentes. Avalie se ainda precisa de cada um.</p>
    <table class="table" style="margin-top:12px;">
      <thead><tr><th>Serviço</th><th>Valor</th><th>Frequência</th><th>Preciso?</th></tr></thead>
      <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(12)]) + '''
      </tbody></table>
    <div class="card" style="margin-top:14px;">
      <div class="grid-3" style="text-align:center;">
        <div><div class="fin-label">Total Mensal</div><div>R$ <div class="write-line" style="width:60px;display:inline-block;"></div></div></div>
        <div><div class="fin-label">Total Anual</div><div>R$ <div class="write-line" style="width:60px;display:inline-block;"></div></div></div>
        <div><div class="fin-label">Posso Cancelar</div><div>R$ <div class="write-line" style="width:60px;display:inline-block;"></div></div></div>
      </div>
    </div>'''
    pages.append(page_wrap(81, content, u"Finanças", "81"))

    # P82: Lista de Compras
    content = '''<h1 class="page-title">Lista de Compras</h1>
    <div class="grid-2" style="gap:20px;">
      <div>
        <div class="subsection-title">Alimentação</div>
        ''' + '\n'.join([checkbox("_" * 28) for _ in range(12)]) + '''
      </div>
      <div>
        <div class="subsection-title">Higiene e Limpeza</div>
        ''' + '\n'.join([checkbox("_" * 28) for _ in range(12)]) + '''
      </div>
    </div>'''
    pages.append(page_wrap(82, content, u"Finanças", "82"))

    # P83: Metas Financeiras
    content = '''<h1 class="page-title">Metas Financeiras</h1>
    <div class="finance-goals">''' + ''.join([f'''
      <div class="fin-goal-card">
        <div class="fin-goal-num">{i}</div>
        <div class="fin-goal-fields">
          <div class="grid-2">
            <div><label class="field-label-inline">Meta:</label><div class="write-line"></div></div>
            <div><label class="field-label-inline">Valor:</label><div class="write-line"></div></div>
          </div>
          <div class="grid-2" style="margin-top:6px;">
            <div><label class="field-label-inline">Prazo:</label><div class="write-line"></div></div>
            <div><label class="field-label-inline">Guardar/mês:</label><div class="write-line"></div></div>
          </div>
          <div class="progress-bar-empty" style="margin-top:6px;"></div>
        </div>
      </div>''' for i in range(1, 6)]) + '''
    </div>'''
    pages.append(page_wrap(83, content, u"Finanças", "83"))

    # P84: Balanco Mensal
    content = '''<h1 class="page-title">Balanço Mensal</h1>
    <div class="month-field"><label class="field-label-inline">Mês:</label><div class="write-line" style="width:150px;display:inline-block;"></div></div>
    <div class="grid-2" style="gap:20px;margin-top:14px;">
      <div class="card card-blue">
        <div class="card-header">Entradas</div>
        <table class="table">
          <thead><tr><th>Fonte</th><th>Valor</th></tr></thead>
          <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(5)]) + '''
          <tr><td style="font-weight:600;">Total</td><td><div class="write-line"></div></td></tr>
          </tbody></table>
      </div>
      <div class="card">
        <div class="card-header">Saídas por Categoria</div>
        <table class="table">
          <thead><tr><th>Categoria</th><th>Valor</th></tr></thead>
          <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(7)]) + '''
          <tr><td style="font-weight:600;">Total</td><td><div class="write-line"></div></td></tr>
          </tbody></table>
      </div>
    </div>
    <div class="card" style="margin-top:14px;">
      <div class="grid-3" style="text-align:center;">
        <div><div class="fin-label">Entrou</div><div class="write-line"></div></div>
        <div><div class="fin-label">Saiu</div><div class="write-line"></div></div>
        <div><div class="fin-label">Resultado</div><div class="write-line"></div></div>
      </div>
    </div>'''
    pages.append(page_wrap(84, content, u"Finanças", "84"))

    # P85: Controle de Dividas
    content = '''<h1 class="page-title">Controle de Dívidas</h1>
    <table class="table" style="margin-top:12px;">
      <thead><tr><th>Dívida</th><th>Total</th><th>Parcela</th><th>Restam</th><th>Juros</th></tr></thead>
      <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(8)]) + '''
      </tbody></table>
    <div style="margin-top:14px;">
      <div class="subsection-title">Estratégia de Quitação</div>
      ''' + write_lines(3) + '''
    </div>'''
    pages.append(page_wrap(85, content, u"Finanças", "85"))

    # P86: Compras Planejadas
    content = '''<h1 class="page-title">Compras Planejadas</h1>
    <p class="page-subtitle">Antes de comprar por impulso, anote aqui. Espere 48h. Ainda quer?</p>
    <table class="table" style="margin-top:12px;">
      <thead><tr><th style="width:30%;">Item</th><th>Preço</th><th>Preciso?</th><th>Prioridade</th><th>Comprei?</th></tr></thead>
      <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="checkbox" style="margin:auto;"></div></td></tr>' for _ in range(12)]) + '''
      </tbody></table>
    <div class="tip-box" style="margin-top:12px;">
      <strong>Regra dos 48h:</strong> Anotou? Espere 2 dias. Se ainda quiser, libere. Impulso passa, necessidade real não.
    </div>'''
    pages.append(page_wrap(86, content, u"Finanças", "86"))

    # P87: Renda Extra
    content = '''<h1 class="page-title">Renda Extra</h1>
    <div class="subsection-title">Ideias de Renda Extra</div>
    ''' + write_lines(5, dotted=True) + '''
    <div style="margin-top:16px;">
      <div class="subsection-title">Acompanhamento</div>
      <table class="table">
        <thead><tr><th>Fonte</th><th>Mês</th><th>Valor</th><th>Horas</th></tr></thead>
        <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(8)]) + '''
        </tbody></table>
    </div>'''
    pages.append(page_wrap(87, content, u"Finanças", "87"))

    return pages
