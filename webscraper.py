import cmd
import requests

class Scraper(cmd.Cmd):
  prompt = 'SCRAPER >> '
  intro = 'Web Scraper. By Grenadieren/Razu'

  def do_scrape(self, line):
   url1 = input("URL:")
   req1 = requests.get(url1)
   print(req1.text)
   print(req1.encoding)
   print(req1.headers)
   print(req1.history)
   print(req1.cookies)
   print(req1.__hash__)
   print(req1.links)
   print(req1.status_code)
   print(req1.__attrs__)
   
if __name__ == '__main__':
    Scraper().cmdloop()
