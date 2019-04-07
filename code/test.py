import csv
import os
import codecs


def save_to_csv_file(csv_file, csv_data):
    dir_name = os.path.dirname(csv_file)
    os.makedirs(dir_name)
    with codecs.open(csv_file, 'a', 'utf-8') as file:
        writer = csv.writer(file, dialect='excel', lineterminator='\n')
        for row in csv_data:
            writer.writerow([row])

if __name__ == '__main__':
    save_to_csv_file('test/test.csv', ['Add-ons', 'Australia Good Food Guide', 'Digital Terrain Model', 'Fuel Prices API', 'HERE Traffic (ML)', 'Highway Exit POI', 'Hook Turns', 'Local Search API', 'Lonely Planet', 'Merian Scout Travel Guide (to be discontinued)', 'Natural Guidance', 'Parking API', 'Postal Code Boundaries', 'Postal Code Points', 'Safety Cameras API', 'Scenic Routes', 'Transit and Pedestrian(Tram Stop POI&nbsp; only)', 'Toll Costs'])