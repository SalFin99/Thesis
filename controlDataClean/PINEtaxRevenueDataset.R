readAllfiles <- function(path){
  
  csv_files <- list.files(path = path, pattern = "\\.csv$", full.names = TRUE)
  print(csv_files)
  
  #list to store all the dataframes
  dataframes <- list() 
  
  for (file in csv_files){
    df <- read.csv(file)
    #get country file name without the .csv
    country_name <- tools::file_path_sans_ext(basename(file))
    df$country<- country_name
    
    #the original dataframe has the value of the env. taxes revenues in a column named after the country itself.
    colnames(df)[2] <- "envTaxRevenue"
    colnames(df)[1] <- "year"
    
    
    #the original csv from the PINE database has an "OECD" column, in position 3, that I dont need.
    df <- subset(df, select = -c(3))
    
    dataframes[[country_name]] <- df
    
  }
  
  #create just a single df
  combined_df <- do.call(rbind, dataframes)
  #delete row names
  rownames(combined_df)<-NULL
  
  #set country names with capital letter
  combined_df$country <- stringr::str_to_title(combined_df$country)
  
  return(combined_df)
  
}





