# Pie chart

# Create Data
tree_data <- c(105, 50, 45)
tree_labels <- c("Jeffrey Pine", "Ponderosa", "White Fir")

# Make the default Pie Plot
dev.new()
pie(tree_data, labels=tree_labels)

# And a bar chart
barplot(height=tree_data, names=tree_labels, ylab="Counts")