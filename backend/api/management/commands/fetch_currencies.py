import requests
from decouple import config
from django.core.management.base import BaseCommand
from api.models import Currency

# Load environment variables from .env file
API_KEY = config('API_KEY')


class Command(BaseCommand):
    help = 'Fetch currency data from external API and populate the database'

    def handle(self, *args, **kwargs):
        # get api key
        api_key = API_KEY

        if not api_key:
            self.stdout.write(self.style.ERROR('API_KEY not found in .env file'))
            return

        # Define the API URL
        url = f'https://api.exchangeratesapi.io/v1/latest?access_key={api_key}'  # Replace with the actual API endpoint

        try:
            # Make a GET request to fetch the data
            response = requests.get(url)
            data = response.json()

            if data['success']:
                base_currency = data['base']
                date = data['date']
                rates = data['rates']

                # Iterate over the rates and populate the database
                for currency_code, rate in rates.items():
                    Currency.objects.update_or_create(
                        code=currency_code,
                        defaults={
                            'rate': rate,
                            'date': date,
                        }
                    )

                self.stdout.write(self.style.SUCCESS('Successfully populated the database with currency data.'))
            else:
                self.stdout.write(self.style.ERROR('Failed to fetch data: API returned an unsuccessful response.'))

        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data: {e}'))
