from django.db import models
from django.forms import ModelForm
from django.db.models import F
from django.db.models.functions import (
    Pi, Power, Round
)

from django.utils import timezone
tz = timezone.get_default_timezone()

class Date(models.Model):
    """Дата фиксирования переменной"""
    # comment = models.TextField(default='')
    # text = models.CharField(verbose_name="Введите название", default='', max_length=100)
    date_enter=models.DateField(blank=False, null=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return 'Расчет от {}'.format(self.date_enter.strftime('%d.%m.%Y %H:%M'))
        # return self.date_enter
    # def __unicode__(self):
    #     return "%s" % (self.date_enter)

# class Entry(models.Model):
#     """Факторная переменная(вводится оператором) 20 переменных"""
#     date = models.ForeignKey(Date, verbose_name="Группа расчотов", on_delete=models.PROTECT, null=True)    
#     date_added=models.DateTimeField(verbose_name='Дата расчета', auto_now_add=True)
#     basicity_coefficient_in_agglomerate=models.DecimalField(verbose_name='Коэффициент основности агломерата КГОК:', default=0, max_digits=5, decimal_places=2)
#     sinter_make_minus_fife=models.DecimalField(verbose_name="Выход класса -5 мм вагломерате КГОК:", default=0, max_digits=5, decimal_places=2)
#     titanium_content_in_agglomerate=models.DecimalField( verbose_name="Содержание титана в агломерате КГОК:", default=0, max_digits=5, decimal_places=2)
#     magnesium_content_in_agglomerate=models.DecimalField(verbose_name="Содержание магния в агломерате КГОК:", default=0, max_digits=5, decimal_places=2)
#     content_of_magnetic_iron=models.DecimalField(verbose_name="Содержание железа магнитного в исходной руде:", default=0, max_digits=5, decimal_places=2)
#     content_magnetic_iron_in_the_source_ore=models.DecimalField(verbose_name="Содержание железа общего в концентрате:", default=0, max_digits=5, decimal_places=2)  
#     total_iron_content_in_the_concentrate=models.DecimalField(verbose_name="Коэффициент основности концентрата:", default=0, max_digits=5, decimal_places=2)
#     calcium_content_of_limestone=models.DecimalField(verbose_name="Содержание кальция в известняке:", default=0, max_digits=5, decimal_places=2)
#     output_of_plus_four_mm_class_in_coke=models.DecimalField(verbose_name="Выход класса +4 мм в коксе", default=0, max_digits=5, decimal_places=2)
#     water_consumption_in_drum_pelletizer=models.DecimalField(verbose_name="Расход воды в барабанном окомкователе:", default=0, max_digits=5, decimal_places=2)
#     temperature_in_the_furnace_of_am=models.DecimalField(verbose_name="Температура в горне а/м:", default=0, max_digits=7, decimal_places=2)
#     velocity_am=models.DecimalField(verbose_name="Скорость а/м", default=0, max_digits=5, decimal_places=2)
#     iron_content_in_agglomerate=models.DecimalField(verbose_name="Содержание железа вагломерате КГОК:", default=0, max_digits=5, decimal_places=2)
#     mechanical_strength_of_agglomerate=models.DecimalField(verbose_name="Механическая (барабанная) прочность агломерата:", default=0, max_digits=5, decimal_places=2)
#     titanium_content_inthe_source_ore=models.DecimalField(verbose_name="Содержание титана в исходной руде:", default=0, max_digits=5, decimal_places=2)
#     specific_fuel_consumption=models.DecimalField(verbose_name="Удельный расход топлива:", default=0, max_digits=5, decimal_places=2)
#     specific_consumption_of_natural_gas=models.DecimalField(verbose_name="Удельный расход природного газа:", default=0, max_digits=5, decimal_places=2)    
#     jig_bed_weight=models.DecimalField(verbose_name="Вес постели:", default=0, max_digits=5, decimal_places=2)
#     charge_consumption_before_seeding=models.DecimalField(verbose_name="Расход шихты до высева:", default=0, max_digits=5, decimal_places=2)
#     moisture_content_in_hopper_am=models.DecimalField(verbose_name="Влажность шихты в бункере а/м:", default=0, max_digits=5, decimal_places=2)

#     output_agglomerate = models.GeneratedField(verbose_name="Выход аглоотсева, кг/т:", 
#         expression=Round(237.5+
#         3.44*F("basicity_coefficient_in_agglomerate")+
#         0.79*F("sinter_make_minus_fife")+
#         67.1*F("titanium_content_in_agglomerate")+
#         36.4*F("magnesium_content_in_agglomerate")+
#         9.67*F("content_of_magnetic_iron")+
#         8.28*F("content_magnetic_iron_in_the_source_ore")+
#         214.95*F("total_iron_content_in_the_concentrate")+
#         2.48*F("calcium_content_of_limestone")+
#         0.95*F("output_of_plus_four_mm_class_in_coke")+
#         1.75*F("water_consumption_in_drum_pelletizer")+
#         0.03*F('temperature_in_the_furnace_of_am')+
#         4.6*F('velocity_am')-
#         16.6*F('iron_content_in_agglomerate')-
#         1.86*F('mechanical_strength_of_agglomerate')-
#         64.5*F('titanium_content_inthe_source_ore')-
#         0.35*F('specific_fuel_consumption')-
#         4.6*F('specific_consumption_of_natural_gas')-
#         0.19*F('jig_bed_weight')-
#         0.06*F('charge_consumption_before_seeding')-
#         7.1*F('moisture_content_in_hopper_am'), precision=1), 
#         output_field=models.BigIntegerField(),
#         db_persist=False, #Если вы используете postgresql , тот тут всегда указывайте True

        
#     )
    # def __str__(self):
    #      return 'Выход аглоотсева, кг/т: {}'.format(self.output_agglomerate)+format(self.date_added.astimezone(tz).strftime('%d.%m.%Y %H:%M'))
    
    

    # class Meta:deactivate
    #     verbose_name_plural ='entries'

class Entry(models.Model):
    """Факторная переменная(вводится оператором) 18 переменных"""
    date = models.ForeignKey(Date, verbose_name="Группа расчотов", on_delete=models.PROTECT, null=True)    
    date_added=models.DateTimeField(verbose_name='Дата расчета', auto_now_add=True)
    titanium_content_in_agglomerate=models.DecimalField( verbose_name="Содержание титана в агломерате КГОК:", default=0, max_digits=5, decimal_places=2)
    mechanical_strength_of_agglomerate=models.DecimalField(verbose_name="Механическая (барабанная) прочность агломерата:", default=0, max_digits=5, decimal_places=2)
    output_in_agglomerate_of_size_class=models.DecimalField(verbose_name="Выход в агломерате классаа крупности-40+15мм:", default=0, max_digits=5, decimal_places=2)
    specific_consumption_of_natural_gas=models.DecimalField(verbose_name="Расход природного газа:", default=0, max_digits=5, decimal_places=2)   
    water_consumption_in_drum_pelletizer=models.DecimalField(verbose_name="Расход воды в барабанном окомкователе:", default=0, max_digits=5, decimal_places=2)
    charge_consumption_before_seeding=models.DecimalField(verbose_name="Расход агломерационной шихты после высева:", default=0, max_digits=5, decimal_places=2)
    exhaust_gas_temperature=models.DecimalField(verbose_name="Температура отходящих газов:", default=0, max_digits=5, decimal_places=2)
    velocity_am=models.DecimalField(verbose_name="Скорость агломашины", default=0, max_digits=5, decimal_places=2)
    jig_bed_weight=models.DecimalField(verbose_name="Вес постели общий:", default=0, max_digits=5, decimal_places=2)
    content_titan_in_source_ore=models.DecimalField(verbose_name="Содержание титана в концентрате", default=0, max_digits=5, decimal_places=2)  
    content_of_size_class_in_source_ore=models.DecimalField(verbose_name="Содержание в концентрате класса крупности -0,071 мм:", default=0, max_digits=5, decimal_places=2)
    output_in_limestone_of_size_class=models.DecimalField(verbose_name="Выход в известняке класса крупности +3, мм:", default=0, max_digits=5, decimal_places=2)
    specific_fuel_consumption=models.DecimalField(verbose_name="Удельный расход топлива:", default=0, max_digits=5, decimal_places=2)
    consumption_of_agglomeration_charge_after_seeding=models.DecimalField(verbose_name="Расход агломерационной шихты послевысева:", default=0, max_digits=5, decimal_places=2)
    filling_level_of_bed_bin=models.DecimalField(verbose_name="Уровень заполнения бункера постели:", default=0, max_digits=5, decimal_places=2)
    moisture_content_in_hopper_am=models.DecimalField(verbose_name="Влажность шихты в бункере а/м:", default=0, max_digits=5, decimal_places=2)
    temperature_in_vacuum_chamber_no_eighteen=models.DecimalField(verbose_name="Температура в вакуум-камере № 18:", default=0, max_digits=5, decimal_places=2)
    temperature_in_vacuum_chamber_no_nineteen=models.DecimalField(verbose_name="Температура в вакуум-камере № 19:", default=0, max_digits=5, decimal_places=2)

    
    
    output_agglomerate = models.GeneratedField(verbose_name="Выход аглоотсева, кг/т:", 
        expression=Round(714.38+
        74.41*F("titanium_content_in_agglomerate")+
        9.09*F("mechanical_strength_of_agglomerate")+
        1.06*F("output_in_agglomerate_of_size_class")+
        23.19*F("specific_consumption_of_natural_gas")+
        12.1*F("water_consumption_in_drum_pelletizer")+
        0.84*F("charge_consumption_before_seeding")+
        3.85*F("exhaust_gas_temperature")+
        64.37*F("velocity_am")+
        0.21*F("jig_bed_weight")-
        155.15*F("content_titan_in_source_ore")-
        6.08*F("content_of_size_class_in_source_ore")-
        5.81*F("output_in_limestone_of_size_class")-
        2.8*F("specific_fuel_consumption")-
        0.68*F("consumption_of_agglomeration_charge_after_seeding")-
        1.82*F("filling_level_of_bed_bin")-
        81.66*F("moisture_content_in_hopper_am")-
        1.17*F("temperature_in_vacuum_chamber_no_eighteen")-
        1.05*F("temperature_in_vacuum_chamber_no_nineteen"), precision=1), 
        output_field=models.BigIntegerField(),
        db_persist=False, #Если вы используете postgresql , тот тут всегда указывайте True

        
    )
    actual_value_of_agglomeration_output=models.DecimalField(verbose_name="Фактическое значение выхода аглоотсева, кг/т", default=0, max_digits=5, decimal_places=2)
    difference_between_estimated_and_actual_values = models.GeneratedField(verbose_name="Абсолютная разница между расчетным и фактическим значениями", 
        expression=Round(
        F("output_agglomerate")-
        F("actual_value_of_agglomeration_output"), precision=1), 
        output_field=models.BigIntegerField(),
        db_persist=False, #Если вы используете postgresql , тот тут всегда указывайте True

        
    )
    # def __str__(self):
    #      return 'Выход аглоотсева, кг/т: {}'.format(self.output_agglomerate)+format(self.date_added.astimezone(tz).strftime('%d.%m.%Y %H:%M'))
    
    

    # class Meta:
    #     verbose_name_plural ='entries'




   


