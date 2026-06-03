from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.db import migrations

from datetime import datetime, timedelta
import time

def new_catalog(apps, schema_editor):

    # Суперпользователь id=1
    user = User.objects.create_superuser(username='root',
    email='shop260222@mail.ru',
    password='SsNn5678+-@')
    print("Суперпользователь создан")
    
    # Группа менеджеров
    managers = Group.objects.get_or_create(name = 'Managers')
    managers = Group.objects.get(name='Managers')
    print("Группа менеджеров создана")
    
    # Пользователь с ролью менеджера id=2
    user = User.objects.create_user(username='manager', password='Ss0066+-')
    managers.user_set.add(user)
    print("Менеджер добавлен в группу менеджеров")

    # Простые пользователи id=3...27 
    user = User.objects.create_user(username='user1', password='Uu0066+-', email='user1@mail.ru', first_name='Дина', last_name='Мусина')
    user = User.objects.create_user(username='user2', password='Uu0066+-', email='user2@mail.ru', first_name='Адия', last_name='Жунусова')
    user = User.objects.create_user(username='user3', password='Uu0066+-', email='user3@mail.ru', first_name='Айнура', last_name='Кенина')
    user = User.objects.create_user(username='user4', password='Uu0066+-', email='user4@mail.ru', first_name='Рустем', last_name='Какимов')
    user = User.objects.create_user(username='user5', password='Uu0066+-', email='user5@mail.ru', first_name='Алишер', last_name='Кабдуалиев')
    user = User.objects.create_user(username='user6', password='Uu0066+-', email='user6@mail.ru', first_name='Бауржан', last_name='Арыкбаев')
    user = User.objects.create_user(username='user7', password='Uu0066+-', email='user7@mail.ru', first_name='Алишер', last_name='Танатаров')
    user = User.objects.create_user(username='user8', password='Uu0066+-', email='user8@mail.ru', first_name='Мерует', last_name='Искакова')
    user = User.objects.create_user(username='user9', password='Uu0066+-', email='user9@mail.ru', first_name='Ольга', last_name='Муравьева')
    user = User.objects.create_user(username='user10', password='Uu0066+-', email='user10@mail.ru', first_name='Ақжарқын', last_name='Сансызбаева')
    user = User.objects.create_user(username='user11', password='Uu0066+-', email='user11@mail.ru', first_name='Арайлым', last_name='Алматова')
    user = User.objects.create_user(username='user12', password='Uu0066+-', email='user12@mail.ru', first_name='Айгерім', last_name='Дүйсенбиева')
    user = User.objects.create_user(username='user13', password='Uu0066+-', email='user13@mail.ru', first_name='Салтанат', last_name='Зиноллаева')
    user = User.objects.create_user(username='user14', password='Uu0066+-', email='user14@mail.ru', first_name='Сейтқасым', last_name='Болат')
    user = User.objects.create_user(username='user15', password='Uu0066+-', email='user15@mail.ru', first_name='Сара', last_name='Фазилова')
    user = User.objects.create_user(username='user16', password='Uu0066+-', email='user16@mail.ru', first_name='Бектас', last_name='Ерсейіт')
    user = User.objects.create_user(username='user17', password='Uu0066+-', email='user17@mail.ru', first_name='Диас', last_name='Мырзаш')
    user = User.objects.create_user(username='user18', password='Uu0066+-', email='user18@mail.ru', first_name='Нұржан', last_name='Жүрсінбек')
    user = User.objects.create_user(username='user19', password='Uu0066+-', email='user19@mail.ru', first_name='Дина', last_name='Жағыпар')
    user = User.objects.create_user(username='user20', password='Uu0066+-', email='user20@mail.ru', first_name='Жастілек', last_name='Жасталап')
    user = User.objects.create_user(username='user21', password='Uu0066+-', email='user21@mail.ru', first_name='Еркебұлан', last_name='Қадыхан')
    user = User.objects.create_user(username='user22', password='Uu0066+-', email='user22@mail.ru', first_name='Молдир', last_name='Бутабекова')
    user = User.objects.create_user(username='user23', password='Uu0066+-', email='user23@mail.ru', first_name='Аружан', last_name='Таурбекова')
    user = User.objects.create_user(username='user24', password='Uu0066+-', email='user24@mail.ru', first_name='Алтынай', last_name='Қожанова')
    user = User.objects.create_user(username='user25', password='Uu0066+-', email='user25@mail.ru', first_name='Эльнара', last_name='Иминова')
    print("Созданы простые пользователи")

    ##### Организации #####

    Organization = apps.get_model("product", "Organization")

    organization = Organization()
    organization.title='LG Electronics Almaty Kazakhstan'
    organization.address='Абай даңғылы 42, Алматы 050040'
    organization.phone='8 (727) 346 7837'
    organization.save()

    organization = Organization()
    organization.title='«Самсунг Электроникс Орталық Еуразия» ЖШС'
    organization.address='Әл-Фараби даңғылы 36-ғимарат, Б блогы, 3-қабат, Алматы 050059'
    organization.phone='+77273211212'
    organization.save()

    organization = Organization()
    organization.title='«Хуавей Текнолоджиз Қазақстан» ЖШС'
    organization.address='Достық даңғылы 210Б, 1-блок, 11-қабат, «KOKTEM GRAND» БО 050051; Алматы қ.'
    organization.phone='+7 (727) 344 09 99'
    organization.save()

    organization = Organization()
    organization.title='STN distribution'
    organization.address='Қазақстан, 050012, Алматы, Мұратбаев көшесі, 180-үй, 201-кеңсе, "Гермес" БО'
    organization.phone='+7 (727) 333 0 999'
    organization.save()

    organization = Organization()
    organization.title='Lenovo Shop Kazakhstan'
    organization.address='Қазақстан Республикасы, 050060, Алматы қ., Тәжібаева көшесі 184, 104-кеңсе'
    organization.phone='+7 (705) 674-89-09'
    organization.save()

    organization = Organization()
    organization.title='Canon Ru'
    organization.address='Алматы қ., Қазақстан, Әл-Фараби даңғылы 7, "Нұрлы-тау" БО'
    organization.phone='+7 727 277 77 95'
    organization.save()

    organization = Organization()
    organization.title='HP inc.'
    organization.address='77/7, Al-Farabi Ave., 6th Floor (West Wing) P.C. 050040 Almaty Kazakhstan'
    organization.phone='+7-727-356-2180'
    organization.save()

    organization = Organization()
    organization.title='«АСБИС Қазақстан» ЖШС'
    organization.address='050018, Қазақстан Республикасы, Алматы қ., Жетісу ауданы, Түлкібас көшесі, 2-үй'
    organization.phone='+7 727 390 46 06'
    organization.save()

    print("Организации добавлены")

    ##### Приходные накладные  #####

    Invoice = apps.get_model("product", "Invoice")
    
    invoice = Invoice()
    invoice.organization_id = 4
    invoice.datei = datetime.now() - timedelta(days=45)
    invoice.numb = 1
    invoice.save()

    invoice = Invoice()
    invoice.organization_id = 2
    invoice.datei = datetime.now() - timedelta(days=44)
    invoice.numb = 2
    invoice.save()

    invoice = Invoice()
    invoice.organization_id = 8
    invoice.datei = datetime.now() - timedelta(days=43)
    invoice.numb = 3
    invoice.save()

    invoice = Invoice()
    invoice.organization_id = 4
    invoice.datei = datetime.now() - timedelta(days=42)
    invoice.numb = 4
    invoice.save()

    invoice = Invoice()
    invoice.organization_id = 8
    invoice.datei = datetime.now() - timedelta(days=41)
    invoice.numb = 5
    invoice.save()

    print("Приходные накладные добавлены")

    ##### Категория товара #####

    Category = apps.get_model("product", "Category")

    category = Category()
    category.title='Смартфон'   
    category.save()

    category = Category()
    category.title='Түймелі телефон'   
    category.save()

    category = Category()
    category.title='Смарт-сағат'   
    category.save()

    category = Category()
    category.title='Құлаққап'   
    category.save()

    category = Category()
    category.title='Планшет'   
    category.save()

    category = Category()
    category.title='Электронды кітап'   
    category.save()
    
    print("Категория товара добавлена")

    ##### Каталог товаров #####
    
    Catalog = apps.get_model("product", "Catalog")

    catalog = Catalog()
    catalog.invoice_id = 1
    catalog.code='159421'
    catalog.category_id=1
    catalog.title='Tecno POP 5, 32Gb, Ice Lake Green (BD2p) смартфоны'
    catalog.info='POP 5 смартфоны кеңірек қарау және көруге ыңғайлы болу үшін нүкте тәрізді ойығы бар классикалық 6.1" HD+ экранымен жабдықталған. Сондай-ақ POP 5 экраны аса жоғары ажыратымдылыққа (720x1560) ие, бұл неғұрлым анық әрі әсерлі кескін береді.'
    catalog.details='Экран өлшемі, дюйм: 6.1; Экран ажыратымдылығы: 1560 x 720; Матрица түрі: IPS; Жедел жад көлемі: 2 Гб; Кірістірілген жад көлемі: 32 Гб; Процессор моделі: SC7731e; Процессор жиілігі: 1.3 ГГц; Негізгі камера, Мп: 5; Фронталды камера, Мп: 5; Сымсыз интерфейстер: Wi-Fi, Bluetooth; Батарея сыйымдылығы: 5000 мАч'
    catalog.price=38990
    catalog.quantity=10
    catalog.photo='images/product01.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 1
    catalog.code='151551'
    catalog.category_id=1
    catalog.title='Tecno POP 4 Pro, 16Gb, Cosmic Shine (BC3) смартфоны'
    catalog.info='POP 4 Pro телефонында диагоналі 6.52 дюйм болатын тамшы тәрізді ойығы бар классикалық экран қолданылады. Дисплейдің үлкен өлшемі мен экран мен корпус өлшемдерінің мінсіз арақатынасы жақсырақ көрсету сапасына қол жеткізуге мүмкіндік береді.'
    catalog.details='Экран өлшемі, дюйм: 6.52; Экран ажыратымдылығы: 1200 x 540; Жедел жад көлемі: 1 Гб; Кірістірілген жад көлемі: 16 Гб; Процессор моделі: MT6739WA; Процессор жиілігі: 1.25 ГГц; Негізгі камера, Мп: 8; Фронталды kamera, Мп: 8; Сымсыз интерфейстер: Wi-Fi, Bluetooth; Батарея сыйымдылығы: 5000 мАч'
    catalog.price=39990
    catalog.quantity=10
    catalog.photo='images/product02.jpg'
    catalog.save()
    print(catalog.id)
    
    catalog = Catalog()
    catalog.invoice_id = 1
    catalog.code='151555'
    catalog.category_id=1
    catalog.title='Tecno Spark 6, 64Gb, Comet Black (KE7) смартфоны'
    catalog.info='Орталық процессордың есептеу қуаты 60%-ға, графикалық процессордың өнімділігі 26%-ға артты. Қуатты процессор құрылғының сіз ойламаған тұрақты әрі бірқалыпты жұмысын қамтамасыз етеді және ойындардың тағы бір керемет рахатқа айналуына кепілдік береді.'
    catalog.details='Экран өлшемі, дюйм: 6.8; Экран ажыратымдылығы: 1640 x 720 [20.5:9]; Матрица түрі: IPS; Жедел жад көлемі: 4 Гб; Кірістірілген жад көлемі: 64 Гб; Процессор моделі: Helio G70; Процессор жиілігі: 2 ГГц + 1.7 ГГц; Негізгі камера, Мп: 16 + 2 + 2 + 2; Фронталды камера, Мп: 8; Сымсыз интерфейстер: Wi-Fi, Bluetooth; Батарея сыйымдылығы: 5000 мАч'
    catalog.price=64990
    catalog.quantity=10
    catalog.photo='images/product03.jpg'
    catalog.save()
    print(catalog.id)
    
    catalog = Catalog()
    catalog.invoice_id = 1
    catalog.code='149582'
    catalog.category_id=1
    catalog.title='Tecno POP 2F, 16Gb, Midnight Black (B1f) смартфоны'
    catalog.info='16 ГБ жадтың арқасында сүйікті әрі қымбат естеліктеріңізді сақтауға көбірек орын болады. Қойманы кеңейту — таңғажайып пайдаланушы интерфейсін ұсына отырып, ең жоғары өнімділікке қол жеткізудің тамаша қадамы.'
    catalog.details='Экран өлшемі, дюйм: 5.5; Экран ажыратымдылығы: 960 x 480 [18:9]; Жедел жад көлемі: 1 Гб; Кірістірілген жад көлемі: 16 Гб; Процессор моделі: MT6582; Процессор жиілігі: 1.3 ГГц; Негізгі камера, Мп: 5; Фронталды камера, Мп: 8; Сымсыз интерфейстер: Wi-Fi, Bluetooth; Батарея сыйымдылығы: 2400 мАч'
    catalog.price=27990
    catalog.quantity=10
    catalog.photo='images/product04.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 1
    catalog.code='151549'
    catalog.category_id=1
    catalog.title='Tecno POP 3, 16Gb, Sandstone Black (BB2) смартфоны'
    catalog.info='16 ГБ ТЖҚ (Тұрақты жад құрылғысы) арқасында сүйікті естеліктеріңіз бен маңызды файлдарыңызды сақтауға көбірек орын болады. Орын босату үшін жиі тазалау туралы уайым азырақ. Практикалық және әрқашан тамаша.'
    catalog.details='Экран өлшемі, дюйм: 5.7; Экран ажыратымдылығы: 960 x 480 [18:9]; Матрица түрі: TN; Жедел жад көлемі: 1 Гб; Кірістірілген жад көлемі: 16 Гб; Процессор моделі: MT6580; Процессор жиілігі: 1.3 ГГц; Негізгі камера, Мп: 5; Фронталды камера, Мп: 8; Сымсыз интерфейстер: Wi-Fi, Bluetooth; Батарея сыйымдылығы: 3500 мАч'
    catalog.price=28990
    catalog.quantity=10
    catalog.photo='images/product05.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 2
    catalog.code='159457'
    catalog.category_id=1
    catalog.title='Samsung Galaxy A03 Core, 32Gb, Black (SM-A032F) смартфоны'
    catalog.info='V-тәрізді ойығы бар 6.5 дюймдік экранмен қолжетімділік шекарасын кеңейтіңіз. HD+ технологиясының арқасында Galaxy A03 Core дисплейі жарқын, анық және таза суретті көрсетеді.'
    catalog.details='Экран өлшемі, дюйм: 6.5; Экран ажыратымдылығы: 1600 x 720 [20:9]; Жедел жад көлемі: 2 Гб; Кірістірілген жад көлемі: 32 Гб; Процессор моделі: SC9863A; Процессор жиілігі: 1.6 ГГц + 1.2 ГГц; Негізгі камера, Мп: 8; Фронталды камера, Мп: 5; Сымсыз интерфейстер: Wi-Fi, Bluetooth; Батарея сыйымдылығы: 5000 мАч'
    catalog.price=48990
    catalog.quantity=10
    catalog.photo='images/product06.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 2
    catalog.code='156712'
    catalog.category_id=1
    catalog.title='Samsung Galaxy A22, 64Gb, White (SM-A225F) смартфоны'
    catalog.info='HD+ ажыратымдылығы мен 600 нитке дейінгі жарықтығы бар Super AMOLED 6.4\'\' Infinity-U экранындағы егжей-тегжейлі кескіннен ләззат алыңыз. Кеңейтілген экранның арқасында сіз көбірек көресіз, ал аса бірқалыпты айналдыру ойын сеансы немесе экрандағы кескінді парақтау кезінде ыңғайлы көруді қамтамасыз етеді.'
    catalog.details='Экран өлшемі, дюйм: 6.4 / Экран ажыратымдылығы: 1600 х 720 [20:9] / Матрица түрі: Super AMOLED / Жедел жад көлемі: 4 Гб / Кірістірілген жад көлемі: 64 Гб / Процессор моделі: MT6769V/CTZA / Процессор жиілігі: 2.0 ГГц + 1.8 ГГц / Негізгі камера ажыратымдылығы: 48 Мп + 8 Мп + 2 Мп + 2 Мп / Фронталды камера ажыратымдылығы: 13 Мп / Сымсыз интерфейстер: Wi-Fi; Bluetooth; NFC / Батарея сыйымдылығы: 5000 мАч'
    catalog.price=90100
    catalog.quantity=10    
    catalog.photo='images/product07.jpg'
    catalog.save()
    print(catalog.id)
   
    catalog = Catalog()
    catalog.invoice_id = 2
    catalog.code='153241'
    catalog.category_id=1
    catalog.title='Samsung Galaxy A02, 32Gb, Black (SM-A022G) смартфоны'
    catalog.info='Камераға арналған V-тәрізді ойығы бар үлкен 6.5 дюймдік HD+ экраны мазмұнға толықтай ену үшін жасалған.'
    catalog.details='Экран өлшемі, дюйм: 6.5; Экран ажыратымдылығы: 1600 x 720 [20:9]; Матрица түрі: TFT; Жедел жад көлемі: 2 Гб; Кірістірілген жад көлемі: 32 Гб; Процессор моделі: MT6739; Процессор жиілігі: 1.5; Негізгі камера, Мп: 13 + 2; Фронталды kamera, Мп: 5; Сымсыз интерфейстер: Wi-Fi, Bluetooth; Батарея сыйымдылығы: 5000 мАч'
    catalog.price=53990
    catalog.quantity=10
    catalog.photo='images/product08.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 2
    catalog.code='156722'
    catalog.category_id=1
    catalog.title='Samsung Galaxy A12, 32Gb, Blue (SM-A127F) смартфоны'
    catalog.info='Камераға арналған V-тәрізді ойығы бар үлкен 6.5 дюймдік HD+ экраны мазмұнға толықтай ену үшін жасалған. HD+ технологиясын қолдаудың арқасында Galaxy A12-дегі сурет жарқын әрі қанық.'
    catalog.details='Экран өлшемі, дюйм: 6.5; Экран ажыратымдылығы: 1600 x 720 [20:9]; Матрица түрі: TFT; Жедел жад көлемі: 3 Гб; Кірістірілген жад көлемі: 32 Гб; Процессор моделі: 850; Процессор жиілігі: 2 ГГц; Негізгі камера, Мп: 48 + 5 + 2 + 2; Фронталды камера, Мп: 8; Сымсыз интерфейстер: Wi-Fi, Bluetooth, NFC; Батарея сыйымдылығы: 5000 мАч'
    catalog.price=69990
    catalog.quantity=10
    catalog.photo='images/product09.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 2
    catalog.code='153441'
    catalog.category_id=1
    catalog.title='Samsung Galaxy A32, 64Gb, Awesome Black (SM-A325F) смартфоны'
    catalog.info='Тіпті ашық күндізгі жарықта да тамаша көрінетін, FHD+ ажыратымдылығы мен 800 нитке дейінгі жарықтығы бар Super AMOLED 6.4\'\' Infinity-U экранындағы егжей-тегжейлі кескіннен ләззат алыңыз. "Eye Comfort Shield" көзді қорғау функциясы көк жарық деңгейін төмендетеді, ал аса бірқалыпты айналдыру ойын сеансы немесе экрандағы кескінді парақтау кезінде ыңғайлы көруді қамтамасыз етеді.'
    catalog.details='Экран өлшемі, дюйм: 6.4; Экран ажыратымдылығы: 2400 x 1080 [20:9]; Матрица түрі: Super AMOLED; Жедел жад көлемі: 4 Гб; Кірістірілген жад көлемі: 64 Гб; Процессор моделі: Helio G80; Процессор жиілігі: 2 ГГц + 1.8 ГГц; Негізгі камера, Мп: 64 + 8 + 5 + 5; Фронталды камера, Мп: 20; Сымсыз интерфейстер: Wi-Fi, Bluetooth, NFC; Батарея сыйымдылығы: 5000 мАч'
    catalog.price=199990
    catalog.quantity=10
    catalog.photo='images/product10.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 3
    catalog.code='159919'
    catalog.category_id=1
    catalog.title='Xiaomi Redmi 9C, 128Gb, Midnight Gray (M2006C3MG) смартфоны'
    catalog.info='Смартфон'
    catalog.details='Экран өлшемі, дюйм: 6.52 / Экран ажыратымдылығы: 1600 х 720 [20:9] / Матрица түрі: IPS / Жедел жад көлемі: 4 Гб / Кірістірілген жад көлемі: 64 Гб / Процессор моделі: Snapdragon 460 / Процессор жиілігі: 1.8 ГГц / Негізгі камера ажыратымдылығы: 13 Мп + 2 Мп + 2 Мп / Фронталды камера ажыратымдылығы: 8 Мп / Сымсыз интерфейстер: Wi-Fi; Bluetooth / Батарея сыйымдылығы: 5000 мАч'
    catalog.price=69900
    catalog.quantity=10
    catalog.photo='images/product11.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 3
    catalog.code='147507'
    catalog.category_id=1
    catalog.title='Xiaomi Redmi 9A, 32Gb, Granite Grey (M2006C3LG) смартфоны'
    catalog.info='Xiaomi Redmi 9A — бұл бюджеттік смартфонның нұсқасы, оның басты ерекшеліктері диагоналі 6.53" үлкен экран және 5000 мАч сыйымдылықты батарея болып табылады. Негізгі және фронталды AI камералары (тиісінше 13 Мп және 5 Мп) тамаша әрі сапалы фотосуреттерді оңай түсіруге мүмкіндік береді.'
    catalog.details='Экран өлшемі, дюйм: 6.53; Экран ажыратымдылығы: 1600 x 720 [20:9]; Жедел жад көлемі: 2 Гб; Кірістірілген жад көлемі: 32 Гб; Процессор моделі: Helio G25; Процессор жиілігі: 2.0 ГГц; Негізгі камера, Мп: 13; Фронталды камера, Мп: 5; Сымсыз интерфейстер: Wi-Fi, Bluetooth; Батарея сыйымдылығы: 5000 мАч'
    catalog.price=54990
    catalog.quantity=10
    catalog.photo='images/product12.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 3
    catalog.code='145755'
    catalog.category_id=1
    catalog.title='Xiaomi Redmi Note 9S, 64Gb, Interstellar Grey смартфоны'
    catalog.info='Xiaomi-де мұндай камералар әлі болған емес. Ең алдымен камералардың шаршы блогы көзге түседі. 4 камера шағын аумақты алып, құрылғының жалпы дизайнымен үйлесімді көрінеді.'
    catalog.details='Экран өлшемі, дюйм: 6.67; Экран ажыратымдылығы: 2400 x 1080 [20:9]; Матрица түрі: IPS; Жедел жад көлемі: 4 Гб; Кірістірілген жад көлемі: 64 Гб; Процессор моделі: Snapdragon 720G; Процессор жиілігі: 2.3 ГГц; Негізгі камера, Мп: 48 + 8 + 5 + 2; Фронталды камера, Мп: 16; Сымсыз интерфейстер: Wi-Fi, Bluetooth, IrDA; Батарея сыйымдылығы: 5020 мАч'
    catalog.price=88900
    catalog.quantity=10
    catalog.photo='images/product13.jpg'
    catalog.save()
    print(catalog.id)
    
    catalog = Catalog()
    catalog.invoice_id = 3
    catalog.code='157496'
    catalog.category_id=1
    catalog.title='Xiaomi Redmi 10, 4Gb, 64Gb, Sea Blue (21061119AG) смартфоны'
    catalog.info='Xiaomi Redmi 10 — қуатты MediaTek Helio G88 процессорының алғашқы иегері. Мүлдем жаңа чип анық фотосуреттерді және жақсартылған ойын процесін қамтамасыз етеді.'
    catalog.details='Экран өлшемі, дюйм: 6.5; Экран ажыратымдылығы: 2400 x 1080 [20:9]; Жедел жад көлемі: 4 Гб; Кірістірілген жад көлемі: 64 Гб; Процессор моделі: Helio G88; Процессор жиілігі: 2.0 ГГц + 1.8 ГГц; Негізгі камера, Мп: 50 + 8 + 2 + 2; Фронталды камера, Мп: 8; Сымсыз интерфейстер: Wi-Fi, Bluetooth, IrDA; Батарея сыйымдылығы: 5000 мАч'
    catalog.price=89990
    catalog.quantity=10
    catalog.photo='images/product14.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 3
    catalog.code='159921'
    catalog.category_id=1
    catalog.title='Xiaomi Redmi Note 11, 64Gb, Twilight Blue (2201117TG) смартфоны'
    catalog.info='Смартфон'
    catalog.details='Экран өлшемі, дюйм: 6.43; Экран ажыратымдылығы: 2400 x 1080 [20:9]; Матрица түрі: AMOLED; Жедел жад көлемі: 4 Гб; Кірістірілген жад көлемі: 64 Гб; Процессор моделі: Snapdragon 680; Процессор жиілігі: 2.4 ГГц + 1.9 ГГц; Негізгі камера, Мп: 50 + 8 + 2 + 2; Фронталды камера, Мп: 13; Сымсыз интерфейстер: Wi-Fi, Bluetooth, IrDA; Батарея сыйымдылығы: 5000 мАч'
    catalog.price=109990
    catalog.quantity=10
    catalog.photo='images/product15.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 4
    catalog.code='153536'
    catalog.category_id=1
    catalog.title='Meizu M10, 2Gb, 32Gb, Phantom Black (M918H) смартфоны'
    catalog.info='Смартфон'
    catalog.details='Экран өлшемі, дюйм: 6.5 / Экран ажыратымдылығы: 1600 х 720 [20:9] / Жедел жад көлемі: 2 Гб / Кірістірілген жад көлемі: 32 Гб / Процессор моделі: Helio P25 / Процессор жиілігі: 2.5 ГГц / Негізгі камера ажыратымдылығы: 13 Мп + 2 Мп + 2 Мп / Фронталды камера ажыратымдылығы: 8 Мп / Сымсыз интерфейстер: Wi-Fi; Bluetooth / Батарея сыйымдылығы: 4000 мАч'
    catalog.price=45900
    catalog.quantity=10
    catalog.photo='images/product16.jpg'
    catalog.save()
    print(catalog.id)
    
    catalog = Catalog()
    catalog.invoice_id = 4
    catalog.code='154927'
    catalog.category_id=1
    catalog.title='OPPO A54, 64Gb, Black (CPH2239) смартфоны'
    catalog.info='Артқы қақпағының бірегей дизайны мен 0.2 мм жіңішке жақтауы бар 3D-корпус талғампаз көрініп қана қоймайды, сонымен қатар ұзақ пайдалану кезінде де ыңғайлы.'
    catalog.details='Экран өлшемі, дюйм: 6.51; Экран ажыратымдылығы: 1600 x 720 [20:9]; Матрица түрі: IPS; Жедел жад көлемі: 4 Гб; Кірістірілген жад көлемі: 64 Гб; Процессор моделі: Helio P35; Процессор жиілігі: 2.3 ГГц; Негізгі камера, Мп: 13 + 2 + 2; Фронталды камера, Мп: 16; Сымсыз интерфейстер: Wi-Fi, Bluetooth, NFC; Батарея сыйымдылығы: 5000 мАч'
    catalog.price=94900
    catalog.quantity=10
    catalog.photo='images/product17.jpg'
    catalog.save()
    print(catalog.id)
    
    catalog = Catalog()
    catalog.invoice_id = 4
    catalog.code='Артикул '
    catalog.category_id=1
    catalog.title='OPPO A74, 128Gb, Black (CPH2219) смартфоны'
    catalog.info='Құрылғы экранына кірістірілген заманауи сканер саусақ іздерін жылдам әрі жоғары дәлдікпен оқиды және смартфонды бір түрту арқылы бұғаттан шығаруға мүмкіндік береді.'
    catalog.details='Экран өлшемі, дюйм: 6.43; Экран ажыратымдылығы: 2400 x 1080 [20:9]; Матрица түрі: AMOLED; Жедел жад көлемі: 4 Гб; Кірістірілген жад көлемі: 128 Гб; Процессор моделі: Snapdragon 662; Процессор жиілігі: 1.8 ГГц + 2 ГГц; Негізгі камера, Мп: 48 + 2 + 2; Фронталды камера, Мп: 16; Сымсыз интерфейстер: Wi-Fi, Bluetooth, NFC; Батарея сыйымдылығы: 5000 мАч'
    catalog.price=119990
    catalog.quantity=10
    catalog.photo='images/product18.jpg'
    catalog.save()
    print(catalog.id)
    
    catalog = Catalog()
    catalog.invoice_id = 4
    catalog.code='150469'
    catalog.category_id=1
    catalog.title='OPPO Reno4 Lite, 8Gb, Black (CPH2125) смартфоны'
    catalog.info='Reno сериялы смартфондары OPPO модельдік қатарындағы ең жұқа және жеңіл болып табылады, мұндай құрылғылардың корпусы тегіс жұмырланған жиектерге ие, оларды пайдалану өте ыңғайлы.'
    catalog.details='Экран өлшемі, дюйм: 6.43; Экран ажыратымдылығы: 2400 x 1080 [20:9]; Матрица түрі: Super AMOLED; Жедел жад көлемі: 8 Гб; Кірістірілген жад көлемі: 128 Гб; Процессор моделі: Helio P95; Процессор жиілігі: 2.2 ГГц; Негізгі камера, Мп: 48 + 8 + 2 + 2; Фронталды камера, Мп: 16 + 2; Сымсыз интерфейстер: Wi-Fi, Bluetooth, NFC; Батарея сыйымдылығы: 4000 мАч'
    catalog.price=125990
    catalog.quantity=10
    catalog.photo='images/product19.jpg'
    catalog.save()
    print(catalog.id)
    
    catalog = Catalog()
    catalog.invoice_id = 4
    catalog.code='154925'
    catalog.category_id=1
    catalog.title='OPPO Reno5 Lite, 128Gb, Black (CPH2205) смартфоны'
    catalog.info='Төрт объективі және жасанды интеллекті бар Reno5 Lite камерасы өмірдің барлық сәттерін түсіруге өте ыңғайлы. Макротүсірілімнен бастап аса кең бұрышты және зум-суреттерге дейін — Reno5 Lite өмір жолын жарқын әрі кристаллдай анық егжей-тегжейлермен көрсетеді.'
    catalog.details='Экран өлшемі, дюйм: 6.43; Экран ажыратымдылығы: 2400 x 1080 [20:9]; Матрица түрі: AMOLED; Жедел жад көлемі: 8 Гб; Кірістірілген жад көлемі: 128 Гб; Процессор моделі: Helio P95; Процессор жиілігі: 2.2 ГГц; Негізгі камера, Мп: 48 + 8 + 2 + 2; Фронталды камера, Мп: 32; Сымсыз интерфейстер: Wi-Fi, Bluetooth, NFC; Батарея сыйымдылығы: 4310 мАч'
    catalog.price=139990
    catalog.quantity=10
    catalog.photo='images/product20.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 5
    catalog.code='155256'
    catalog.category_id=2
    catalog.title='Nokia 125 DS, Black ұялы телефоны'
    catalog.info='Ұялы телефон'
    catalog.details='Экран өлшемі, дюйм: 2.4 / Экран ажыратымдылығы: 240 x 320 / Кірістірілген жад көлемі: 4 Мб / Батарея сыйымдылығы: 1020 мАч'
    catalog.price=13390
    catalog.quantity=10
    catalog.photo='images/product21.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 5
    catalog.code='151280'
    catalog.category_id=2
    catalog.title='Tecno T454, Champagne Gold ұялы телефоны'
    catalog.info='Ұялы телефон'
    catalog.details='Экран өлшемі, дюйм: 2.8 / Экран ажыратымдылығы: 240 x 320 / Жедел жад көлемі: 4 Мб / Кірістірілген жад көлемі: 4 Мб / Сымсыз интерфейстер: Bluetooth / Батарея сыйымдылығы: 1500 мАч'
    catalog.price=7990
    catalog.quantity=10
    catalog.photo='images/product22.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 5
    catalog.code='158563'
    catalog.category_id=2
    catalog.title='TeXet TM-122, Black ұялы телефоны'
    catalog.info='TM-122 — тек қоңыраулар мен SMS-пен шектелетін қарапайым телефон емес. FM-радио, кірістірілген плеер және басқа да көптеген функциялар мобильді құрылғының қолданылу аясын кеңейтеді және оның әлеуетін барынша жайлылықпен толық іске асыруға мүмкіндік береді.'
    catalog.details='Экран өлшемі, дюйм: 1.77; Экран ажыратымдылығы: 128 x 160; Батарея сыйымдылығы: 600 мАч'
    catalog.price=4590
    catalog.quantity=10
    catalog.photo='images/product23.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 5
    catalog.code='139072'
    catalog.category_id=2
    catalog.title='Philips Xenium E109, Red ұялы телефоны'
    catalog.info='Егер сізге стиліңізді көрсету үшін сәннен озып тұратын дизайн қажет болса, онда жоғары сапалы әрленген бұл жалпақ, заманауи конструкцияның теңдесі жоқ.'
    catalog.details='Экран өлшемі, дюйм: 1.77; Экран ажыратымдылығы: 128 x 160; Матрица түрі: TFT; Жедел жад көлемі: 32 Мб; Кірістірілген жад көлемі: 32 Мб; Процессор моделі: MT6261D; Батарея сыйымдылығы: 1000 мАч'
    catalog.price=8790
    catalog.quantity=10
    catalog.photo='images/product24.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 5
    catalog.code='149529'
    catalog.category_id=2
    catalog.title='Prestigio Muze H1, Black ұялы телефоны'
    catalog.info='Бұрыштары жұмырланған шағын 2.4 дюймдік телефонды қолда ұстау өте жағымды. Ал кішігірім өлшемдері мен 85 грамға дейінгі салмағының арқасында ол джинсы немесе күртеше қалтасына оңай сыйып кетеді.'
    catalog.details='Экран өлшемі, дюйм: 2.4; Экран ажыратымдылығы: 240 x 240; Матрица түрі: TFT; Жедел жад көлемі: 32 Мб; Кірістірілген жад көлемі: 32 Мб; Процессор моделі: Spreadtrum SC6531E; Сымсыз интерфейстер: Bluetooth; Батарея сыйымдылығы: 1400 мАч'
    catalog.price=6590
    catalog.quantity=10
    catalog.photo='images/product25.jpg'
    catalog.save()
    print(catalog.id)

    print("Каталог товаров добавлен")

    ##### Продажа + Доставка #####
    
    Sale = apps.get_model("product", "Sale")
    Delivery = apps.get_model("product", "Delivery")

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=30)
    sale.catalog_id = 1
    sale.price = 38990
    sale.quantity = 1
    sale.user_id = 3
    sale.rating = 5
    sale.details='Керемет телефон, бәрі жақсы жұмыс істейді. Камерасы тек зум режимінде өте жақсы түсіреді, матаның текстурасын егжей-тегжейлі етіп суретке тартады.'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=30)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Өтінім өңдеуге қабылданды'
    delivery.details='Өтінім өңдеуге қабылданды'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Тауар жолда'
    delivery.details='Тауар жолда'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Тауар қоймада'
    delivery.details='Тауар қоймада'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Өтінім жабылды, тауар жеткізілді'
    delivery.details='Өтінім жабылды, тауар жеткізілді'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()

    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=29)
    sale.catalog_id = 1
    sale.price = 38990
    sale.quantity = 1
    sale.user_id = 4
    sale.rating = 4
    sale.details='Жылдам жұмыс істейді, өте жақсы. Камерасы дірілдейді және сапасы аса жақсы емес.'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=29)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Өтінім өңдеуге қабылданды'
    delivery.details='Өтінім өңдеуге қабылданды'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Тауар жолда'
    delivery.details='Тауар жолда'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Тауар қоймада'
    delivery.details='Тауар қоймада'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Өтінім жабылды, тауар жеткізілді'
    delivery.details='Өтінім жабылды, тауар жеткізілді'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()

    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=28)
    sale.catalog_id = 6
    sale.price = 48990
    sale.quantity = 1
    sale.user_id = 5
    sale.rating = 5
    sale.details='Специально не стала сразу писать отзыв-сначала решила посмотреть в деле. Приятно удивлена: в диапазоне цен до 10 000 рублей считаю это лучший телефон. Покупался дочке на день рождения на 11 лет. Выглядит солидно-но не громоздко. Все игры тянет,вотс ап яндекс музыка, Ютуб детям, родительский контроль-все работает. Звук немного как из ведра-но для ребенка отлично. Громкий-память 32 uu,-более, чем достаточно. Камера четкая: подружек кошечек,видео -все сняли все красиво)'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=28)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Заявка принята в обработку'
    delivery.details='Заявка принята в обработку'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Товар в пути'
    delivery.details='Товар в пути'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Товар на складе'
    delivery.details='Товар на складе'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Заявка закрыта, товар доставлен'
    delivery.details='Заявка закрыта, товар доставлен'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()

    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=27)
    sale.catalog_id = 6
    sale.price = 48990
    sale.quantity = 1
    sale.user_id = 6
    sale.rating = 5
    sale.details='Жұмыс істеп тұр. Кеше әкелді. Ұзақ ойланып, таңдадым. Тек пікірлерге сүйеніп сатып алдым. Пікір жазатындардың бәріне рақмет. Оңай әрі қарапайым. Түсініп алдым. Жалпы қалыпты телефон.'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=27)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Өтінім өңдеуге қабылданды'
    delivery.details='Өтінім өңдеуге қабылданды'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Тауар жолда'
    delivery.details='Тауар жолда'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Тауар қоймада'
    delivery.details='Тауар қоймада'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Өтінім жабылды, тауар жеткізілді'
    delivery.details='Өтінім жабылды, тауар жеткізілді'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()
    
    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=26)
    sale.catalog_id = 11
    sale.price = 69900
    sale.quantity = 1
    sale.user_id = 7
    sale.rating = 5
    sale.details='Кәсіби шолу жасаудан аулақпын, мен сияқты қарапайым пайдаланушы үшін өз класы мен баға сегментіндегі тамаша жұмыс құрылғысы'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=26)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Өтінім өңдеуге қабылданды'
    delivery.details='Өтінім өңдеуге қабылданды'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Тауар жолда'
    delivery.details='Тауар жолда'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Тауар қоймада'
    delivery.details='Тауар қоймада'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Өтінім жабылды, тауар жеткізілді'
    delivery.details='Өтінім жабылды, тауар жеткізілді'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()

    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=25)
    sale.catalog_id = 11
    sale.price = 69900
    sale.quantity = 1
    sale.user_id = 8
    sale.rating = 5
    sale.details='Осы баға санатындағы тамаша телефон. Үлкен батареясы бірнеше күн бойы қуаттамауға мүмкіндік береді, әрине, егер ойын ойнамасаңыз). Камерасы орташа, бірақ телефон әдемі фотосуреттер түсіру үшін сатып алынған жоқ. Үлкен экраны плюс болып табылады, өйткені егде жастағы адамға алынды.'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=25)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Өтінім өңдеуге қабылданды'
    delivery.details='Өтінім өңдеуге қабылданды'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Тауар жолда'
    delivery.details='Тауар жолда'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Тауар қоймада'
    delivery.details='Тауар қоймада'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Өтінім жабылды, тауар жеткізілді'
    delivery.details='Өтінім жабылды, тауар жеткізілді'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()

    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=24)
    sale.catalog_id = 16
    sale.price = 45900
    sale.quantity = 1
    sale.user_id = 9
    sale.rating = 5
    sale.details='Бәрі жақсы, балаға сатып алдық, 3 Гб жедел жад толықтай жетеді.'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=24)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Өтінім өңдеуге қабылданды'
    delivery.details='Өтінім өңдеуге қабылданды'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Тауар жолда'
    delivery.details='Тауар жолда'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Тауар қоймада'
    delivery.details='Тауар қоймада'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Өтінім жабылды, тауар жеткізілді'
    delivery.details='Өтінім жабылды, тауар жеткізілді'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()
    
    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=23)
    sale.catalog_id = 16
    sale.price = 45900
    sale.quantity = 1
    sale.user_id = 10
    sale.rating = 4
    sale.details='Телефон қатпайды, экраны жарқын және менің телефоным мен мониторымдағы IPS матрицасынан көп қалыспайды.'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=23)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Өтінім өңдеуге қабылданды'
    delivery.details='Өтінім өңдеуге қабылданды'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Тауар жолда'
    delivery.details='Тауар жолда'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Тауар қоймада'
    delivery.details='Тауар қоймада'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Өтінім жабылды, тауар жеткізілді'
    delivery.details='Өтінім жабылды, тауар жеткізілді'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()

    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=22)
    sale.catalog_id = 21
    sale.price = 13390
    sale.quantity = 1
    sale.user_id = 11
    sale.rating = 3
    sale.details='Осы уақытқа дейін тамаша жұмыс істеп тұрған LG GS107 телефонымен салыстырамын, ол әлдеқайда қаттырақ шығады, радионы гарнитурасыз-ақ өте жақсы ұстайды, қуаты 5-7 күнге жетеді, бұл әлі өзінің түпнұсқа батареясымен. Nokia-ны параметрлері жағынан LG GS107-ге ұқсас болар деген үмітпен алған едім, бірақ ол әлдеқайда нашар болып шықты.'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=22)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Өтінім өңдеуге қабылданды'
    delivery.details='Өтінім өңдеуге қабылданды'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Тауар жолда'
    delivery.details='Тауар жолда'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Тауар қоймада'
    delivery.details='Тауар қоймада'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Өтінім жабылды, тауар жеткізілді'
    delivery.details='Өтінім жабылды, тауар жеткізілді'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()
    
    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=21)
    sale.catalog_id = 21
    sale.price = 13390
    sale.quantity = 1
    sale.user_id = 12
    sale.rating = 5
    sale.details='Үлкен батырмалар. Телефон 83 жастағы иесіне өте жақсы сәйкес келді. Көңілінен шықты.'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=21)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Өтінім өңдеуге қабылданды'
    delivery.details='Өтінім өңдеуге қабылданды'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Тауар жолда'
    delivery.details='Тауар жолда'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Тауар қоймада'
    delivery.details='Тауар қоймада'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Өтінім жабылды, тауар жеткізілді'
    delivery.details='Өтінім жабылды, тауар жеткізілді'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()

    print("Продажа + Доставка добавлен")

class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(new_catalog),
        migrations.RunSQL("""CREATE VIEW view_catalog AS
                        SELECT catalog.id, catalog.code, catalog.category_id, category.title AS category, catalog.title, catalog.info, catalog.details, catalog.price, catalog.quantity, catalog.photo, 
                        (SELECT AVG(rating) FROM sale WHERE sale.catalog_id = catalog.id) AS avg_rating,
                        (SELECT SUM(quantity) FROM sale WHERE sale.catalog_id = catalog.id) AS sale_quantity,
                        CASE 
                            WHEN (catalog.quantity - (SELECT SUM(quantity) FROM sale WHERE sale.catalog_id = catalog.id)) IS NULL 
                        THEN catalog.quantity 
                            ELSE (catalog.quantity - (SELECT SUM(quantity) FROM sale WHERE sale.catalog_id = catalog.id)) 
                        END
                        AS available
                        FROM catalog LEFT JOIN category ON catalog.category_id = category.id;"""),
        migrations.RunSQL("""CREATE VIEW view_sale AS
                        SELECT sale.id, username, saleday, catalog_id, view_catalog.category, view_catalog.title, info, code, sale.price, sale.quantity, sale.price*sale.quantity AS total, user_id, rating, sale.details,
                        (SELECT strftime('%d.%m.%Y',deliveryday) || ' - ' || movement FROM delivery WHERE sale_id = sale.id AND deliveryday = (SELECT MAX(deliveryday) AS Expr1 FROM delivery AS S WHERE  (sale_id = sale.id) )) AS final
                        FROM sale LEFT JOIN view_catalog ON sale.catalog_id = view_catalog.id
                        LEFT JOIN auth_user ON sale.user_id = auth_user.id"""),
        #migrations.RunSQL("""CREATE VIEW view_catalog AS
        #                SELECT catalog.id, catalog.code, catalog.category_id, category.title AS category, catalog.title, catalog.info, catalog.details, catalog.price, catalog.quantity, catalog.photo, 
        #                (SELECT AVG(rating) FROM sale WHERE sale.catalog_id = catalog.id) AS avg_rating,
        #                (SELECT SUM(quantity) FROM sale WHERE sale.catalog_id = catalog.id) AS sale_quantity,
        #                CASE WHEN (catalog.quantity - (SELECT SUM(quantity) FROM sale WHERE sale.catalog_id = catalog.id)) IS NULL 
        #                THEN catalog.quantity
        #                ELSE (catalog.quantity - (SELECT SUM(quantity) FROM sale WHERE sale.catalog_id = catalog.id))  
        #                END
        #                AS available
        #                FROM catalog LEFT JOIN category ON catalog.category_id = category.id"""),        
        #migrations.RunSQL("""CREATE VIEW view_sale AS
        #                SELECT sale.id, username, saleday, catalog_id, view_catalog.category, view_catalog.title, info, code, sale.price, sale.quantity, sale.price*sale.quantity AS total, user_id, rating, sale.details,
        #                (SELECT to_char( deliveryday, 'DD.MM.YYYY') || ' - ' || movement FROM delivery WHERE sale_id = sale.id AND deliveryday = (SELECT MAX(deliveryday) AS Expr1 FROM delivery AS S WHERE  (sale_id = sale.id) )) AS final
        #                FROM sale LEFT JOIN view_catalog ON sale.catalog_id = view_catalog.id
        #                LEFT JOIN auth_user ON sale.user_id = auth_user.id"""),
    ]
