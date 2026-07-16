# -*- coding: utf-8 -*-
"""Shared helpers for page generation."""


def header(section=""):
    return f'''<div class="page-header">
    <span class="brand">CATreport</span>
    <span class="section-name">{section}</span>
  </div>'''


def footer(num):
    return f'''<div class="page-footer">
    <span class="footer-brand">CATreport</span>
    <span class="page-number">{num}</span>
  </div>'''


def checkbox(label, meta=""):
    m = f'<span class="meta">{meta}</span>' if meta else ""
    return f'<div class="checkbox-line"><div class="checkbox"></div><span class="label">{label}</span>{m}</div>'


def write_lines(count, dotted=False):
    cls = "write-line-dotted" if dotted else "write-line"
    return "\n".join([f'<div class="{cls}"></div>' for _ in range(count)])


def field(label):
    return f'''<div class="field-group">
    <label class="field-label">{label}</label>
    <div class="write-line"></div>
  </div>'''


def page_wrap(page_id, content, section="", num=""):
    h = header(section) if section else ""
    f = footer(num) if num else ""
    return f'''<section class="page" id="page-{page_id}">
  {h}
  <div class="page-content">
    {content}
  </div>
  {f}
</section>'''
