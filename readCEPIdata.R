readBACIIdata <- function(path){
  csv_files <- list.files(path = path, pattern = "\\.csv$", full.names = TRUE)
  
  dataframes <- list()
  
  for(file in csv_files){
    df <- read.csv(file)
    csv_year <- tools::file_path_sans_ext(basename(file))
    
    
    
    df <- df[,-6] #remove quantity column
    df <- df[df$i=="156",] #keep obs where exporter is only China
    df <- df[df$k=="854140",] #keep obs for solar tech only (HS854140)
    
    dataframes[[csv_year]] <- df
  }
  
  #create just a single df
  combined_df <- do.call(rbind, dataframes)
  #delete row names
  rownames(combined_df)<-NULL
  
  return(combined_df)
    
    return(combined_df)
  
}

