TABreadSolarAdditions <- function(folder){
  
country_list = list.files(folder,pattern = "\\.txt$", full.names = TRUE)

print(country_list)


dataframes <- list()

  for(country in country_list){
    
    
    df <- readr::read_delim(country, delim='\t', col_names = FALSE)
    
    df <- as.data.frame(t(df))
    
    colnames(df) <- c("year", "solarNetAdditions")
    
    country_name <- tools::file_path_sans_ext(basename(country))
    df$country<- country_name
    
    dataframes[[country_name]] <- df
    
  }

print(dataframes)


#create just a single df
combined_df <- do.call(rbind, dataframes)
#delete row names
rownames(combined_df)<-NULL

#set country names with capital letter
combined_df$country <- stringr::str_to_title(combined_df$country)

return(combined_df)
}




