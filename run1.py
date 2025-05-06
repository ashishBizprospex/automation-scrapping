import os
import subprocess

# List of spider scripts with their working directory and spider name
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

    # Add more spiders here
]

def run_spiders():
    for job in SPIDERS:
        full_path = os.path.abspath(job["path"])
        spider_name = job["spider"]
        print(f"\n📁 Changing directory to: {full_path}")
        os.chdir(full_path)

        command = ["scrapy", "crawl", spider_name]
        print(f"🕷️ Running command: {' '.join(command)} in {os.getcwd()}")

        subprocess.run(command)

        # Return to root directory for next spider
        os.chdir("../../..")
        print(f"🔙 Returned to base directory: {os.getcwd()}")

if __name__ == "__main__":
    print("🚀 Starting all registered spiders...\n")
    run_spiders()

