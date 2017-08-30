import sys
import logging
import Common
import Utils
reload(sys)
sys.setdefaultencoding('utf-8')


def parse_details_page(content):
    info = []

    ul_tag = content.find('ul', {'class': 'er-list-two f-clear'})
    if ul_tag:
        area_tag = ul_tag.find('a', {'class':'xiaoqu card-blue'})
        if area_tag:
            info.append(area_tag.string.strip())
        location_tags = ul_tag.find_all('a', {'class':'blue'})
        if location_tags:
            for location in location_tags:
                info.append(location.string.strip())
            else:
                info.append('None')
        else:
            logging.error('Can not find specify tag')

    div_tag = content.find('div', {'class':'price-wrap'})
    if div_tag:
        price = div_tag.find('span', {'class':'price'}).string
        if price is None:
            info.append('None')
        else:
            info.append(price)

        unit = div_tag.find('span', {'class':'unit'}).string
        if unit is None:
            info.append('None')
        else:
            info.append(unit)
    else:
        logging.error('Can not find price tag')

    ul_tag = content.find('ul', {'class':'er-list f-clear'})
    if ul_tag:
        span_tags = ul_tag.find_all('span', {'class':'content'})
        if span_tags:
            for span in span_tags:
                info.append(span.string.strip())
        else:
            logging.error('Can not find specify tag')

    property_description_tag = content.find('div', id='js-house-describe')
    if property_description_tag:
        item_tags = property_description_tag.find_all('div',{'class':'item'})
        for item in item_tags:
            info.append(item.string.strip())
            logging.info('current property attribute is: {0}'.format(item.string))

    return info

if __name__ == '__main__':
    Common.log_configuration('DEBUG')
    content = Utils.get_data("http://sh.ganji.com/fang5/2776639768x.htm")
    parse_details_page(content)