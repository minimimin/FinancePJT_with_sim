import csv
from django.core.management.base import BaseCommand
from maps.models import Region

class Command(BaseCommand):
    help = 'Import data from CSV file to Django model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Region.objects.create(
                    sido=row['sido'],
                    gungu=row['gungu'],
                )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))