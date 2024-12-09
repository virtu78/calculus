from django.contrib import admin

# Register your models here.


from agglomerates.models import Date, Entry
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




