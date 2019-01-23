"""
PORTFEL package.

Initial file for portfel package.

SiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSi
Получаем CSV с данными по фьючерсу на бакс:
    идем на mfd.ru
    забиваем в поиск наш фьючерс
    выбираем функцию экспорт в CVS или MetaStock
    выбираем таймфрейм - день
    интервал - [слева]дата на год меньше текущей и [справа]текущая
    формат : выбираем текстовый и "каждый тикер в отдельном файле"
    формат даты/времени - yyyyMMdd HHmmss
    разделитель полей : точка с запятой
    десятичный разделитель : точка
    формат записи : TICKER,PER,DATE,TIME,OPEN,HIGH,LOW,CLOSE,VOL,OPENINT
SiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSiSi

"""

if __name__ == "__main__":
    print("It OK if using python -m portfel")

