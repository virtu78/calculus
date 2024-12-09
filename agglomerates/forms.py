# from django import forms


from .models import Date, Entry
from django.forms import ModelForm

class DateForm(ModelForm):
    class Meta:
        model = Date
        fields=['text']
        
        
class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields=[
            # 'date',
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
            'actual_value_of_agglomeration_output',            
            ]
        

        
