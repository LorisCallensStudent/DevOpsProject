De vorige situatie is gewijzigd we werken niet meer weg remote scripten:
=> Nu werken we aan de hand van classen


1 script [Main.py] => Wat staat er hier nu al allemaal in?
- Het keuze menu: op basis van de gekozen optie wordt een vagrantBox object gemaakt met de juiste hardgecodeerde parameters.




Wat ontbreekt er / werkt er niet?

- Voor geen van deze hosts heb ik een correct .sh bestand kunnen schrijven, de map met sh bevat blanko scripts (behalve voor LAMP server & de vyos box heeft geen sh script nodig)

- Voor het aanmaken van de hosts heb ik BOXEN gebruikt die ik op Vagrant Cloud vond: dit wil zeggen dat deze nog niet werken en nog gewijzigd gaan moeten worden

- Voor de vyos box heb ik zelf al een vyos machine kunnen aanmaken
PROBLEEM: elke keer als ik deze afsluit reset deze (probleem voor vagrant login) 

=> Dit alles wil zeggen dat voor bovenstaande hosts de code geschreven is maar het vagrant gedeelte nog moet gedaan worden

=> Dit zorgt er ook voor dat veel nog niet is kunnen gestest worden.

=> Optie 7 en 8 zullen werken via remote wmi (zie toledo hiervoor)
	Niels heeft zelf gezegd dat wij niet met wmi kunnen werken omdat we de juiste zaken niet ingesteld hebben op onze vm's dus hoe testen?????