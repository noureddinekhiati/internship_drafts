import splitfolders  # or import split_folders

input_folder = 'daata/'

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
#Train, val, test
splitfolders.ratio(input_folder, output="dataset_sup", 
                   seed=42, ratio=(.6, .1, .3), 
                   group_prefix=None) # default values