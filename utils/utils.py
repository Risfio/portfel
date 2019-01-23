"""
UTILS package.


Для загрузки данных так же можно рассмотреть https://www.finam.ru/profile/moex-akcii/gazprom/export/

"""
import pandas as pd


def si_prices_volumes(filepath):
    """
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
    :return: DataFrame
    """
    df = pd.read_csv(filepath, sep=";")
    return df

