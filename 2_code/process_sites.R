require(xml2)
require(rvest)
require(tidyverse)

files = list.files('1_data/sites', full.names = T)

tables = list()
for(i in 1:length(files)){
  print(i)
  page = read_html(files[i])
  node = html_node(page, xpath = '//*[@id="table-apps"]')
  tab = node %>% html_table()
  tab$id = str_extract_all(files[i], '[:digit:]+')[[1]][2]
  tables[[i]] = tab
  }

tag_tbl = do.call(rbind, tables) %>% select(-1) %>% as_tibble()

steam = read_csv('1_data/steam.csv') %>% arrange(id) %>% 
  right_join(tag_tbl %>% mutate(id = as.numeric(id))) %>% 
  select(tag, Name, Rating, Followers, Online, Peak) %>% 
  rename(Tag = tag) %>% 
  mutate(Rating = str_replace(Rating, '%', '') %>% as.numeric(),
         Followers = str_replace_all(Followers, ',', '') %>% as.numeric(),
         Online = str_replace_all(Online, ',', '') %>% as.numeric(),
         Peak = str_replace_all(Peak, ',', '') %>% as.numeric())

steam_agg = steam %>% 
  group_by(Name) %>% 
  summarize(Tags = paste0(Tag, collapse=';'),
            Rating = mean(Rating, na.rm=T),
            Followers = mean(Followers, na.rm=T),
            Online = mean(Online, na.rm=T),
            Peak = mean(Peak, na.rm=T))
  
write_csv(steam_agg, '1_data/steam_tags.csv')
