import Details_Page_Parse
import logging
import Utils
import re
import Common


def get_links(content,url_prefix):
    links = []
    tips_list_tag = content.find('div', {'class': 'f-list js-tips-list'})

    if tips_list_tag:
        div_tags = tips_list_tag.find_all('div',{'class':{'f-list-item ershoufang-list'}})
        for div_tag in div_tags:
            if div_tag['href']:
                link = url_prefix + div_tag['href']
                links.append(link)
            else:
                continue
    else:
        logging.error('No tag')

    return links


def get_page_nums(total_num, num_per_page):
    return total_num/num_per_page + 1


def get_total_num(content, area):
    m_result_tag = content.find('p', {'class':'m-result f-fr'})

    if m_result_tag:
        num = m_result_tag.span.text.strip()
        num = re.findall(re.compile(r'^\d+\.?'),num)[0]
    else:
        logging.error('Can not find this tag')
    logging.info('Total property number is :{0} in area {1}'.format(num, area))
    return num


def get_link_num_per_page(content):
    tips_list_tag = content.find('div',{'class':'f-list js-tips-list'})
    num = 0

    if tips_list_tag:
        div_tags = tips_list_tag.find_all('div', {'class':{'f-list-item ershoufang-list'}})
        num = len(div_tags)
    else:
        logging.error('Can not find this tage')
        num = 0
    logging.info('The list item number in this page is: {0}'.format(num))

    return num


def get_details_by_links(links):
    infos = []
    for link in links:
        logging.info('Pick up property details from url: {0}'.format(link))
        try:
            content = Utils.get_data(link)
        except Exception as exception:
            logging.error('Error: {0}'.format(exception.message))
            content = None
        if content is None:
            continue
        info = Details_Page_Parse.parse_details_page(content)
        if info:
            infos.append(info)

    return infos

if __name__ == '__main__':
    Common.log_configuration('DEBUG')
    content = Utils.get_data("http://sh.ganji.com/fang5/pudongxinqu")
    links = get_links(content,"http://sh.ganji.com")
    get_details_by_links(links)