# myapp/management/commands/loadcsv.py
from django.core.management.base import BaseCommand, CommandError
from django_app1.models import Company
import pandas as pd

class Command(BaseCommand):
    help = 'Load a CSV file into the Company table'

    def add_arguments(self, parser):
        parser.add_argument('csv_filename', type=str, help='The CSV file path')

    def handle(self, *args, **options):
        csv_filename = options['csv_filename']
        try:
            csv_data = pd.read_csv(csv_filename,sep=';', encoding='utf-8')
            self.stdout.write(f"Loading data from {csv_filename}")
            
            for record in csv_data.to_dict(orient="records"):
                Company.objects.create(
                    name=record.get('Name', ''),
                    #comment=record.get('Comment', ''),
                    sector=record.get('Sector', ''),
                    location=record.get('Location', ''),
                    num_posts=record.get('Number of Posts', ''),
                    url_posts=record.get('URL Posts', '')
                    
                )
            self.stdout.write(self.style.SUCCESS('Successfully loaded data into Company table'))
        
        except FileNotFoundError:
            raise CommandError(f"File {csv_filename} does not exist")
        except Exception as e:
            raise CommandError(f"An error occurred: {e}")
