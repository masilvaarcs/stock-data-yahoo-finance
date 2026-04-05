"""Consulta dados de ações da Apple via Yahoo Finance (yfinance)."""

import argparse
import yfinance as yf


def obter_dados_acao(ticker: str = "AAPL", periodo: str = "1mo"):
    """Baixa dados históricos de uma ação."""
    dados = yf.download(ticker, period=periodo)
    return dados


def calcular_ganho(dados):
    """Calcula ganho/perda percentual entre primeiro e último fechamento."""
    if dados.empty:
        return 0.0
    primeiro = float(dados["Close"].iloc[0])
    ultimo = float(dados["Close"].iloc[-1])
    return round(((ultimo - primeiro) / primeiro) * 100, 2)


def main():
    parser = argparse.ArgumentParser(description="Consulta dados de ações via Yahoo Finance")
    parser.add_argument("--ticker", default="AAPL", help="Símbolo da ação (default: AAPL)")
    parser.add_argument("--period", default="1mo", help="Período: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max")
    args = parser.parse_args()

    print(f"\nConsultando {args.ticker} - Período: {args.period}")
    dados = obter_dados_acao(args.ticker, args.period)

    if dados.empty:
        print("Nenhum dado encontrado.")
        return

    print(dados.tail())
    ganho = calcular_ganho(dados)
    print(f"\nVariação no período: {ganho:+.2f}%")


if __name__ == "__main__":
    main()
