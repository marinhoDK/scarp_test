from config_reader import ConfigReader
from web_scraper import WebProperties, StaticDataScraper, InteractiveDataScraper
from playwright.sync_api import sync_playwright


def static_scrape_data(scraper, config):
    return scraper.scrape(config['url'], config)


def interactive_scrape_data(scraper, config):
    return scraper.scrape(config['url'], config['actions'])


def main():
    config_file_path = r'./config.json' 
    config_reader = ConfigReader(config_file_path)
    pages_config = config_reader.read_config()

    with sync_playwright() as playwright:
        web_properties = WebProperties(browser_type=playwright.chromium)
        static_scraper = StaticDataScraper(web_properties)
        interactive_scraper = InteractiveDataScraper(web_properties)

        for page_config in pages_config:
            if "selector" in page_config:  
                #pass
                result = static_scrape_data(static_scraper, page_config)
                if result is None:
                    print(f"Failed to scrape static data for {page_config['name']}.")
            elif "actions" in page_config:  
                #pass
                result = interactive_scrape_data(interactive_scraper, page_config)
                if result is None or len(result) == 0:
                    print(f"Failed to scrape interactive data for {page_config['name']}.")
            
            
                

if __name__ == "__main__":
    main()