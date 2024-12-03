import csv
from django.core.management.base import BaseCommand, CommandError
from blog.models import BlogPost

class Command(BaseCommand):
    help = 'Import blog posts from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        try:
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if 'title' not in row or 'content' not in row:
                        raise CommandError('CSV file is missing required fields: title, content')

                    BlogPost.objects.create(
                        title=row['title'],
                        content=row['content'],
                        country=row.get('country', None)
                    )
            self.stdout.write(self.style.SUCCESS('Successfully imported blog posts'))
        except FileNotFoundError:
            raise CommandError(f"File '{csv_file}' does not exist.")
