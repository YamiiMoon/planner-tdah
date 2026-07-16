# Instruções para configurar o PDF do Planner

## Como gerar o PDF

1. Abra o arquivo `index.html` (gerado pelo build.py) no navegador
2. Use Ctrl+P (ou Cmd+P no Mac)
3. Selecione "Salvar como PDF"
4. Certifique-se de que o tamanho está em A4
5. Margens: Nenhuma
6. Marque "Gráficos de fundo"
7. Salve como `planner-tdah-produtivo.pdf`

## Onde colocar o PDF

Coloque o arquivo PDF na pasta:

```
secure/planner-tdah-produtivo.pdf
```

O nome do arquivo deve corresponder ao configurado em `config.py`:

```python
PDF_FILENAME = "planner-tdah-produtivo.pdf"
```

## Segurança

- A pasta `secure/` NÃO é servida publicamente
- O download só é liberado após confirmação de pagamento
- Cada token de download expira após 30 minutos
- Cada token só pode ser usado uma vez

## Testando

Para testar sem pagamento real:
1. Use o ambiente sandbox do Asaas (ASAAS_SANDBOX = True no config.py)
2. Crie uma cobrança
3. No painel sandbox do Asaas, simule o pagamento
4. O webhook notificará sua aplicação
5. O redirecionamento acontecerá automaticamente
