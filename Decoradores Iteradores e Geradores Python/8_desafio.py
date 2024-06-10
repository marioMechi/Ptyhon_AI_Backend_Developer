def transacoes(self):
    return self._transacoes

def adicionar_transacao(self, transacao):
    self._transacoes.append(
        {
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        }
    )

def gerar_relatorio(self, tipo_transacao=None):
    for transacao in self._trasacoes:
        if tipo_transacao is None or transacao ['tipo'].lower() == tipo_transacao.lower():
            yield transacao
def transacoes_do_dia(self):
    data_atual = datetime.utcnow().date()
    transacoes = []
    for trasacao in self._transacoes:
        data_transacao = datetime. striptime(trasacao['data'], "%d-%m-Y %H: %M :S"). date()
        if data_atual ==data_transacao:
            transacoes.append(transacao)
        return transacoes