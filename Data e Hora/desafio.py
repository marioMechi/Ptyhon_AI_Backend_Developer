def log_transacao(func):
    def envolve(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f'{datetime.now()}: {func.__name__.upper()}')
        return resultado
    return envelope