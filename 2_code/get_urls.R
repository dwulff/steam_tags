require(xml2)
require(rvest)
require(tidyverse)

page = read_html('1_data/overview_page.html')

tags = html_nodes(page, xpath = "//*[contains(@class, 'label-link')]")

labels = sapply(tags, html_text)
links = sapply(tags, html_attr, name = "href")
steam = tibble(tag = labels, 
               url = paste0("https://steamdb.info", links),
               id = str_extract(links,'[:digit:]+'))

write_lines(steam$url, '1_data/urls.txt')
write_lines(steam$id, '1_data/urls_ids.txt')
write_csv(steam,'1_data/steam.csv')


