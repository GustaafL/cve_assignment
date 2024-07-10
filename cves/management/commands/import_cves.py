from django.core.management.base import BaseCommand, CommandError
from cves.models import CVE
import requests


class Command(BaseCommand):
    help = "Import CVEs from NIST"

    def handle(self, *args, **options):

        try:
            response = requests.get(
                "https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=50",
                timeout=300,
            )
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            raise CommandError(f"Error fetching data from NIST: {e}") from e
            # load data into database
        print(data)
        for cve in data["vulnerabilities"]:
            cve_id = cve["cve"]["id"]
            description = cve["cve"]["descriptions"][0]["value"]

            cve = CVE(cve_id=cve_id, description=description)
            cve.save()
        self.stdout.write(self.style.SUCCESS("Successfully imported CVEs"))


#  [{'lang': 'en', 'value': 'The debug command in Sendmail is enabled, allowing attackers to execute commands as root.'}, {'lang': 'es', 'value': 'El comando de depuración de Sendmail está activado, permitiendo a atacantes ejecutar comandos como root.'}]
