from django.test import TestCase
from django.urls import resolve
from agglomerates.views import index
import datetime
from .models import Date
# Create your tests here.

class ItemModelTest(TestCase):
    # def test_bad_maths(self):
    #     """Проверка работоспособномти"""
    #     self.assertEqual(1+1,2
    #     )

    def test_url_resolves_to_all_dates_view(self):
            """Тест корневой url преобразуется в представление страницы  all_dates"""
            # found=resolve('/')
            # self.assertEqual(found.func, index)
            first_date=Date()
            first_date.comment="Расчет_февраль"
            first_date.text="Расчет1"
            first_date.dat_added=datetime.datetime(2024, 10, 10)
            first_date.save()
            
            second_date=Date()
            second_date.comment="Расчет_март"
            second_date.text="Расчет2"
            second_date.dat_added=datetime.datetime(2024, 9, 9)
            second_date.save()

            saved_dates=Date.objects.all()
            self.assertEqual(saved_dates.count(), 2)
            first_saved_date=saved_dates[0]
            second_saved_date=saved_dates[1]
            self.assertEqual(first_saved_date.comment, 'Расчет_февраль')
            self.assertEqual(second_saved_date.comment, 'Расчет_март')
    
    # def my_test(self):
    #         """ Тест модели"""
    #         first_date=Date()
    #         first_date.text="Расчет_февраль"
    #         first_date.text="Расчет1"
    #         first_date.date_added=datetime.datetime(2024, 10, 10)
    #         first_date.save()

    #         second_date=Date()
    #         second_date.text="Расчет_март"
    #         second_date.text="Расчет2"
    #         second_date.date_added=datetime.datetime(2024, 9, 9)
    #         second_date.save()

    #         saved_dates=Date.objects.all()
    #         self.assertEqual(saved_dates.count(), 2)
    #         first_saved_date=saved_dates[0]
    #         second_saved_date=saved_dates[1]
    #         self.assertEqual(first_saved_date.text, 'Расчет_февраль')
    #         self.assertEqual(second_saved_date.text, 'Расчет_март')