from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    # Проверка добавления книги
    def test_add_new_book_book_successfully_added(self):
        collector = BooksCollector()
        book = 'На краю Ойкумены'

        collector.add_new_book(book)

        for key in collector.get_books_rating():
            assert key == book  # проверяем название книги
            assert collector.get_books_rating()[key] == 1  # проверяем рейтинг по-умолчанию

    # Выставить рейтинг книге в списке
    def test_set_book_rating_happy_path(self):
        collector = BooksCollector()
        book = 'Улитка на склоне'
        rate = 10

        collector.add_new_book(book)
        collector.set_book_rating(book, rate)

        assert collector.get_book_rating(book) == rate

    # Выводим список книг с определенным рейтингом (5)
    def test_get_books_with_specific_rating_returns_books_with_rating_five(self):
        collector = BooksCollector()
        book_rating_1 = 'Что-то про WH40K'
        book_rating_5_one = 'Град обреченный'
        book_rating_5_two = 'Отель у погибшего альпиниста'
        book_rating_10 = "Город и звезды"

        collector.add_new_book(book_rating_1)
        collector.add_new_book(book_rating_5_one)
        collector.add_new_book(book_rating_5_two)
        collector.add_new_book(book_rating_10)

        collector.set_book_rating(book_rating_1, 1)
        collector.set_book_rating(book_rating_5_one, 5)
        collector.set_book_rating(book_rating_5_two, 5)
        collector.set_book_rating(book_rating_10, 10)

        assert book_rating_5_one, book_rating_5_two in collector.get_books_with_specific_rating(5)

    # Добавление книги в избранное
    def test_add_book_in_favorites_happy_path(self):
        collector = BooksCollector()
        book = 'Парень из преисподней'

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        assert book in collector.get_list_of_favorites_books()

    # Проверка удаления книги из избранного
    def test_delete_book_from_favorites_happy_path(self):
        collector = BooksCollector()
        book = 'Парень из преисподней'

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        if book in collector.get_list_of_favorites_books():
            collector.delete_book_from_favorites(book)
            assert book not in collector.get_list_of_favorites_books()
        else:
            print("Книга не была добавлена в Избранное")
