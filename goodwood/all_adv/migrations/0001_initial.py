# Generated by Django 4.1.7 on 2023-03-22 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarActuator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=70, verbose_name='Привод')),
            ],
            options={
                'verbose_name': 'Привод',
                'verbose_name_plural': 'Привод',
            },
        ),
        migrations.CreateModel(
            name='CarBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=70, verbose_name='Кузов')),
            ],
            options={
                'verbose_name': 'Кузов',
                'verbose_name_plural': 'Кузов',
            },
        ),
        migrations.CreateModel(
            name='CarFuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=70, verbose_name='Топливо')),
            ],
            options={
                'verbose_name': 'Топливо',
                'verbose_name_plural': 'Топливо',
            },
        ),
        migrations.CreateModel(
            name='CarMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=70, verbose_name='Марка')),
            ],
            options={
                'verbose_name': 'Марка',
                'verbose_name_plural': 'Марки',
            },
        ),
        migrations.CreateModel(
            name='CarTransmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=70, verbose_name='Коробка')),
            ],
            options={
                'verbose_name': 'Коробка',
                'verbose_name_plural': 'Коробка',
            },
        ),
        migrations.CreateModel(
            name='Intention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=70, verbose_name='Намерение')),
            ],
            options={
                'verbose_name': 'Намерение',
                'verbose_name_plural': 'Намерение',
            },
        ),
        migrations.CreateModel(
            name='LawStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=70, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статус',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=70, verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
            },
        ),
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=45, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=70, verbose_name='Субъект')),
            ],
            options={
                'verbose_name': 'Субъект',
                'verbose_name_plural': 'Субъект',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=21, verbose_name='Вид сделки')),
            ],
            options={
                'verbose_name': 'Вид сделки',
                'verbose_name_plural': 'Вид сделки',
            },
        ),
        migrations.CreateModel(
            name='Adv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
                ('title', models.CharField(help_text='Это хелп', max_length=50, verbose_name='Наименование')),
                ('city', models.CharField(max_length=50, null=True, verbose_name='Город')),
                ('district_city', models.CharField(blank=True, default='', max_length=50, verbose_name='Район города')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/%d/')),
                ('user_name', models.CharField(max_length=50, null=True, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=50, null=True, verbose_name='Телефон')),
                ('content', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Цена')),
                ('subrubric', models.CharField(blank=True, choices=[(None, 'Выберите'), ('Транспортные средства', (('Автомобили', 'Автомобили'), ('Автомобильные запчасти', 'Автомобильные запчасти'), ('Водный транспорт и запчасти', 'Водный транспорт и запчасти'), ('Прицепы и дома', 'Прицепы и дома'), ('Мотоциклы, малая техника и запчасти', 'Мотоциклы, малая техника и запчасти'), ('Воздушные транспортные средства и запчасти', 'Воздушные транспортные средства и запчасти'), ('Другие транспортные средства', 'Другие транспортные средства'))), ('Электроника', (('Компьютеры и комплектующие', 'Компьютеры и комплектующие'), ('Оргтехника', 'Оргтехника'), ('Фото и видео', 'Фото и видео'), ('Телефоны и планшеты', 'Телефоны и планшеты'), ('Телевизоры и ТВ-приставки', 'Телевизоры и ТВ-приставки'), ('Другая электроника', 'Другая электроника'))), ('Недвижимость', (('Квартиры', 'Квартиры'), ('Дома', 'Дома'), ('Комнаты', 'Комнаты'), ('Участки', 'Участки'), ('Коммерческая', 'Коммерческая'))), ('Хозяйство', (('Искусство и антиквариат', 'Искусство и антиквариат'), ('Детские товары и игрушки', 'Детские товары и игрушкит'), ('Одежда', 'Одежда'), ('Сад и огород', 'Сад и огород'), ('Инструмент', 'Инструмент'), ('Мебель', 'Мебель'), ('Домашний декор', 'Домашний декор'), ('Бытовая техника', 'Бытовая техника'))), ('Досуг и хобби', (('Журналы, книги и издания', 'Журналы, книги и издания'), ('Животные', 'Животные'), ('Хобби', 'Хобби'), ('Знакомства', 'Знакомства'), ('Охота и рыбалка', 'Охота и рыбалка'), ('Часы и ювелирные изделия', 'Часы и ювелирные изделия'), ('Музыкальные инструменты', 'Музыкальные инструменты'), ('Спорт', 'Спорт'))), ('Работа', (('Бухгалтерский учет и аудит', 'Бухгалтерский учет и аудит'), ('IT, администрирование и поддержка', 'IT, администрирование и поддержка'), ('Реклама и маркетинг', 'Реклама и маркетинг'), ('Искусство и развлечение', 'Искусство и развлечение'), ('Автомобилестроение и механика', 'Автомобилестроение и механика'), ('Уход за детьми', 'Уход за детьми'), ('Обслуживание', 'Обслуживание'), ('Здравоохранение', 'Здравоохранение'), ('Гостиничный бизнес и туризм', 'Гостиничный бизнес и туризм'), ('Мода и красота', 'Мода и красота'), ('Графический дизайн и САПР', 'Графический дизайн и САПР'), ('Управление персоналом', 'Управление персоналом'), ('Установка и техническое обслуживание', 'Установка и техническое обслуживание'), ('Интернет и электронная коммерция', 'Интернет и электронная коммерция'), ('Правоохранительные органы, гос.управление', 'Правоохранительные органы, гос.управление'), ('Производство', 'Производство'), ('Менеджмент и управление', 'Менеджмент и управление'), ('Строительство', 'Строительство'), ('Горнодобывающая промышленность', 'Горнодобывающая промышленность'), ('Издательское дело, журналистика и СМИ', 'Издательское дело, журналистика и СМИ'), ('Закупки и мерчендайзинг', 'Закупки и мерчендайзинг'), ('Рестораны и общественное питание', 'Рестораны и общественное питание'), ('Розничная и оптовая торговля', 'Розничная и оптовая торговля'), ('Транспортные и складские услуги', 'Транспортные и складские услуги'), ('Ветеринарные услуги', 'Ветеринарные услуги'), ('Работа на дому', 'Работа на дому')))], max_length=70, null=True, verbose_name='Подрубрика')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано от')),
                ('update', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено  от')),
                ('street', models.CharField(blank=True, default='', max_length=50, verbose_name='Улица')),
                ('floors', models.CharField(blank=True, max_length=50, null=True, verbose_name='Этажей')),
                ('floor', models.CharField(blank=True, max_length=50, null=True, verbose_name='Этаж')),
                ('rooms', models.CharField(blank=True, max_length=50, null=True, verbose_name='Комнат')),
                ('square_rooms', models.FloatField(blank=True, null=True, verbose_name='Площадь комнат')),
                ('square_land', models.FloatField(blank=True, null=True, verbose_name='Площадь земли')),
                ('car_model', models.CharField(blank=True, max_length=50, null=True, verbose_name='Модель')),
                ('car_year', models.CharField(blank=True, max_length=50, null=True, verbose_name='Год')),
                ('car_color', models.CharField(blank=True, max_length=50, null=True, verbose_name='Цвет')),
                ('car_run', models.CharField(blank=True, max_length=50, null=True, verbose_name='Пробег')),
                ('car_engine_capacity', models.FloatField(blank=True, null=True, verbose_name='Объем двигателя')),
                ('who', models.CharField(blank=True, max_length=50, null=True, verbose_name='Кто')),
                ('whom', models.CharField(blank=True, max_length=50, null=True, verbose_name='Кого')),
                ('your_age', models.CharField(blank=True, max_length=50, null=True, verbose_name='Возраст Ваш')),
                ('intention_age', models.CharField(blank=True, max_length=50, null=True, verbose_name='Возраст поиска')),
                ('salary', models.CharField(blank=True, max_length=50, null=True, verbose_name='Зарплата от')),
                ('mode', models.CharField(blank=True, max_length=50, null=True, verbose_name='Режим работы')),
                ('car_actuator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='all_adv.caractuator', verbose_name='Привод')),
                ('car_body', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='all_adv.carbody', verbose_name='Кузов')),
                ('car_fuel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='all_adv.carfuel', verbose_name='Топливо')),
                ('car_mark', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='all_adv.carmark', verbose_name='Марка')),
                ('car_transmission', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='all_adv.cartransmission', verbose_name='Коробка')),
                ('intention', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='all_adv.intention', verbose_name='Намерение')),
                ('law_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='all_adv.lawstatus', verbose_name='Статус')),
                ('ower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='all_adv.subject', verbose_name='Субъект')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='all_adv.region', verbose_name='Регион')),
                ('rubric', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='all_adv.rubric', verbose_name='Рубрика')),
                ('transaction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='all_adv.transaction', verbose_name='Вид сделки')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['-published'],
            },
        ),
    ]
