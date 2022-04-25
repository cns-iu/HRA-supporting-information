import json
import urllib.request


def main():
    # To get TOKEN for viewing unpublished data, go to EUI, log in, then view source, then copy token from browser
    # TOKEN = sys.argv[1] if len(sys.argv) > 1 else None
    TOKEN = ''
    HBM_LINK = 'https://ccf-api.hubmapconsortium.org/v1/hubmap/rui_locations.jsonld'
    if TOKEN:
        HBM_LINK += '&token=' + TOKEN

    # first, let's get the most recent data
    with urllib.request.urlopen(HBM_LINK) as url:
        data = json.loads(url.read().decode())

        x = []
        y = []
        z = []
        counter = 0
        
        for item in data['@graph']:
            for sample in item['samples']:
                counter = counter + 1
                x.append(sample['rui_location']['x_dimension'])
                y.append(sample['rui_location']['y_dimension'])
                z.append(sample['rui_location']['z_dimension'])
                
    print("Number of tissue blocks: " + str(counter))
    print(compute_average(x))
    print(compute_average(y))
    print(compute_average(z))

def compute_average(list):
    """takes a list of numbers and returns the average
    Args:
        list ([number]): list of numbers
    """
    total = 0
    for item in list:
        total = total + item
    return total/len(list)


main()
