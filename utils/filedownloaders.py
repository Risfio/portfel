"""

Usefull functions for download from data from files.

"""

from pandas import DataFrame as pd


def Si_from_CSV(filepath, sep=";"):
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

    Загружаем в DataFrame данные по нужному фьючерсу Si.

    :param filepath: полный путь к .csv файлу (как получить - описание выше)
    :param sep: разделитель для значений должен быть " ; "
    :return: возвращает DataFrame с загруженными данными для фьючерса Si
    """
    return pd.read_csv(filepath)

