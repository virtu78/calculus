from django.contrib import admin

# Register your models here.


from agglomerates.models import Date, Entry
from django.urls import path
from openpyxl.reader.excel import load_workbook

# from core.forms import XlsxImportForm
# from django.core.models import Record
class DateAdmin(admin.ModelAdmin):
    fields=[
    'enter_date',
    'created',
   ]
    readonly_fields = (
        'created',)

admin.site.register(Date)


class EntryAdmin(admin.ModelAdmin):
    fields=[
    'date',
    'titanium_content_in_agglomerate',
    'mechanical_strength_of_agglomerate',
    'output_in_agglomerate_of_size_class',
    'specific_consumption_of_natural_gas',
    'water_consumption_in_drum_pelletizer',
    'charge_consumption_before_seeding',
    'exhaust_gas_temperature',
    'velocity_am',
    'jig_bed_weight',
    'content_titan_in_source_ore',
    'content_of_size_class_in_source_ore',
    'output_in_limestone_of_size_class',
    'specific_fuel_consumption',
    'consumption_of_agglomeration_charge_after_seeding',
    'filling_level_of_bed_bin',
    'moisture_content_in_hopper_am',
    'temperature_in_vacuum_chamber_no_eighteen',
    'temperature_in_vacuum_chamber_no_nineteen',
    'output_agglomerate',
    'actual_value_of_agglomeration_output',
    'difference_between_estimated_and_actual_values',
    'date_added']
    
    # fields = [
    #     'date',
    #     'basicity_coefficient_in_agglomerate',
    #     'sinter_make_minus_fife',
    #     'titanium_content_in_agglomerate',
    #     'magnesium_content_in_agglomerate',
    #     'content_of_magnetic_iron',
    #     'content_magnetic_iron_in_the_source_ore',
    #     'total_iron_content_in_the_concentrate',
    #     'calcium_content_of_limestone',
    #     'output_of_plus_four_mm_class_in_coke',
    #     'water_consumption_in_drum_pelletizer',        
    #     'temperature_in_the_furnace_of_am',
    #     'velocity_am',
    #     'iron_content_in_agglomerate',
    #     'mechanical_strength_of_agglomerate',
    #     'titanium_content_inthe_source_ore',
    #     'specific_fuel_consumption',
    #     'specific_consumption_of_natural_gas',
    #     'jig_bed_weight',
    #     'charge_consumption_before_seeding',
    #     'moisture_content_in_hopper_am',
    #     'output_agglomerate',
    #     'date_added']
    readonly_fields = (
        # 'basicity_coefficient_in_agglomerate',
        # 'sinter_make_minus_fife',
        # 'titanium_content_in_agglomerate',
        # 'magnesium_content_in_agglomerate',
        # 'content_of_magnetic_iron',
        # 'content_magnetic_iron_in_the_source_ore',
        # 'total_iron_content_in_the_concentrate',
        # 'calcium_content_of_limestone',
        # 'output_of_plus_four_mm_class_in_coke',
        # 'water_consumption_in_drum_pelletizer',        
        # 'temperature_in_the_furnace_of_am',
        # 'velocity_am',
        # 'iron_content_in_agglomerate',
        # 'mechanical_strength_of_agglomerate',
        # 'titanium_content_inthe_source_ore',
        # 'specific_fuel_consumption',
        # 'specific_consumption_of_natural_gas',
        # 'jig_bed_weight',
        # 'charge_consumption_before_seeding',
        # 'moisture_content_in_hopper_am',

        'output_agglomerate',        
        'difference_between_estimated_and_actual_values',
        'date_added',)


admin.site.register(Entry, EntryAdmin)




# class RecordAdmin(admin.ModelAdmin):
#     list_display = ('name', 'value')
#     change_list_template = 'core/record_change_list.html'

#     def get_urls(self):
#         urls = super().get_urls()
#         # Добавляем URL нашего обработчика импорта.
#         my_urls = [
#             path('import-records-from-xlsx/', self.import_records_from_xlsx),
#         ]
#         return my_urls + urls

#     def import_records_from_xlsx(self, request):
#         context = admin.site.each_context(request)
#         if request.method == 'POST':
#             xlsx_file = request.FILES['xlsx_file']

#             workbook = load_workbook(filename=xlsx_file, read_only=True)
#             worksheet = workbook.active

#             # Читаем файл построчно и создаем объекты.
#             records_to_save = []
#             for row in worksheet.rows:
#                 new_obj = self.model(name=row[0].value, value=row[1].value)
#                 records_to_save.append(new_obj)
#             self.model.objects.bulk_create(records_to_save)

#             self.message_user(request, f'Импортировано строк: {len(records_to_save)}.')
#             return redirect('admin:core_record_changelist')

#         context['form'] = XlsxImportForm()
#         return render(request, 'core/add_records_form.html', context=context)


# admin.site.register(Record, RecordAdmin)