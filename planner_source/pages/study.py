# -*- coding: utf-8 -*-
"""Secao 10: Estudos (paginas 100-107)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers import page_wrap, checkbox, write_lines, field


def get_pages():
    pages = []

    # P100: Planner de Estudos
    content = '''<h1 class="page-title">Planner de Estudos</h1>
    <div class="grid-2" style="gap:16px;">
      <div>''' + field("Matéria / Curso") + field("Professor / Plataforma") + field("Meta de estudo") + '''</div>
      <div>''' + field("Prazo / Prova") + field("Material necessário") + field("Horário ideal p/ estudar") + '''</div>
    </div>
    <div style="margin-top:16px;">
      <div class="subsection-title">Cronograma da Semana</div>
      <table class="table">
        <thead><tr><th>Dia</th><th>Tópico</th><th>Duração</th><th>Método</th><th>Feito</th></tr></thead>
        <tbody>''' + ''.join([f'<tr><td>{d}</td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="checkbox" style="margin:auto;"></div></td></tr>' for d in ["Seg","Ter","Qua","Qui","Sex","Sáb","Dom"]]) + '''
        </tbody>
      </table>
    </div>
    <div class="tip-box" style="margin-top:12px;">
      <strong>Dica TDAH:</strong> Alterne entre matérias a cada 25-45 min. Monotonia mata o foco.
    </div>'''
    pages.append(page_wrap(100, content, "Estudos", "100"))

    # P101: Planner por Materia
    content = '''<h1 class="page-title">Estudo por Tópico</h1>
    <div class="grid-2" style="margin-bottom:16px;">
      <div>''' + field("Matéria") + '''</div>
      <div>''' + field("Capítulo / Módulo") + '''</div>
    </div>
    <div class="study-sections">
      <div class="study-section">
        <div class="subsection-title">Conceitos Principais</div>
        ''' + write_lines(5, dotted=True) + '''
      </div>
      <div class="study-section" style="margin-top:14px;">
        <div class="subsection-title">Dúvidas / Pontos de Confusão</div>
        ''' + write_lines(3, dotted=True) + '''
      </div>
      <div class="study-section" style="margin-top:14px;">
        <div class="subsection-title">Conexões com o que já sei</div>
        ''' + write_lines(3, dotted=True) + '''
      </div>
      <div class="study-section" style="margin-top:14px;">
        <div class="subsection-title">Resumo em 3 frases</div>
        ''' + write_lines(3) + '''
      </div>
    </div>'''
    pages.append(page_wrap(101, content, "Estudos", "101"))

    # P102: Checklist de Estudos
    content = '''<h1 class="page-title">Checklist de Estudos</h1>
    <div class="month-field"><label class="field-label-inline">Período:</label><div class="write-line" style="width:200px;display:inline-block;"></div></div>
    <div class="grid-2" style="gap:20px;margin-top:16px;">
      <div>
        <div class="subsection-title">Antes de Estudar</div>
        ''' + checkbox("Ambiente organizado") + checkbox("Celular no silencioso") + checkbox("Água e lanche prontos") + checkbox("Material separado") + checkbox("Timer configurado") + checkbox("Meta da sessão definida") + '''
      </div>
      <div>
        <div class="subsection-title">Durante o Estudo</div>
        ''' + checkbox("Anotações ativas (não passivas)") + checkbox("Pausas a cada 25-45 min") + checkbox("Resumo ao final de cada bloco") + checkbox("Dúvidas anotadas") + checkbox("Sem multitarefa") + checkbox("Recompensa entre blocos") + '''
      </div>
    </div>
    <div style="margin-top:16px;">
      <div class="subsection-title">Revisão</div>
      ''' + checkbox("Revisei em 24h") + checkbox("Revisei em 1 semana") + checkbox("Revisei em 1 mês") + checkbox("Fiz exercícios práticos") + checkbox("Expliquei para alguém (ou para mim mesmo)") + '''
    </div>'''
    pages.append(page_wrap(102, content, "Estudos", "102"))

    # P103: Checklist de Trabalho
    content = '''<h1 class="page-title">Checklist de Trabalho</h1>
    <div class="work-checklist">
      <div class="grid-2" style="gap:20px;">
        <div>
          <div class="subsection-title">Início do Dia</div>
          ''' + checkbox("Verificar agenda/calendário") + checkbox("Definir as 3 prioridades") + checkbox("Responder mensagens urgentes") + checkbox("Organizar mesa/área de trabalho") + checkbox("Timer do primeiro bloco") + '''
        </div>
        <div>
          <div class="subsection-title">Final do Dia</div>
          ''' + checkbox("Anotar pendências para amanhã") + checkbox("Responder mensagens pendentes") + checkbox("Atualizar status de projetos") + checkbox("Organizar arquivos/abas") + checkbox("Definir primeira tarefa de amanhã") + '''
        </div>
      </div>
      <div style="margin-top:20px;">
        <div class="subsection-title">Projetos em Andamento</div>
        <table class="table">
          <thead><tr><th style="width:30%;">Projeto</th><th style="width:25%;">Próxima ação</th><th style="width:15%;">Prazo</th><th style="width:15%;">Prioridade</th><th style="width:15%;">Status</th></tr></thead>
          <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(6)]) + '''
          </tbody>
        </table>
      </div>
    </div>'''
    pages.append(page_wrap(103, content, "Estudos", "103"))

    # P104: Checklist de Limpeza
    content = '''<h1 class="page-title">Checklist de Limpeza</h1>
    <p class="page-subtitle">Divida por cômodo e por frequência. Não tente limpar tudo no mesmo dia.</p>
    <div class="grid-2" style="gap:16px;">
      <div class="card">
        <div class="card-header">Diário (5 min)</div>
        ''' + checkbox("Lavar louça") + checkbox("Guardar o que está fora do lugar") + checkbox("Limpar superfícies da cozinha") + checkbox("Tirar lixo se cheio") + '''
      </div>
      <div class="card">
        <div class="card-header">Semanal</div>
        ''' + checkbox("Aspirar / varrer") + checkbox("Trocar roupa de cama") + checkbox("Limpar banheiro") + checkbox("Passar pano no chão") + checkbox("Organizar papéis") + '''
      </div>
    </div>
    <div class="grid-2" style="gap:16px;margin-top:12px;">
      <div class="card">
        <div class="card-header">Quinzenal</div>
        ''' + checkbox("Limpar geladeira") + checkbox("Lavar tapetes") + checkbox("Limpar janelas") + '''
      </div>
      <div class="card">
        <div class="card-header">Mensal</div>
        ''' + checkbox("Limpar armários") + checkbox("Verificar vencimentos") + checkbox("Organizar gavetas") + '''
      </div>
    </div>'''
    pages.append(page_wrap(104, content, "Organização", "104"))

    # P105: Planner de Leitura
    content = '''<h1 class="page-title">Planner de Leitura</h1>
    <table class="table" style="margin-top:12px;">
      <thead><tr><th style="width:25%;">Título</th><th style="width:20%;">Autor</th><th style="width:12%;">Páginas</th><th style="width:12%;">Início</th><th style="width:12%;">Fim</th><th style="width:19%;">Avaliação</th></tr></thead>
      <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(12)]) + '''
      </tbody></table>
    <div style="margin-top:14px;">
      <div class="subsection-title">Quero Ler</div>
      ''' + write_lines(5, dotted=True) + '''
    </div>'''
    pages.append(page_wrap(105, content, "Estudos", "105"))

    # P106: Planner de Cursos
    content = '''<h1 class="page-title">Cursos e Aprendizado</h1>
    <table class="table" style="margin-top:12px;">
      <thead><tr><th style="width:25%;">Curso</th><th style="width:20%;">Plataforma</th><th style="width:15%;">Progresso</th><th style="width:15%;">Prazo</th><th style="width:25%;">Próximo passo</th></tr></thead>
      <tbody>''' + ''.join(['<tr><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td><td><div class="write-line"></div></td></tr>' for _ in range(8)]) + '''
      </tbody></table>
    <div style="margin-top:16px;">
      <div class="subsection-title">Habilidades que quero desenvolver</div>
      ''' + '\n'.join([checkbox("_" * 45) for _ in range(5)]) + '''
    </div>'''
    pages.append(page_wrap(106, content, "Estudos", "106"))

    # P107: Anotacoes Cornell
    content = '''<h1 class="page-title">Anotações — Método Cornell</h1>
    <div class="grid-2" style="margin-bottom:12px;">
      <div>''' + field("Matéria / Tópico") + '''</div>
      <div>''' + field("Data") + '''</div>
    </div>
    <div class="cornell-layout">
      <div class="cornell-left">
        <div class="cornell-label">Palavras-chave / Perguntas</div>
        ''' + write_lines(20, dotted=True) + '''
      </div>
      <div class="cornell-right">
        <div class="cornell-label">Anotações</div>
        ''' + write_lines(20, dotted=True) + '''
      </div>
    </div>
    <div class="cornell-bottom" style="margin-top:12px;">
      <div class="cornell-label">Resumo (com suas próprias palavras)</div>
      ''' + write_lines(4) + '''
    </div>'''
    pages.append(page_wrap(107, content, "Estudos", "107"))

    return pages