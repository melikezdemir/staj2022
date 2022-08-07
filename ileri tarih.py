import datetime
today=datetime.date.today()
ileri_tarih=datetime.timedelta(days=30)
yeni_tarih=today+ileri_tarih
yeni_tarih
yeni_tarih.strftime('%c')
