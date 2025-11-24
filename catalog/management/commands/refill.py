from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):

        # Сначала создаем категории
        categories_data = [
            {
                "id": 1,
                "name": "Уличная Еда (Street Food)",
                "description": "Быстро, сытно, аутентично. Еда, которую едят стоя или на ходу. "
                               "Примеры: шаурма, хот-доги, тако, блинчики с начинкой, самоса, гамбургеры."
            },
            {
                "id": 2,
                "name": "Домашняя Кухня (Home Cooking)",
                "description": "С душой, для семьи, по рецептам. Еда, с которой ассоциируется уют и семья."
                               "Примеры: мамины пирожки, воскресный борщ, домашняя паста, тушеное мясо, запеканка."
            },
            {
                "id": 3,
                "name": "Ресторанная Кухня (Restaurant Cuisine)",
                "description": "Искусство, технология, презентация. Блюда, где главное — мастерство шефа и впечатление гостя."
                               "Примеры: стейк средней прожарки, утонченные десерты, фуа-гра, блюда молекулярной кухни."
            },
            {
                "id": 4,
                "name": "Фьюжн / Авторская Кухня (Fusion / Author's Cuisine)",
                "description": "Эксперимент, креатив, смешение культур. Шеф соединяет несовместимые, на первый взгляд, техники и вкусы."
                               "Примеры: суши-бургер, пельмени с уткой по-пекински, тирамису с чаем матча."
            },
            {
                "id": 5,
                "name": "Фермерская Кухня (Farm-to-Table)",
                "description": "Сезонность, локальность, качество продуктов. Акцент на свежести и происхождении ингредиентов."
                               "Примеры: салат из только что собранных овощей, стейк из мяса местной фермы, сыр от соседней сыроварни."
            },
            {
                "id": 6,
                "name": "Постная / Вегетарианская Кухня (Lenten / Vegetarian Cuisine)",
                "description": "Растительная основа, легкость, этика. Блюда без мяса, часто с акцентом на овощи, крупы и бобовые."
                               "Примеры: фалафель, овощное карри, чечевичный суп, тофу-скрембл."
            },
            {
                "id": 7,
                "name": "Праздничная Кухня (Festive / Holiday Cuisine)",
                "description": "Традиции, изобилие, символизм. Блюда, которые готовят по особым случаям."
                               "Примеры: новогодний оливье, пасхальный кулич, индейка на День Благодарения, рождественский гусь."
            },
            {
                "id": 8,
                "name": "Пикник / Походная Кухня (Picnic / Campfire Cooking)",
                "description": "На природе, простота, дымный аромат. Еда, которую готовят и едят на открытом воздухе."
                               "Примеры: шашлык, барбекю, запеченная в углях картошка, сэндвичи, сосиски на гриле."
            },
            {
                "id": 9,
                "name": "Фуд-трип / Гастрономический Туризм (Food Trip Cuisine)",
                "description": "Аутентичность, открытие, локальные вкусы. Блюда, которые ты пробуешь, путешествуя по миру."
                               "Примеры: паэлья в Валенсии, паста в Риме, том-ям в Таиланде, крок-месье в Париже."
            },
            {
                "id": 10,
                "name": "Базовая / Начинающая Кухня (Basic / Beginner's Cuisine)",
                "description": "Просто, быстро, без изысков. Рецепты, с которых начинается путь на кухне."
                               "Примеры: яичница, макароны с сыром, салат из огурцов и помидоров, бутерброды."
            },
            {
                "id": 11,
                "name": "Гастрономическая / Высокая Кухня (Gastronomic / Haute Cuisine)",
                "description": "Сложные техники, дорогие продукты, идеальная подача. Вершина кулинарного искусства."
                               "Примеры: блюда из мишленовских ресторанов, конфи из утки, су-вид стейк, сложные соусы."
            },
            {
                "id": 12,
                "name": "Бабушкина / Наследие Кухня (Grandma's / Heritage Cuisine)",
                "description": "Рецепты-легенды, семейные секреты, ностальгия. Самая душевная категория, часто пересекается с домашней кухней, но с акцентом на традиции."
                               "Примеры: семейный рецепт борща, фирменные вареники, пирог по рецепту прабабушки."
            }
        ]

        products_data = [
            {
                "name": "Искусство шаурмы: от уличной классики до авторских версий",
                "description": "Освойте все секреты приготовления идеальной шаурмы - от выбора мяса и маринадов до правильной сборки",
                "image": "shawarma-course.jpg",
                "category_id": 1,
                "price": 2900.00,
                "date_of_create": "2024-03-15 14:20:00",
                "date_of_last_change": "2024-11-08 09:45:00"
            },
            {
                "name": "Уличные бургеры: как превзойти ресторанный уровень",
                "description": "Научитесь создавать бургеры с идеальной котлетой, соусами и сочетаниями ингредиентов",
                "image": "street-burger-course.jpg",
                "category_id": 1,
                "price": 3200.00,
                "date_of_create": "2024-04-22 11:30:00",
                "date_of_last_change": "2024-10-15 16:20:00"
            },
            {
                "name": "Азиатская уличная еда: вок, вок, вок!",
                "description": "Освойте технику работы с воком и готовьте аутентичные азиатские блюда как с уличных лотков",
                "image": "asian-street-food-course.jpg",
                "category_id": 1,
                "price": 3500.00,
                "date_of_create": "2024-05-10 09:15:00",
                "date_of_last_change": "2025-01-12 14:30:00"
            },
            {
                "name": "Бабушкины пироги: рецепты, которые мы теряем",
                "description": "Восстановите семейные традиции - научитесь печь пироги по старинным рецептам",
                "image": "grandma-pies-course.jpg",
                "category_id": 2,
                "price": 2700.00,
                "date_of_create": "2024-02-28 13:45:00",
                "date_of_last_change": "2024-09-05 10:10:00"
            },
            {
                "name": "Воскресный обед: от супа до компота",
                "description": "Полный цикл приготовления традиционного домашнего обеда на всю семью",
                "image": "sunday-lunch-course.jpg",
                "category_id": 2,
                "price": 3100.00,
                "date_of_create": "2024-01-15 08:20:00",
                "date_of_last_change": "2024-12-20 15:40:00"
            },
            {
                "name": "Домашняя выпечка без сложностей",
                "description": "Простая и вкусная выпечка для повседневных завтраков и семейных чаепитий",
                "image": "home-baking-course.jpg",
                "category_id": 2,
                "price": 2500.00,
                "date_of_create": "2024-03-08 10:00:00",
                "date_of_last_change": "2024-08-14 11:25:00"
            },
            {
                "name": "Ресторанные десерты в домашних условиях",
                "description": "Техники и рецепты десертов, которые не стыдно подать в лучших ресторанах",
                "image": "restaurant-desserts-course.jpg",
                "category_id": 3,
                "price": 4800.00,
                "date_of_create": "2024-06-12 16:45:00",
                "date_of_last_change": "2025-02-01 13:15:00"
            },
            {
                "name": "Стейк-мастер: от выбора мяса до идеальной прожарки",
                "description": "Профессиональный подход к приготовлению стейков различных видов и степени прожарки",
                "image": "steak-master-course.jpg",
                "category_id": 3,
                "price": 5200.00,
                "date_of_create": "2024-07-18 14:30:00",
                "date_of_last_change": "2024-11-30 09:50:00"
            },
            {
                "name": "Соусы - душа ресторанной кухни",
                "description": "Освойте классические и современные ресторанные соусы, преображающие любое блюдо",
                "image": "restaurant-sauces-course.jpg",
                "category_id": 3,
                "price": 4500.00,
                "date_of_create": "2024-04-05 11:10:00",
                "date_of_last_change": "2024-10-22 17:20:00"
            },
            {
                "name": "Фьюжн-кухня: где Восток встречается с Западом",
                "description": "Учимся смелым кулинарным экспериментам и созданию авторских блюд",
                "image": "east-west-fusion-course.jpg",
                "category_id": 4,
                "price": 4100.00,
                "date_of_create": "2024-08-25 15:25:00",
                "date_of_last_change": "2025-01-08 12:40:00"
            },
            {
                "name": "Молекулярная кухня для начинающих",
                "description": "Основы молекулярной гастрономии - сферы, эспумы и желирование в домашних условиях",
                "image": "molecular-basics-course.jpg",
                "category_id": 4,
                "price": 5800.00,
                "date_of_create": "2024-09-14 13:50:00",
                "date_of_last_change": "2025-02-14 10:30:00"
            },
            {
                "name": "Авторские завтраки: разбуди своего внутреннего шефа",
                "description": "Создавайте уникальные блюда для завтрака, сочетая несочетаемое",
                "image": "author-breakfasts-course.jpg",
                "category_id": 4,
                "price": 3600.00,
                "date_of_create": "2024-05-30 09:40:00",
                "date_of_last_change": "2024-12-05 14:15:00"
            },
            {
                "name": "Сезонное меню: от фермы до стола",
                "description": "Учимся готовить из сезонных продуктов, максимально раскрывая их вкус",
                "image": "seasonal-menu-course.jpg",
                "category_id": 5,
                "price": 3900.00,
                "date_of_create": "2024-03-22 12:35:00",
                "date_of_last_change": "2024-11-18 08:45:00"
            },
            {
                "name": "Овощи главной роли: фермерская гастрономия",
                "description": "Превращаем свежие овощи в гастрономические шедевры",
                "image": "vegetables-main-course.jpg",
                "category_id": 5,
                "price": 3400.00,
                "date_of_create": "2024-06-08 10:20:00",
                "date_of_last_change": "2024-10-30 16:50:00"
            },
            {
                "name": "Деревенские сыры и хлеб",
                "description": "Научитесь готовить домашние сыры и хлеб из натуральных ингредиентов",
                "image": "farm-cheese-bread-course.jpg",
                "category_id": 5,
                "price": 4300.00,
                "date_of_create": "2024-04-18 14:15:00",
                "date_of_last_change": "2024-09-25 11:05:00"
            },
            {
                "name": "Веганская кухня: вкусно без компромиссов",
                "description": "Полноценные и вкусные блюда растительной кухни, которые понравятся всем",
                "image": "vegan-no-compromise-course.jpg",
                "category_id": 6,
                "price": 3300.00,
                "date_of_create": "2024-02-14 16:40:00",
                "date_of_last_change": "2024-08-08 13:25:00"
            },
            {
                "name": "Постный стол: традиции и современность",
                "description": "Готовим разнообразные и питательные блюда для постных дней",
                "image": "lenten-traditional-course.jpg",
                "category_id": 6,
                "price": 2800.00,
                "date_of_create": "2024-01-25 09:30:00",
                "date_of_last_change": "2024-12-10 15:20:00"
            },
            {
                "name": "Растительный протеин: от тофу до бобовых",
                "description": "Освойте все способы приготовления растительных белков",
                "image": "plant-protein-course.jpg",
                "category_id": 6,
                "price": 3100.00,
                "date_of_create": "2024-03-05 11:55:00",
                "date_of_last_change": "2024-11-25 10:10:00"
            },
            {
                "name": "Новогодний пир: готовим как профессионалы",
                "description": "Полное меню для новогоднего стола - от закусок до десертов",
                "image": "new-year-feast-course.jpg",
                "category_id": 7,
                "price": 4700.00,
                "date_of_create": "2024-10-15 14:50:00",
                "date_of_last_change": "2024-12-28 17:30:00"
            },
            {
                "name": "Пасхальный стол: традиции и современные тренды",
                "description": "Готовим к Пасхе все необходимое - от куличей до мясных блюд",
                "image": "easter-table-course.jpg",
                "category_id": 7,
                "price": 3200.00,
                "date_of_create": "2024-12-05 10:25:00",
                "date_of_last_change": "2025-03-20 12:45:00"
            },
            {
                "name": "Рождественские угощения Европы",
                "description": "Традиционные рождественские блюда разных европейских стран",
                "image": "christmas-europe-course.jpg",
                "category_id": 7,
                "price": 3800.00,
                "date_of_create": "2024-09-20 13:40:00",
                "date_of_last_change": "2024-12-15 16:15:00"
            },
            {
                "name": "Мастер-гриль: от углей до идеального стейка",
                "description": "Все секреты приготовления на углях - мясо, рыба, овощи и даже десерты",
                "image": "grill-master-course.jpg",
                "category_id": 8,
                "price": 4400.00,
                "date_of_create": "2024-05-15 15:10:00",
                "date_of_last_change": "2024-08-20 14:35:00"
            },
            {
                "name": "Пикник-шеф: еда для выезда на природу",
                "description": "Готовим удобную и вкусную еду для пикников и походов",
                "image": "picnic-chef-course.jpg",
                "category_id": 8,
                "price": 2900.00,
                "date_of_create": "2024-04-12 12:20:00",
                "date_of_last_change": "2024-07-30 09:55:00"
            },
            {
                "name": "Кемпинг-кухня: гастрономия в походных условиях",
                "description": "Научитесь готовить вкусные блюда с минимальным набором оборудования",
                "image": "camping-cooking-course.jpg",
                "category_id": 8,
                "price": 2600.00,
                "date_of_create": "2024-06-25 08:45:00",
                "date_of_last_change": "2024-09-15 11:40:00"
            },
            {
                "name": "Итальянский фуд-трип: от Рима до Сицилии",
                "description": "Готовим аутентичные итальянские блюда, как в лучших тратториях",
                "image": "italian-food-trip-course.jpg",
                "category_id": 9,
                "price": 4900.00,
                "date_of_create": "2024-07-08 14:25:00",
                "date_of_last_change": "2025-01-25 13:50:00"
            },
            {
                "name": "Азиатский гастротур: уличная еда 5 стран",
                "description": "Погружение в уличную кухню Таиланда, Вьетнама, Кореи, Японии и Китая",
                "image": "asian-food-tour-course.jpg",
                "category_id": 9,
                "price": 5100.00,
                "date_of_create": "2024-08-30 16:30:00",
                "date_of_last_change": "2025-02-10 15:05:00"
            },
            {
                "name": "Средиземноморский вояж: от Греции до Марокко",
                "description": "Кулинарное путешествие по странам Средиземноморья",
                "image": "mediterranean-voyage-course.jpg",
                "category_id": 9,
                "price": 4600.00,
                "date_of_create": "2024-09-05 10:50:00",
                "date_of_last_change": "2025-01-18 12:25:00"
            },
            {
                "name": "Кулинарный ликбез: основы для начинающих",
                "description": "Базовые техники и рецепты для тех, кто только начинает свой кулинарный путь",
                "image": "cooking-basics-course.jpg",
                "category_id": 10,
                "price": 2200.00,
                "date_of_create": "2024-01-10 09:15:00",
                "date_of_last_change": "2024-06-20 14:10:00"
            },
            {
                "name": "5 блюд за 30 минут: кухня для занятых",
                "description": "Быстрые и простые рецепты для будних дней",
                "image": "5-dishes-30min-course.jpg",
                "category_id": 10,
                "price": 1900.00,
                "date_of_create": "2024-02-20 11:40:00",
                "date_of_last_change": "2024-07-12 08:30:00"
            },
            {
                "name": "Не бойся ножа: базовые навыки нарезки",
                "description": "Освойте правильные техники нарезки продуктов быстро и безопасно",
                "image": "knife-skills-basics-course.jpg",
                "category_id": 10,
                "price": 2400.00,
                "date_of_create": "2024-03-12 13:25:00",
                "date_of_last_change": "2024-08-25 10:45:00"
            },
            {
                "name": "Высокая кухня: техники мишленовских шефов",
                "description": "Профессиональные техники и подходы из мира высокой гастрономии",
                "image": "michelin-techniques-course.jpg",
                "category_id": 11,
                "price": 8900.00,
                "date_of_create": "2024-10-08 15:35:00",
                "date_of_last_change": "2025-02-28 16:20:00"
            },
            {
                "name": "Су-вид для дома: ресторанный уровень",
                "description": "Освойте технологию низкотемпературного приготовления в домашних условиях",
                "image": "sous-vide-home-course.jpg",
                "category_id": 11,
                "price": 6700.00,
                "date_of_create": "2024-11-12 12:15:00",
                "date_of_last_change": "2025-03-05 14:55:00"
            },
            {
                "name": "Дегустационные меню: искусство подачи",
                "description": "Учимся создавать и сервировать многосоставные дегустационные сеты",
                "image": "tasting-menu-course.jpg",
                "category_id": 11,
                "price": 7200.00,
                "date_of_create": "2024-12-03 14:40:00",
                "date_of_last_change": "2025-03-12 11:30:00"
            },
            {
                "name": "Семейные рецепты: сохраняем наследие",
                "description": "Учимся готовить блюда, которые передаются из поколения в поколение",
                "image": "family-recipes-course.jpg",
                "category_id": 12,
                "price": 2800.00,
                "date_of_create": "2024-02-05 10:05:00",
                "date_of_last_change": "2024-10-10 13:15:00"
            },
            {
                "name": "Старославянская кухня: забытые рецепты",
                "description": "Возрождаем традиционные блюда наших предков",
                "image": "old-slavic-cuisine-course.jpg",
                "category_id": 12,
                "price": 3200.00,
                "date_of_create": "2024-03-18 08:50:00",
                "date_of_last_change": "2024-11-05 15:45:00"
            },
            {
                "name": "Бабушкины заготовки на зиму",
                "description": "Традиционные рецепты консервации и заготовок по семейным рецептам",
                "image": "grandma-preserves-course.jpg",
                "category_id": 12,
                "price": 2500.00,
                "date_of_create": "2024-07-22 11:20:00",
                "date_of_last_change": "2024-12-08 09:35:00"
            }
        ]

        # ШАГ 1: УДАЛЯЕМ СУЩЕСТВУЮЩИЕ ДАННЫЕ
        products_count_before = Product.objects.count()
        categories_count_before = Category.objects.count()

        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(
            self.style.WARNING(f"Удалено {products_count_before} продуктов и {categories_count_before} категорий")
        )

        # ШАГ 2: СОЗДАЕМ КАТЕГОРИИ
        categories_for_create = []
        for category_item in categories_data:
            categories_for_create.append(
                Category(
                    id=category_item['id'],
                    name=category_item['name'],
                    description=category_item['description']
                )
            )

        Category.objects.bulk_create(categories_for_create)

        self.stdout.write(
            self.style.SUCCESS(f"Создано {len(categories_for_create)} категорий")
        )

        # ШАГ 3: СОЗДАЕМ ПРОДУКТЫ
        products_for_create = []
        for product_item in products_data:
            product = Product(
                name=product_item['name'],
                description=product_item['description'],
                image=product_item['image'],
                price=product_item['price'],
                date_of_create=product_item['date_of_create'],
                date_of_last_change=product_item['date_of_last_change']
            )
            # Устанавливаем категорию по ID
            product.category_id = product_item['category_id']
            products_for_create.append(product)

        Product.objects.bulk_create(products_for_create)

        self.stdout.write(
            self.style.SUCCESS(f"Создано {len(products_for_create)} новых продуктов")
        )

        # Финальная статистика
        self.stdout.write(
            self.style.SUCCESS(
                f"База данных полностью обновлена. "
                f"Теперь в базе: {Category.objects.count()} категорий и {Product.objects.count()} продуктов"
            )
        )

        # Показываем созданные категории и продукты
        self.stdout.write("\n" + "=" * 50)
        self.stdout.write("Созданные категории:")
        for category in Category.objects.all():
            product_count = Product.objects.filter(category=category).count()
            self.stdout.write(f"  - {category.name} ({product_count} продуктов)")

        self.stdout.write("\nСозданные продукты:")
        for product in Product.objects.all():
            self.stdout.write(f"  - {product.name} - {product.price} руб. ({product.category.name})")
