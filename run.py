import os
import subprocess
from datetime import datetime
import traceback

BASE_DIR = os.path.abspath(os.getcwd())
LOG_FILE = os.path.join(BASE_DIR, "spider_run_log.txt")

SPIDERS = [
    {
        "path": "spider-scripts/PEP-https-www.nbim.no-/tutorial/tutorial",
        "spider": "aml_pep_nbim_norway_entity_Server_CR"
    },
    {
        "path": "spider-scripts/PEP-https-www.state.gov/tutorial/tutorial",
        "spider": "aml_pep_state_united_states_person_Server_CR"
    },
    {
        "path": "spider-scripts/PEP-https-www.saps.gov.za-/tutorial/tutorial",
        "spider": "aml_pep_saps_south_africa_person_Server_CR"
    },
    {
        "path": "spider-scripts/PEP-https-www.ice.gov-/tutorial/tutorial",
        "spider": "aml_pep_ice_united_states_person_Server_CR"
    },
    {
        "path": "spider-scripts/PEP-https-www.legislation.gov.uk-/tutorial/tutorial",
        "spider": "aml_pep_legislation_united_kingdom_entity_Server_CR"
    },
    {
        "path": "spider-scripts/PEP-https-www.fdic.gov-/tutorial/tutorial",
        "spider": "PEP-Scraper-FDIC-Updated_Server_CR"
    }
]

def log(message, sep=False):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    full_message = f"[{timestamp}] {message}"
    if sep:
        full_message = "\n" + "=" * 80 + "\n" + full_message
    print(full_message)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(full_message + '\n')

def run_spiders():
    for job in SPIDERS:
        full_path = os.path.abspath(job["path"])
        spider_name = job["spider"]

        log(f"🔄 Starting spider '{spider_name}' in '{full_path}'", sep=True)

        try:
            os.chdir(full_path)

            process = subprocess.Popen(
                ["scrapy", "crawl", spider_name],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                bufsize=1,  # Line buffered
                universal_newlines=True
            )

            with open(LOG_FILE, 'a', encoding='utf-8') as f:
                for line in process.stdout:
                    print(line, end='')  # Print to terminal
                    f.write(line)        # Write to log file

            process.wait()

            if process.returncode == 0:
                log(f"✅ SUCCESS: '{spider_name}' completed successfully.")
            else:
                log(f"❌ ERROR: '{spider_name}' failed with return code {process.returncode}.")

        except Exception as e:
            tb = traceback.format_exc()
            log(f"❌ EXCEPTION: Failed to run '{spider_name}' - {str(e)}\n{tb}")

        finally:
            os.chdir(BASE_DIR)
            log(f"🔚 Finished spider '{spider_name}'\n" + "-" * 80)
            log(f"🔙 Returned to base directory.")

def clear_log():
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.write("")

if __name__ == "__main__":
    clear_log()
    log("🚀 Run started", sep=True)
    run_spiders()
    log("✅ All spiders completed.", sep=True)

