from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        products_data = [
            {
                "name": "Детский велосипед Stels",
                "description": "Трехколесный велосипед для детей от 3 лет с регулируемым сиденьем",
                "image": "products/kids_bike.jpg",
                "category_id": 7,  # Используем category_id вместо category
                "price": "4599.00",
                "date_of_create": "2024-01-20T09:15:00Z",
                "date_of_last_change": "2024-01-20T09:15:00Z"
            },
            {
                "name": "Автомобильные дворники Bosch",
                "description": "Качественные стеклоочистители с каркасной конструкцией",
                "image": "products/wipers.jpg",
                "category_id": 8,  # category_id вместо category
                "price": "1299.00",
                "date_of_create": "2024-01-19T14:30:00Z",
                "date_of_last_change": "2024-01-19T14:30:00Z"
            },
            {
                "name": "Набор для вязания",
                "description": "Комплект спиц и пряжи для создания теплых вещей",
                "image": "products/knitting_kit.jpg",
                "category_id": 9,  # category_id вместо category
                "price": "1899.00",
                "date_of_create": "2024-01-18T11:45:00Z",
                "date_of_last_change": "2024-01-18T11:45:00Z"
            },
            {
                "name": "Подарочная упаковка премиум",
                "description": "Набор подарочных коробок и бумаги для особых случаев",
                "image": "products/gift_wrap.jpg",
                "category_id": 10,  # category_id вместо category
                "price": "899.00",
                "date_of_create": "2024-01-17T16:20:00Z",
                "date_of_last_change": "2024-01-17T16:20:00Z"
            },
            {
                "name": "Увлажняющий крем La Roche-Posay",
                "description": "Интенсивное увлажнение для чувствительной кожи",
                "image": "products/moisturizer.jpg",
                "category_id": 6,  # category_id вместо category
                "price": "2199.00",
                "date_of_create": "2024-01-16T13:10:00Z",
                "date_of_last_change": "2024-01-16T13:10:00Z"
            },
            {
                "name": "Конструктор магнитный Magformers",
                "description": "Развивающий магнитный конструктор для детей от 5 лет",
                "image": "products/magnetic_builder.jpg",
                "category_id": 7,  # category_id вместо category
                "price": "3299.00",
                "date_of_create": "2024-01-15T10:30:00Z",
                "date_of_last_change": "2024-01-15T10:30:00Z"
            },
            {
                "name": "Автомобильный пылесос",
                "description": "Компактный пылесок для уборки в салоне автомобиля",
                "image": "products/car_vacuum.jpg",
                "category_id": 8,  # category_id вместо category
                "price": "1599.00",
                "date_of_create": "2024-01-14T15:40:00Z",
                "date_of_last_change": "2024-01-14T15:40:00Z"
            },
            {
                "name": "Набор для выжигания по дереву",
                "description": "Комплект с выжигателем и деревянными заготовками",
                "image": "products/wood_burning.jpg",
                "category_id": 9,  # category_id вместо category
                "price": "2499.00",
                "date_of_create": "2024-01-13T12:25:00Z",
                "date_of_last_change": "2024-01-13T12:25:00Z"
            },
            {
                "name": "Подарочный букет из конфет",
                "description": "Эксклюзивный букет, собранный из шоколадных конфет",
                "image": "products/candy_bouquet.jpg",
                "category_id": 10,  # category_id вместо category
                "price": "1899.00",
                "date_of_create": "2024-01-12T17:50:00Z",
                "date_of_last_change": "2024-01-12T17:50:00Z"
            },
            {
                "name": "Электрическая зубная щетка Oral-B",
                "description": "Зубная щетка с технологией 3D-чистки и таймером",
                "image": "products/electric_brush.jpg",
                "category_id": 6,  # category_id вместо category
                "price": "4299.00",
                "date_of_create": "2024-01-11T08:45:00Z",
                "date_of_last_change": "2024-01-11T08:45:00Z"
            }
        ]

        # Получаем количество продуктов до очистки
        products_count_before = Product.objects.count()

        # УДАЛЯЕМ ВСЕ СУЩЕСТВУЮЩИЕ ПРОДУКТЫ
        Product.objects.all().delete()

        self.stdout.write(
            self.style.WARNING(f"Удалено {products_count_before} существующих продуктов")
        )

        # СОЗДАЕМ НОВЫЕ ПРОДУКТЫ
        products_for_create = []
        for product_item in products_data:
            # Создаем продукт, используя category_id
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

        # Используем bulk_create для эффективного создания
        Product.objects.bulk_create(products_for_create)

        self.stdout.write(
            self.style.SUCCESS(f"Создано {len(products_for_create)} новых продуктов")
        )

        # Финальная статистика
        self.stdout.write(
            self.style.SUCCESS(
                f"База данных продуктов полностью обновлена. "
                f"Теперь в базе: {Product.objects.count()} продуктов"
            )
        )