import os
import subprocess
from datetime import datetime

LOG_FILE = "spider_run_log.txt"

SPIDERS = [
    {
        "path": "spider-scripts/PEP-https-www.nbim.no-/tutorial/tutorial",
        "spider": "aml_pep_nbim_norway_entity_Server_CR"
    },
    {
        "path": "PEP-https-www.state.gov/tutorial/tutorial",
        "spider": "aml_pep_state_united_states_person_Server_CR"
    },
    {
        "path": "PEP-https-www.saps.gov.za-/tutorial/tutorial",
        "spider": "aml_pep_saps_south_africa_person_Server_CR"
    },
    {
        "path": "PEP-https-www.ice.gov-/tutorial/tutorial",
        "spider": "aml_pep_ice_united_states_person_Server_CR"
    },
    {
        "path": "PEP-https-www.legislation.gov.uk-/tutorial/tutorial",
        "spider": "aml_pep_legislation_united_kingdom_entity_Server_CR"
    },
    {
        "path": "PEP-https-www.fdic.gov-/tutorial/tutorial",
        "spider": "PEP-Scraper-FDIC-Updated_Server_CR"
    }
]

def log(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    full_message = f"[{timestamp}] {message}"
    print(full_message)
    with open(LOG_FILE, 'a') as f:
        f.write(full_message + '\n')

def run_spiders():
    for job in SPIDERS:
        full_path = os.path.abspath(job["path"])
        spider_name = job["spider"]

        try:
            log(f"🔄 Starting spider '{spider_name}' in '{full_path}'")
            os.chdir(full_path)

            process = subprocess.Popen(
                ["scrapy", "crawl", spider_name],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )

            with open(LOG_FILE, 'a') as f:
                for line in process.stdout:
                    print(line, end='')       # Show on terminal
                    f.write(line)            # Also write to log file

            process.wait()

            if process.returncode == 0:
                log(f"✅ SUCCESS: '{spider_name}' completed successfully.")
            else:
                log(f"❌ ERROR: '{spider_name}' failed with return code {process.returncode}.")

        except Exception as e:
            log(f"❌ EXCEPTION: Failed to run '{spider_name}' - {str(e)}")

        finally:
            os.chdir("../../..")
            log(f"🔙 Returned to base directory.\n")

if __name__ == "__main__":
    log("🚀 Run started")
    run_spiders()
    log("✅ Run completed\n")

