# -*- coding: utf-8 -*-
"""Secao 12: Notas e Paginas Extras (paginas 118-120+)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers import page_wrap, checkbox, write_lines, field


def get_pages():
    pages = []

    # P118: Notas Pautadas
    content = '''<h1 class="page-title">Notas</h1>
    <div class="notes-lined">
      ''' + write_lines(30) + '''
    </div>'''
    pages.append(page_wrap(118, content, "Notas", "118"))

    # P119: Notas Pontilhadas
    dots_row = '<div class="dot-row">' + ''.join(['<span class="dot"></span>' for _ in range(34)]) + '</div>'
    content = '''<h1 class="page-title">Notas</h1>
    <div class="notes-dotted">
      ''' + '\n'.join([dots_row for _ in range(38)]) + '''
    </div>'''
    pages.append(page_wrap(119, content, "Notas", "119"))

    # P120: Notas Quadriculadas
    content = '''<h1 class="page-title">Notas</h1>
    <div class="notes-grid-paper"></div>'''
    pages.append(page_wrap(120, content, "Notas", "120"))

    # P121: Frases Motivacionais (separador)
    quotes = [
        "Progresso não precisa ser linear para ser real.",
        "Feito é melhor que perfeito.",
        "Você não está atrasado. Está no seu tempo.",
        "Cada recomeço ainda é um passo à frente.",
    ]
    quote_cards = ""
    for q in quotes:
        quote_cards += f'''<div class="quote-card"><p class="quote-text">&ldquo;{q}&rdquo;</p></div>\n'''
    content = f'''<div class="quotes-page">
      <div class="quotes-header">
        <svg width="40" height="40" viewBox="0 0 40 40" fill="none"><path d="M12 20c-3 0-5-2-5-5s2-5 5-5c0-3 4-5 4-5s-8 2-8 10c0 4 3 7 7 7s5-3 5-5-2-2-3-2zm16 0c-3 0-5-2-5-5s2-5 5-5c0-3 4-5 4-5s-8 2-8 10c0 4 3 7 7 7s5-3 5-5-2-2-3-2z" fill="#2563EB" opacity="0.15"/></svg>
      </div>
      {quote_cards}
    </div>'''
    pages.append(page_wrap(121, content, "", ""))

    # P122: Pagina Final
    pages.append('''<section class="page page-final" id="page-122">
  <div class="page-content" style="display:flex;align-items:center;justify-content:center;text-align:center;">
    <div>
      <svg width="48" height="48" viewBox="0 0 48 48" fill="none" style="margin-bottom:24px;">
        <rect width="48" height="48" rx="10" fill="#2563EB" fill-opacity="0.1"/>
        <path d="M12 24h6l4-8 6 16 4-8h6" stroke="#2563EB" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <h2 style="font-size:18pt;font-weight:700;color:#1E3A8A;margin-bottom:12px;">Planner TDAH Produtivo</h2>
      <p style="font-size:10pt;color:#64748B;margin-bottom:24px;">Um produto CATreport</p>
      <div style="width:60px;height:2px;background:#2563EB;margin:0 auto 24px;"></div>
      <p style="font-size:10pt;color:#475569;line-height:1.8;max-width:300px;margin:0 auto;">
        Obrigado por escolher organizar sua vida com gentileza.<br>
        Lembre-se: não existe forma errada de usar este planner.<br>
        O melhor sistema é aquele que você realmente usa.
      </p>
      <p style="font-size:9pt;color:#94A3B8;margin-top:32px;">
        &copy; CATreport. Todos os direitos reservados.<br>
        Uso pessoal. Redistribuição não autorizada.
      </p>
    </div>
  </div>
</section>''')

    return pages
